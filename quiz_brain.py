class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.total_questions = len(q_list)

    def still_has_questions(self) -> bool:
        return False if (self.question_number == self.total_questions) else True

    def next_question(self) -> tuple:
        q = self.question_list[self.question_number]
        self.question_number += 1
        return f"Question # {self.question_number} {q.question}", q.answer.lower()
