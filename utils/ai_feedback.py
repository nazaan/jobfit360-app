# utils/ai_feedback.py

import streamlit as st
import openai

def generate_feedback(cv_text: str, jd_text: str, use_openai=True) -> str:
    """
    Generates feedback using OpenAI if key exists.
    Otherwise returns a simple fallback message.
    """

    if not cv_text or not jd_text:
        return "Please upload both CV and JD before generating feedback."

    openai_key = st.secrets.get("OPENAI_API_KEY", None)

    if use_openai and openai_key:
        openai.api_key = openai_key

        prompt = f"""
CV:
{cv_text}

Job Description:
{jd_text}

Give:
1. Short summary of match
2. Strengths
3. Weak points
4. Suggestions to improve
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                max_tokens=350,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"Error contacting OpenAI: {e}"

    # Fallback (no OpenAI key)
    return "AI feedback unavailable (no OpenAI key set)."
