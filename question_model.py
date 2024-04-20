class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def question_str(self):
        return f"Q: {self.text}\nA: {self.answer}"