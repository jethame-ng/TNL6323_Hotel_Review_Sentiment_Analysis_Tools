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

    try:
    response = model.generate_content(prompt)
    return response.text

    except Exception as e:
        return (
            "The AI assistant is temporarily unavailable due to API quota or service limits. "
            "Based on the dashboard results, please refer to the benchmark comparison, top strengths, "
            "top issues, and management recommendations shown above."
        )
