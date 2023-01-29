from question_model import Question
from data import q_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [Question(q["question"].encode("utf-8"), q["correct_answer"]) for q in q_data["results"]]
qB = QuizBrain(question_bank)
ui = QuizInterface(qB)

# print(f"Your result is {qB.correct_answers}/{qB.total_questions}")
