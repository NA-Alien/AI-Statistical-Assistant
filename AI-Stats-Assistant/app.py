import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Securely Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found. Please check your .env file.")
else:
    genai.configure(api_key=api_key)
    # Using the flash model for speed and cost-efficiency
    model = genai.GenerativeModel('gemini-1.5-flash')

# 2. UI Configuration
st.set_page_config(page_title="AI Stats Interpreter", page_icon="📊")
st.title("📊 AI Statistical Interpreter")
st.markdown("""
    This assistant uses **Generative AI** to analyze datasets, verify conditions, 
    and draft formal statistical reports.
""")

# 3. Sidebar and File Upload
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head(10), use_container_width=True)
    
    cols = df.select_dtypes(include=['number']).columns.tolist()
    target = st.selectbox("Select variable for AI reasoning:", cols)
    
    if st.button("Run AI Analysis"):
        # Generate stats for the AI to "see"
        desc_stats = df[target].describe().to_dict()
        
        # Crafting the Professional Prompt
        prompt = f"""
        CONTEXT: You are a Lead Data Scientist. 
        DATA SUMMARY for variable '{target}': {desc_stats}
        
        TASK:
        1. Interpret the distribution (Shape, Center, Spread).
        2. Specifically check for outliers using the 1.5xIQR method.
        3. Draft a 'Conclusion' as if for an AP Statistics Free Response Question (FRQ).
        4. Suggest one follow-up experiment or data collection method to improve results.
        
        STYLE: Clear, academic, and concise. No conversational filler.
        """
        
        with st.spinner("Analyzing data patterns..."):
            try:
                response = model.generate_content(prompt)
                st.subheader("AI Findings")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")

else:
    st.info("Waiting for dataset upload...")
