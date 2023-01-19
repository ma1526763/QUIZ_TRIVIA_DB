class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.correct_answers = 0
        self.question_list = q_list
        self.total_questions = len(q_list)

    def still_has_questions(self):
        return False if (self.question_number == self.total_questions) else True

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Question # {self.question_number} {q.question} (True/False)? "
        ).lower()
        self.check_answer(user_answer, q.answer.lower())
        print()

    def check_answer(self, u_a, answer):
        if u_a == answer:
            self.correct_answers += 1
            print("You guess it right")
        else:
            print("Wrong answer")
        print(f"Your current score is {self.correct_answers}/{self.question_number}")
