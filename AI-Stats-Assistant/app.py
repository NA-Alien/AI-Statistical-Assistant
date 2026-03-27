import streamlit as st
import pandas as pd
from google import genai
import os
from dotenv import load_dotenv

# 1. Securely Load API Key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found. Please check your .env file.")
else:
    # Initialize the 2026 GenAI Client
    client = genai.Client(api_key=api_key)
    # Using the Gemini 3 Flash model for 2026 performance and reliability
    model_id = "gemini-3-flash-preview"

# 2. UI Configuration (2026 Standards)
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
    
    # Updated width='stretch' to comply with 2026 Streamlit standards
    st.dataframe(df.head(10), width="stretch")
    
    # Filter for numerical columns only
    cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if not cols:
        st.error("No numerical columns found in this file.")
    else:
        target = st.selectbox("Select variable for AI reasoning:", cols)
        
        if st.button("Run AI Analysis"):
            # Generate descriptive statistics dictionary for the AI
            desc_stats = df[target].describe().to_dict()
            
            # Professional prompt optimized for Gemini 3 reasoning
            prompt = f"""
            CONTEXT: You are a Lead Data Scientist and AP Statistics expert. 
            DATA SUMMARY for variable '{target}': {desc_stats}
            
            TASK:
            1. Interpret the distribution (Shape, Center, Spread). Use LaTeX for symbols like x-bar or sigma.
            2. Specifically check for outliers using the 1.5xIQR method.
            3. Draft a 'Conclusion' as if for an AP Statistics Free Response Question (FRQ).
            4. Suggest one follow-up experiment or data collection method to improve results.
            
            STYLE: Clear, academic, and concise. No conversational filler.
            """
            
            with st.spinner("AI is analyzing data patterns..."):
                try:
                    # New 2026 generation call
                    response = client.models.generate_content(
                        model=model_id, 
                        contents=prompt
                    )
                    st.subheader("AI Findings")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.info("Check if your API key is correct and your internet connection is stable.")

else:
    st.info("System Ready. Please upload a dataset in the sidebar to begin.")
