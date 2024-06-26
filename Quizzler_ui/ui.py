from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
font = ("Arial", 20, "italic")
class QuizUi():

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(150,
                                                125,
                                                text="",
                                                font=font,
                                                fill=THEME_COLOR,
                                                width=280
                                                )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.question_true)
        self.true_button.grid(column=0, row=2)

        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, command=self.question_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def question_true(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)
    def question_false(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


