class StateTracker:
    def __init__(self):
        self.state = {
            "subject": None,
            "topic": None,
            "last_action": None,
            "history": []
        }

    def update(self, subject: str, topic: str, action: str, response: str):
        self.state["subject"] = subject
        self.state["topic"] = topic
        self.state["last_action"] = action
        self.state["history"].append({
            "subject": subject,
            "topic": topic,
            "action": action,
            "response": response
        })

    def get_last(self):
        return self.state.get("last_action"), self.state.get("subject"), self.state.get("topic")

    def get_history(self):
        return self.state["history"]
