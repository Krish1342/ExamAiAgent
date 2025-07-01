def decide_next_action(parsed_input: dict, state: dict) -> str:
    if parsed_input["intent"] == "quiz_me":
        return "generate_quiz"
    elif parsed_input["intent"] == "explain":
        return "explain_topic"
    elif parsed_input["intent"] == "summarize":
        return "summarize_topic"
    else:
        return "ask_followup"
