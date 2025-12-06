# utils/ai_feedback.py

import streamlit as st
from transformers import pipeline

# Initialize the Hugging Face text-generation pipeline
@st.cache_resource(show_spinner=False)
def load_generator():
    return pipeline("text2text-generation", model="google/flan-t5-large")

generator = load_generator()


def generate_feedback(cv_text: str, jd_text: str) -> str:
    """
    Generates AI feedback for a CV vs JD comparison using flan-t5-large.
    Falls back to a keyword-based message if generation fails.
    """
    if not cv_text or not jd_text:
        return "Please upload both CV and JD."

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
        # Fallback keyword-based feedback
        return (
            "AI feedback unavailable. Here's a simple summary:\n\n"
            "- Make sure your CV matches key skills in the JD.\n"
            "- Highlight relevant experience and achievements.\n"
            "- Include measurable results where possible.\n"
            "- Tailor your CV to the job requirements."
        )
