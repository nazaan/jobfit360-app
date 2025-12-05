import openai

# Make sure your OpenAI API key is set in Streamlit secrets or environment variable
# e.g., st.secrets["OPENAI_API_KEY"] or os.environ["OPENAI_API_KEY"]

def generate_feedback(cv_text: str, jd_text: str, api_key: str) -> str:
    """
    Generate AI feedback on CV vs JD.
    Returns a string with summary, positives, and improvement suggestions.
    """
    if not cv_text or not jd_text:
        return "Please provide both CV and JD text."

    prompt = f"""
You are a career coach. Given the candidate CV and the Job Description,
provide:
1. A short summary paragraph of the candidate's fit
2. Positive points from the CV
3. Suggestions for improvement to better match the JD

CV:
{cv_text}

JD:
{jd_text}

Please format your response clearly.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300,
        api_key=api_key
    )

    return response.choices[0].message.content.strip()

