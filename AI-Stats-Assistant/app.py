import streamlit as st
import pandas as pd
from google import genai
import os
from dotenv import load_dotenv

# 1. Securely Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found. Please check your .env file.")
else:
    client = genai.Client(api_key=api_key)
    model_id = "gemini-3-flash-preview"

# 2. UI Configuration
st.set_page_config(page_title="AI Stats Interpreter", page_icon="📊")
st.title("📊 AI Statistical Interpreter")

# 3. Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Sidebar and File Upload
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head(5), width="stretch")
    
    cols = df.select_dtypes(include=['number']).columns.tolist()
    target = st.selectbox("Select variable for initial analysis:", cols)
    
    if st.button("Run Initial Analysis"):
        desc_stats = df[target].describe().to_dict()
        
        analysis_prompt = f"Analyze the distribution of '{target}' based on these stats: {desc_stats}. Provide shape, center, spread, and outlier check."
        
        with st.spinner("Analyzing..."):
            try:
                response = client.models.generate_content(model=model_id, contents=analysis_prompt)
                # Save to chat history
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error: {e}")

# 5. Chat Interface
st.divider()
st.subheader("Chat with your Data")

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box
if prompt := st.chat_input("Ask a follow-up question about your data..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Send the entire history to maintain context
                chat_response = client.models.generate_content(
                    model=model_id,
                    contents=[{"role": m["role"], "parts": [{"text": m["content"]}]} for m in st.session_state.messages]
                )
                st.markdown(chat_response.text)
                st.session_state.messages.append({"role": "assistant", "content": chat_response.text})
            except Exception as e:
                st.error(f"Error: {e}")
else:
    if not uploaded_file:
        st.info("Upload a dataset to begin the analysis and chat.")
