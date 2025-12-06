# utils/ai_feedback.py

# Option A: Free Hugging Face model (default for now)
from transformers import pipeline

# Load model once (small, fast)
generator = pipeline("text2text-generation", model="google/flan-t5-small")

def generate_feedback(cv_text: str, jd_text: str, use_openai=True, api_key=OPEN_AI_KEY) -> str:
    """
    Generate feedback on CV vs JD.
    By default uses a free local LLM.
    Set use_openai=True to use OpenAI API instead (requires key).
    """
    if not cv_text or not jd_text:
        return "Please provide both CV and JD text."

    prompt = f"""
Candidate CV:
{cv_text}

Job Description:
{jd_text}

Provide:
1. Short summary of fit
2. Positive points
3. Suggestions to improve match
"""

    if use_openai and api_key:
        # Optional OpenAI code (kept for future)
        import openai
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300,
            api_key=api_key
        )
        return response.choices[0].message.content.strip()
    
    # Default: use Hugging Face small model
    output = generator(prompt, max_length=300, do_sample=True)
    return output[0]["generated_text"]
