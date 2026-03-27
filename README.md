# AI Statistical Interpreter 

An intelligent data reasoning engine built with Python, Streamlit, and the **Google GenAI 2.0 SDK**. This application automates statistical analysis and provides a persistent chat interface for interactive data exploration using the Gemini 3 Flash model.

## Technical Evolution 
* **SDK Migration:** Transitioned from the deprecated `google-generativeai` to the modern `google-genai` client.
* **Gemini 3 Integration:** Upgraded the reasoning engine to **Gemini 3 Flash**, resolving 404 errors associated with retired 1.5-series models.
* **Persistent Chat:** Implemented `st.session_state` to maintain conversation memory, allowing for iterative follow-up questions.
* **Streamlit UI Compliance:** Refactored layout parameters to comply with v1.40+ standards using `width='stretch'`.

## Core Features
* **Initial Statistical Analysis:** Automatically generates shape, center, spread, and 1.5xIQR outlier checks for uploaded datasets.
* **Interactive Data Chat:** A dedicated messaging interface to ask follow-up questions about specific data points or trends.
* **LaTeX Math Rendering:** Displays professional-grade mathematical symbols (x-bar, sigma, mu) in all AI responses.
* **Zero-Footprint Security:** Strict separation of API credentials using environment variables.

## API Key and Security Setup
This project requires a Google API key.

1.  **Obtain Key:** Generate an API key via Google AI Studio.
2.  **Local Configuration:** * Create a file named `.env` in the root directory.
    * Add your key: `GEMINI_API_KEY=your_secret_key_here`
3.  **Security:** The `.gitignore` file ensures your `.env` is never uploaded to public repositories. Refer to `.env.example` for the required format.

## Installation
Ensure Python 3.12+ is installed, then run:

```bash
# Install the 2026 dependency stack
py -m pip install streamlit pandas google-genai python-dotenv
```
To launch the dashboard, run:
```bash
py -m streamlit run app.py
```

## Uploading Data
Ensure files uploaded are .csv files (e.g. `dataset1.csv`) 

Format data within these files in this way:
```
Study_Hours,Test_Score
2,65
3,70
4,75
5,80
6,85
7,88
8,92
9,95
10,99
1,40
```

