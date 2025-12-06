# utils/ai_feedback.py

import streamlit as st
from transformers import pipeline

# Initialize the text-generation pipeline (flan-t5-base is lighter and stable on free-tier)
try:
    generator = pipeline("text2text-generation", model="google/flan-t5-base")
except Exception as e:
    st.warning(f"Could not load AI model: {e}")
    generator = None


def generate_feedback(cv_text: str, jd_text: str) -> str:
    """
    Generates AI feedback for a CV vs JD comparison.
    Uses flan-t5-base. Falls back to keyword guidance if generation fails.
    """
    if not cv_text or not jd_text:
        return "Please upload both CV and JD."

    if generator is None:
        return (
            "AI feedback unavailable. Here's a simple summary:\n\n"
            "- Make sure your CV matches key skills in the JD.\n"
            "- Highlight relevant experience and achievements.\n"
            "- Include measurable results where possible.\n"
            "- Tailor your CV to the job requirements."
        )

    prompt = f"""
CV:
{cv_text}

Job Description:
{jd_text}

Analyze and provide:
- Summary of match
- Strengths
- Weak areas
- Suggestions to improve
"""

    try:
        result = generator(
            prompt,
            max_length=600,
            do_sample=True,
            temperature=0.4
        )
        feedback = result[0]['generated_text']
        if not feedback.strip():
            raise ValueError("Empty feedback generated.")
        return feedback

    except Exception as e:
        return (
            "AI feedback unavailable. Here's a simple summary:\n\n"
            "- Make sure your CV matches key skills in the JD.\n"
            "- Highlight relevant experience and achievements.\n"
            "- Include measurable results where possible.\n"
            "- Tailor your CV to the job requirements."
        )
