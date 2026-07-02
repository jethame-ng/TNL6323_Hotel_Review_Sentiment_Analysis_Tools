import google.generativeai as genai
import streamlit as st

from chatbot.prompt import build_prompt

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

    response = model.generate_content(prompt)

    return response.text