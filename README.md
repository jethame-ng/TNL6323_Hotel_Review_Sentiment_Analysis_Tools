# 🏨 Intelligent Hotel Review Sentiment Analysis System

An AI-powered web application for analysing hotel customer reviews using **sentiment analysis**, **aspect-based sentiment analysis**, **hotel benchmarking**, and an **LLM-powered Hotel Management Assistant**.

The system was developed using **Python**, **Streamlit**, **DistilBERT**, and **Google Gemini** to assist hotel management in monitoring customer satisfaction and supporting data-driven decision making.

---

# 🚀 Features

- 📊 Hotel Dashboard
  - Overall sentiment summary
  - Sentiment distribution
  - Sentiment trend analysis
  - Aspect-based sentiment analysis
  - Benchmark comparison
  - Management recommendations

- 📝 Analyse New Review
  - Overall sentiment prediction
  - Aspect detection
  - Clause segmentation
  - Aspect-level sentiment analysis
  - Prediction confidence

- 🤖 AI Hotel Management Assistant
  - Executive summary
  - Competitor benchmarking
  - Hotel strengths
  - Improvement recommendations
  - Interactive question answering

---

# 🛠 Technology Stack

- Python
- Streamlit
- DistilBERT
- Hugging Face Hub
- Google Gemini API
- Pandas
- Scikit-learn
- Matplotlib

---

# 📋 System Requirements

| Software | Version |
|----------|---------|
| Python | 3.10 or later |
| Git | Latest Version |
| Streamlit | Installed via requirements.txt |
| Visual Studio Code (Optional) | Latest Version |

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<username>/TNL6323_Hotel_Review_Sentiment_Analysis_Tools.git
```

```bash
cd TNL6323_Hotel_Review_Sentiment_Analysis_Tools
```

---

## 2. (Optional) Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

Install all required packages using

```bash
pip install -r requirements.txt
```

---

# 📁 Project Structure

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

---

## Folder Description

| Folder/File | Description |
|-------------|-------------|
| `.devcontainer/` | Development container configuration. |
| `.vscode/` | Visual Studio Code settings. |
| `chatbot/` | AI Hotel Management Assistant modules. |
| `data/` | Hotel review datasets. |
| `model/` | Notes regarding the Hugging Face hosted model. |
| `pages/` | Streamlit application pages. |
| `utils/` | Utility functions and sentiment prediction module. |
| `app.py` | Main Streamlit application. |
| `requirements.txt` | Required Python libraries. |

---

# ▶ Running the Application

Run the application using

```bash
streamlit run app.py
```

The application will open automatically.

The sentiment classification model is hosted on the **Hugging Face Hub** and is automatically loaded during execution.

---

# 📊 Using the System

## Hotel Dashboard

- Select hotel
- Overall sentiment summary
- Sentiment trend
- Aspect analytics
- Benchmark comparison
- Management recommendations
- AI Hotel Management Assistant
- Review preview

---

## Analyse New Review

1. Enter a hotel review.
2. Click **Analyse Review**.
3. View:

- Overall sentiment
- Prediction confidence
- Clause segmentation
- Detected aspects
- Aspect sentiment analysis
- Analysis summary

---

# ☁ Streamlit Deployment

The system can also be accessed using the deployed Streamlit application.

```
https://your-streamlit-url.streamlit.app
```

The application remains publicly accessible as long as:

- the Streamlit application remains deployed,
- the GitHub repository remains available,
- Streamlit Community Cloud continues hosting the application.

---

# 🔧 Troubleshooting

| Problem | Solution |
|----------|----------|
| Module not found | Run `pip install -r requirements.txt` |
| Streamlit command not found | Install Streamlit |
| Missing dataset | Ensure CSV files are inside the `data` folder |
| Model loading error | Ensure internet connection for Hugging Face Hub |
| Gemini API error | Configure the Gemini API key |
| App fails to start | Verify all dependencies are installed |

---

# 📝 Additional Notes

- Do not modify the datasets inside the `data` folder.
- Internet connection is required for the AI Hotel Management Assistant.
- The DistilBERT model is automatically downloaded from the Hugging Face Hub.
- Pull the latest version from GitHub to obtain updates.

---

# 👥 Authors

Developed for **TNL6323 – Natural Language Processing**  
Bachelor of Computer Science (Hons.) Artificial Intelligence  
Multimedia University (MMU), Melaka
