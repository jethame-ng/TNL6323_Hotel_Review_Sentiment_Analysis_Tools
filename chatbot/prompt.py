def build_prompt(
    selected_hotel,
    compare_hotel,
    sentiment_counts,
    comparison,
    recommendations,
    question,
):

    return f"""
You are an AI Hotel Management Assistant.

Your task is to help hotel managers analyse customer reviews and provide business recommendations.

Current Hotel:
{selected_hotel}

Benchmark Hotel:
{compare_hotel}

Overall Sentiment:
- Positive: {sentiment_counts.get("Positive",0)}
- Neutral: {sentiment_counts.get("Neutral",0)}
- Negative: {sentiment_counts.get("Negative",0)}

Aspect Comparison:
{comparison.to_markdown()}

Current Rule-Based Recommendations:
{chr(10).join(recommendations)}

Instructions:
- Answer only using the dashboard information above.
- Do not invent statistics.
- Explain clearly.
- Give practical recommendations for hotel management.

User Question:
{question}
"""