from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data import Data
from game_ui import Game_UI
from question import Question
from quiz_logic import Quiz_Logic

MENU_BG = '#00B4D8'
MENU_TEXT_COLOR = '#EEEEEE'
BG_THEME = '#375362'


def start():
    params:dict
    #checks if necessary parameters are selected
    if num_questions.get() == 'Select an Option' or difficulty.get() == 'Select an Option':
            messagebox.showinfo(title='Hold on',message='Please select the number of questions.')
            return
    #parameters if user chooses a specific difficulty level
    elif difficulty.get() != 'Any':
        diff = difficulty.get().lower()
        num = int(num_questions.get())
        params = {'amount':num,
                    'difficulty':diff,
                    'type':'boolean'}
    #if user allows random difficulty
    else:
        num = int(num_questions.get())
        params = {'amount':num,
                    'type':'boolean'}
    #passes parameters into api call
    game = Data(params)
    questions_list = []
    #creates Question objects using results from API call in Data
    for question in game.question_data:
        question_text = question['question']
        answer = question['correct_answer']
        new_question = Question(question_text,answer)
        questions_list.append(new_question)
    #passes lists of Question objects into Quiz_Logic
    quiz = Quiz_Logic(questions_list)
    #closes menu window and opens trivia game with logic and questions based on user selections
    window.destroy()
    ui = Game_UI(quiz)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Menu')
window.config(padx=20,pady=20,bg=MENU_BG)
title_label = Label(text='Select from the following',bg=MENU_BG,
                    fg=MENU_TEXT_COLOR,font=('Arial',24,'bold'))
title_label.grid(column=0,row=0,columnspan=2)
difficulty_label = Label(text='Difficulty',bg=MENU_BG,
                         fg=MENU_TEXT_COLOR,font=('Arial',16),pady=40)
difficulty_label.grid(column=0,row=1,sticky=W)
number_q_label = Label(text='Number of Questions',bg=MENU_BG,fg=MENU_TEXT_COLOR,font=('Arial',16))
number_q_label.grid(column=0,row=2,sticky=W)
# difficulty combobox
difficulty_options = ['Easy','Medium','Hard','Any']
dif_value_inside = StringVar(window)
dif_value_inside.set('Select an Option')
difficulty = ttk.Combobox(window,textvariable=dif_value_inside)
difficulty['values'] = difficulty_options
difficulty.config(font=('Arial',14))
difficulty.grid(column=1,row=1)
#number of questions combobox
number_options = ['5','10','15','20']
num_val_inside = StringVar(window)
num_val_inside.set('Select an Option')
num_questions = ttk.Combobox(window,textvariable=num_val_inside)
num_questions['values'] = number_options
num_questions.config(font=('Arial',14))
num_questions.grid(column=1,row=2)
start_button = Button(text='Start',width=34,font=('Arial',16,'bold'),
                        fg=MENU_TEXT_COLOR,bg='#375362',command=start)
start_button.grid(column=0,row=3,columnspan=2,pady=(40,0))


window.mainloop()


