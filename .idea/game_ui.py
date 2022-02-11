from tkinter import *
from quiz_logic import Quiz_Logic

class Game_UI:
    def __init__(self, logic:Quiz_Logic):
        self.quiz = logic
        THEME_COLOR = "#375362"
        self.window = Tk()
        self.window.title("Trivia Time")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0',bg=THEME_COLOR,fg='white',font=('Arial',16))
        self.score_label.grid(column=1,row=0,sticky=E)
        self.canvas = Canvas(width=300,height=250,border=0)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=40)
        self.canvas_text = self.canvas.create_text(150,125,text='some question',width=260,
                                                   fill=THEME_COLOR,font=('Arial',14,'italic'))
        true_path = 'images/true.png'
        false_path = 'images/false.png'
        true_pic = PhotoImage(file=true_path)
        false_pic = PhotoImage(file=false_path)
        self.true_button = Button(image=true_pic,border=0,highlightthickness=0,command=self.select_True)
        self.true_button.grid(column=0,row=2,sticky=W)
        self.false_button = Button(image=false_pic,border=0,highlightthickness=0,command=self.select_False)
        self.false_button.grid(column=1,row=2,sticky=E)
        self.update_question()

        self.window.mainloop()

    def update_question(self):
        #updates canvas with question text
        self.canvas.config(bg='white')
        #prevents out of bounds error
        if self.quiz.still_has_question():
            next_q = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text=next_q)
        else:
        #ends game if out of questions
            self.canvas.itemconfig(self.canvas_text,
                                   text=f"You have completed the quiz."
                                        f"\nYour final score:{self.quiz.score}/{self.quiz.q_number}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def update_score(self):
        #update score label to reflect change in score
        score = self.quiz.score
        self.score_label.config(text=f'Score: {score}')


    def select_True(self):
        #Gets boolean value when checking answer
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
        self.update_score()


    def select_False(self):
        #Gets boolean value when checking answer
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        self.update_score()


    def give_feedback(self,is_right):
        #canvas flashes red or green then shows the next question
        if is_right:
            self.canvas.config(bg='green')
            self.window.after(500,self.update_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(500,self.update_question)
