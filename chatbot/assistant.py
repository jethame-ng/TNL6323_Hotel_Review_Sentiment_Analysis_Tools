import google.generativeai as genai
import streamlit as st

from chatbot.prompt import build_prompt
from google.api_core.exceptions import ResourceExhausted

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(
    selected_hotel,
    compare_hotel,
    sentiment_counts,
    comparison,
    recommendations,
    question,
):

    prompt = build_prompt(
        selected_hotel,
        compare_hotel,
        sentiment_counts,
        comparison,
        recommendations,
        question,
    )

    try:
        response = model.generate_content(prompt)
        return response.text

    except ResourceExhausted:
        return (
            "⚠️ Gemini API quota exceeded.\n\n"
            "Please try again later."
        )

    except Exception as e:
        return f"LLM Error: {e}"
