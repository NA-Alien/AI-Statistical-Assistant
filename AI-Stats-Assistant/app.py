import streamlit as st
import pandas as pd
import google.generativeai as genai

# Setup API Key (Replace with your actual key for testing, but use secrets for GitHub)
API_KEY = "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Stats Assistant", layout="wide")
st.title("🤖 AI Stats Assistant")
st.markdown("Upload data and let the AI perform the heavy lifting for your analysis.")

# Sidebar for Upload
uploaded_file = st.sidebar.file_uploader("Upload CSV Data", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())
    
    # Select a column for analysis
    cols = df.select_dtypes(include=['number']).columns.tolist()
    selection = st.selectbox("Which variable should the AI analyze?", cols)
    
    if st.button("Generate AI Insights"):
        # Prepare the data summary for the AI
        stats_summary = df[selection].describe().to_string()
        
        prompt = f"""
        Act as an AP Statistics Reader. Analyze this dataset for the variable '{selection}':
        {stats_summary}
        
        1. Describe the Shape, Center, and Spread.
        2. Identify if there are potential outliers using the 1.5xIQR rule.
        3. Suggest the most appropriate inference test (e.g., 1-Sample T-Test) and state the conditions needed.
        Keep the tone professional and tuned for 11th grade academic writing.
        """
        
        with st.spinner("AI is thinking..."):
            response = model.generate_content(prompt)
            st.write("### AI Statistical Interpretation")
            st.info(response.text)
else:
    st.info("Upload a CSV to get started with AI-powered insights.")