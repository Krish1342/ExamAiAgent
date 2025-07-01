def parse_user_input(message: str) -> dict:
    message = message.lower()
    intent = "unknown"
    subject = ""
    topic = ""
    question_type = ""

    if "quiz" in message:
        intent = "quiz_me"
        question_type = "quiz"
    elif "explain" in message:
        intent = "explain"
        question_type = "explanation"
    elif "summarize" in message:
        intent = "summarize"
        question_type = "summary"

    # crude topic/subject parsing
    if "biology" in message:
        subject = "biology"
    if "photosynthesis" in message:
        topic = "photosynthesis"

    return {
        "intent": intent,
        "subject": subject,
        "topic": topic,
        "question_type": question_type
    }
