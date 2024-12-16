#A question model should have q_text as an attribute, q_answer

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer