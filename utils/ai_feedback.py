import streamlit as st
from openai import OpenAI
import os

def generate_feedback(cv_text: str, jd_text: str, use_openai=True) -> str:
    if not cv_text or not jd_text:
        return "Please upload both CV and JD."

    openai_key = st.secrets.get("OPENAI_API_KEY", None)

    if use_openai and openai_key:
        try:
            os.environ["OPENAI_API_KEY"] = openai_key
            client = OpenAI(api_key=openai_key)

            prompt = f"""
CV:
{cv_text}

Job Description:
{jd_text}

Provide:
1. Summary of match
2. Strengths
3. Weak areas
4. Suggestions to improve
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                max_tokens=350,
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error contacting OpenAI: {e}"

    return "AI feedback unavailable (no OpenAI key set)."
