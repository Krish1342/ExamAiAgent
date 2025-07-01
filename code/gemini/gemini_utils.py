
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise Exception("❌ GEMINI_API_KEY is not set in your .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Use a valid and available model
MODEL_NAME = "models/gemini-2.5-pro"
model = genai.GenerativeModel(model_name=MODEL_NAME)

# ✅ Function: Generate a quiz using Gemini
def generate_quiz_with_gemini(subject: str, topic: str, num_questions: int = 3) -> str:
    prompt = f"""
Generate {num_questions} multiple-choice quiz questions for high school students on the topic "{topic}" in the subject "{subject}".
Each question should include:
- a clear question
- four options (a, b, c, d)
- the correct answer labeled like: Answer: a/b/c/d
Return as clean formatted text.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating quiz with Gemini: {str(e)}"

# ✅ Function: Explain a topic using Gemini
def explain_topic_with_gemini(subject: str, topic: str) -> str:
    prompt = f"""
Explain the topic "{topic}" in the subject "{subject}" for a 10th-grade student.
Use simple language, ~100 words max, and give a relatable real-world example.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating explanation with Gemini: {str(e)}"

# ✅ Function: Summarize a topic using Gemini
def summarize_topic_with_gemini(subject: str, topic: str) -> str:
    prompt = f"""
Summarize the topic "{topic}" in the subject "{subject}" for a student in under 5 bullet points.
Keep it concise and helpful for quick revision.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating summary with Gemini: {str(e)}"
