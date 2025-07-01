from gemini.gemini_utils import generate_quiz_with_gemini, explain_topic_with_gemini

def generate_response(action: str, subject: str, topic: str) -> str:
    if action == "generate_quiz":
        return generate_quiz_with_gemini(subject, topic)

    elif action == "explain_topic":
        return explain_topic_with_gemini(subject, topic)

    elif action == "summarize_topic":
        return f"⚠️ Summary generation not yet implemented."

    else:
        return "🤖 I'm not sure what you're asking. Do you want a quiz, explanation, or summary?"
