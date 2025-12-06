# utils/ai_feedback.py

import streamlit as st

# Hugging Face imports
try:
    from transformers import pipeline
    hf_available = True
except ImportError:
    hf_available = False

def generate_feedback(cv_text: str, jd_text: str, use_openai=False) -> str:
    """
    Generates feedback using Hugging Face if available.
    Falls back to simple keyword-based feedback if Hugging Face is unavailable.
    OpenAI is optional and can be enabled in the future.
    """

    if not cv_text or not jd_text:
        return "Please upload both CV and JD."

    # -----------------------------
    # 1️⃣ Hugging Face AI feedback
    # -----------------------------
    if hf_available:
        try:
            generator = pipeline("text2text-generation", model="google/flan-t5-large")
            prompt = f"""
CV:
{cv_text}

Job Description:
{jd_text}

Analyze the following CV against the Job Description. Give a short summary of the match, strengths, weak points, and tips for improvement.
"""
            output = generator(prompt, max_length=200)
            return output[0]["generated_text"]
        except Exception as e:
            st.warning(f"Hugging Face model error: {e}")

    # -----------------------------
    # 2️⃣ Fallback keyword-based feedback
    # -----------------------------
    cv_words = set(cv_text.lower().split())
    jd_words = set(jd_text.lower().split())
    matched = cv_words & jd_words
    missing = jd_words - cv_words

    feedback = f"**Matched keywords:** {', '.join(list(matched)[:20])}\n"
    feedback += f"**Missing keywords:** {', '.join(list(missing)[:20])}\n"
    feedback += "You can improve by adding missing skills/keywords."
    return feedback
