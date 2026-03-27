# AI Statistical Interpreter (2026 Edition)

An intelligent data reasoning engine built with Python, Streamlit, and the **Google GenAI 2.0 SDK**. This application automates the "State-Plan-Do-Conclude" workflow for statistical analysis by leveraging the Gemini 3 Flash model.

##  Technical Evolution (March 2026)
This project has been fully refactored to meet 2026 industry standards:
* **SDK Migration:** Transitioned from the deprecated `google-generativeai` to the modern `google-genai` client for improved latency and reliability.
* **Gemini 3 Integration:** Upgraded the reasoning engine to **Gemini 3 Flash**, resolving 404 errors caused by the retirement of the 1.5-series models.
* **Streamlit UI Compliance:** Refactored layout parameters to comply with the latest Streamlit frontend standards (v1.40+).

## Core Features
* **Automated FRQ Drafting:** Generates statistical conclusions in the formal AP Statistics format.
* **Advanced Outlier Detection:** Combines the mathematical 1.5xIQR rule with AI-driven contextual reasoning.
* **LaTeX Math Rendering:** Outputs professional-grade mathematical symbols ($\bar{x}$, $\sigma$, $\mu$) for academic reports.
* **Zero-Footprint Security:** Implements strict environment variable separation to protect API credentials.

## API Key & Security Setup
This project uses **Environment Variables** to keep your credentials safe.

1.  **Get a Key:** Obtain an API key from [Google AI Studio](https://aistudio.google.com/).
2.  **Local Configuration:** * Create a file named `.env` in the root directory.
    * Add your key: `GEMINI_API_KEY=your_secret_key_here`
3.  **GitHub Safety:** The `.gitignore` file is pre-configured to ensure your `.env` is never uploaded to the public repository.

##  Installation
Ensure you have Python 3.12+ installed, then run:

```bash
# Install the 2026 dependency stack
py -m pip install streamlit pandas google-genai python-dotenv
```
To launch the dashboard, run:
```bash
py -m streamlit run app.py
```
