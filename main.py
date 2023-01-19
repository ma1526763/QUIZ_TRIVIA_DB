from question_model import Question
from data import q_data
from quiz_brain import QuizBrain

question_bank = [Question(q["question"].encode("utf-8"), q["correct_answer"]) for q in q_data["results"]]
qB = QuizBrain(question_bank)
while qB.still_has_questions():
    answer = qB.next_question()
print(f"Your result is {qB.correct_answers}/{qB.total_questions}")
