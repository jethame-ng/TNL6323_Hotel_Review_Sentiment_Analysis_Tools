# 🏨 Intelligent Hotel Review Sentiment Analysis System

An AI-powered hotel review sentiment analysis system developed using **Python** and **Streamlit**. The system assists hotel management in analysing customer reviews through sentiment analysis, aspect-based sentiment analysis, hotel benchmarking, and AI-powered management recommendations.

---

# 1. Introduction

This project provides an interactive web application for hotel management to analyse customer reviews collected from Booking.com. The application integrates sentiment classification, aspect-based sentiment analysis, hotel benchmarking, and an AI Hotel Management Assistant to support data-driven decision-making.

---

# 2. System Requirements

Before running the application, ensure that the following software is installed.

| Software | Version |
|----------|----------|
| Python | 3.10 or later |
| Git | Latest version |
| Visual Studio Code (Optional) | Latest version |
| Streamlit | Installed through `requirements.txt` |

---

# 3. Installation

## Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/jethame-ng/TNL6323_Hotel_Review_Sentiment_Analysis_Tools.git
```

Move into the project directory.

```bash
cd TNL6323_Hotel_Review_Sentiment_Analysis_Tools
```

The remaining setup steps should be performed inside the project directory.

---

## Step 2: Create a Virtual Environment (Optional)

Creating a virtual environment is recommended to avoid package conflicts.

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## Step 3: Install Required Packages

Install all required dependencies.

```bash
pip install -r requirements.txt
```

This automatically installs all required Python packages.

---

# 4. Project Structure

```text
TNL6323_Hotel_Review_Sentiment_Analysis_Tools/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── .vscode/
│   └── settings.json
│
├── chatbot/
│   ├── assistant.py
│   └── prompt.py
│
├── data/
│   ├── Aspect_Hotel_Reviews.csv
│   └── Cleaned_Combined_Hotel_Reviews.csv
│
├── model/
│   └── note.txt
│
├── pages/
│   ├── 1_Hotel_Dashboard.py
│   └── 2_Analyse_New_Review.py
│
├── utils/
│   └── predictor.py
│
├── README.md
├── app.py
└── requirements.txt
```

| Folder/File | Description |
|--------------|-------------|
| `.devcontainer/` | Development container configuration for Visual Studio Code |
| `.vscode/` | Visual Studio Code workspace settings |
| `chatbot/` | AI Hotel Management Assistant modules |
| `data/` | Cleaned hotel review datasets |
| `model/` | Notes indicating the sentiment model is hosted on Hugging Face Hub |
| `pages/` | Streamlit pages |
| `utils/` | Utility functions such as sentiment prediction |
| `README.md` | Project documentation |
| `app.py` | Main Streamlit application |
| `requirements.txt` | Required Python packages |

---

# 5. Configure the Gemini API Key

The AI Hotel Management Assistant requires a valid Google Gemini API key.

## Step 1

Generate a Gemini API key from **Google AI Studio**.

## Step 2

Open your deployed Streamlit application.

Click:

- ⋮ (three-dot menu)
- **Settings**
- **Secrets**

## Step 3

Add the following secret.

```text
GEMINI_API_KEY = "your_gemini_api_key"
```

Replace `your_gemini_api_key` with your own API key.

## Step 4

Click **Save changes**.

The application will automatically use the configured API key.

---

# 6. Running the Application

If Streamlit has not already been installed through `requirements.txt`, install it manually.

```bash
python -m pip install streamlit
```

or

```bash
pip install streamlit
```

Run the application.

```bash
python -m streamlit run app.py
```

or

```bash
streamlit run app.py
```

After the application starts successfully, Streamlit automatically opens the application in your default web browser.

The sentiment model is hosted on the **Hugging Face Hub** and is downloaded automatically during execution.

An internet connection is required when using the AI Hotel Management Assistant.

---

# 7. Using the System

The application consists of two primary modules.

## 7.1 Hotel Dashboard

The Hotel Dashboard enables hotel management to:

- Select a hotel
- View overall sentiment summary
- View sentiment distribution
- View yearly sentiment trends
- Analyse aspect positive rates
- Compare hotels
- View benchmark analysis
- Generate management recommendations
- Interact with the AI Hotel Management Assistant
- Browse customer reviews

---

## 7.2 Analyse New Review

Users can:

1. Enter a hotel review.
2. Click **Analyse Review**.
3. View the generated results.

The system displays:

- Overall sentiment prediction
- Prediction confidence score
- Processed review clauses
- Detected hotel aspects
- Aspect-level sentiment analysis
- Analysis summary
- Aspect detection details

---

# 8. Streamlit Deployment

The deployed application is available through Streamlit Community Cloud.

**Application URL**

https://tnl6323hotelreviewsentimentanalysistools-mnychxhrm9bdmhwqxhxpp.streamlit.app

The deployed version provides the same functionality as the local application.

The public application remains available as long as:

- the Streamlit application remains deployed,
- the GitHub repository remains available,
- Streamlit Community Cloud continues hosting the application.

---

# 9. Troubleshooting

| Problem | Solution |
|----------|----------|
| Module not found | Run `pip install -r requirements.txt`. |
| Streamlit command not found | Install Streamlit using `python -m pip install streamlit` or `pip install streamlit`. |
| Missing dataset | Ensure the CSV files are inside the `data` folder. |
| Unable to load sentiment model | Ensure an internet connection is available so the model can be downloaded from the Hugging Face Hub. |
| Gemini API key not configured | Open **Settings → Secrets** in Streamlit and add `GEMINI_API_KEY = "your_api_key"`. |
| AI assistant does not respond | Verify that the Gemini API key is valid and that an internet connection is available. |
| Application fails to start | Verify that all dependencies listed in `requirements.txt` have been installed successfully. |

---

# 10. Additional Notes

- Do not modify or delete the CSV files inside the `data` folder.
- The application requires an internet connection when using the AI Hotel Management Assistant.
- The sentiment prediction model is automatically downloaded from the Hugging Face Hub.
- Updates can be obtained by pulling the latest version from the GitHub repository.
- Keep the `requirements.txt` file unchanged to ensure all required dependencies can be installed correctly.

---

# 11. Limitations

- The AI Hotel Management Assistant requires an active internet connection.
- Responses generated by the AI assistant depend on the availability of the Gemini API service.
- The sentiment model is downloaded from the Hugging Face Hub during its first execution
