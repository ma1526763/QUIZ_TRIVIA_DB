from tkinter import *
from quiz_brain import QuizBrain
import html
import time
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, qB: QuizBrain):
        self.score = 0
        self.question_original_answer = ""
        self.quiz_object = qB
        self.window = Tk()
        self.window.title("Quiz Api")
        self.window.config(padx=50, pady=50, background=THEME_COLOR)
        self.score_label = Label(text="Score: 0", background=THEME_COLOR, foreground="white", pady=-20)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=200)
        self.question_text = self.canvas.create_text(150, 100, width=280, text="question_text", font=("Arial", 16), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        tick_img = PhotoImage(file="images/true.png")
        cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=tick_img, borderwidth=0, highlightthickness=0, command=self.tick_pressed)
        self.tick_button = Button(image=cross_img, borderwidth=0, highlightthickness=0, command=self.cross_pressed)
        self.tick_button.grid(row=2, column=0)
        self.cross_button.grid(row=2, column=1)
        self.update_question()
        self.window.mainloop()

    def update_question(self):
        self.canvas.config(background="white")
        if self.quiz_object.still_has_questions():
            question, self.question_original_answer = self.quiz_object.next_question()
            self.canvas.itemconfig(self.question_text, text=html.unescape(question))
        else:
            self.canvas.itemconfig(self.question_text, text=f"You got {self.score}/{self.quiz_object.total_questions}")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def tick_pressed(self):
        self.check("true")

    def cross_pressed(self):
        self.check("false")

    def check(self, user_answer):
        if user_answer == self.question_original_answer:
            self.score += 1
            self.feedback("green")
        else:
            self.feedback("red")

    def feedback(self, color):
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.config(background=color)
        self.window.after(1000, self.update_question)
