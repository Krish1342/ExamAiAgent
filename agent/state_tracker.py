class StateTracker:
    def __init__(self):
        self.state = {
            "subject": None,
            "topic": None,
            "progress": {
                "quizzes_taken": [],
            },
            "last_question_type": None
        }

    def update(self, parsed_input: dict):
        self.state["subject"] = parsed_input["subject"]
        self.state["topic"] = parsed_input["topic"]
        self.state["last_question_type"] = parsed_input["question_type"]
        if parsed_input["intent"] == "quiz_me":
            self.state["progress"]["quizzes_taken"].append(parsed_input["topic"])

    def get_state(self):
        return self.state
