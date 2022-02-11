import html

class Quiz_Logic:

    def __init__(self,list):
        self.q_number = 0
        self.score = 0
        self.q_list = list
        self.current_question = None

    def still_has_question(self):
        #checks if there is another question in the list
        return self.q_number < len(self.q_list)

    def next_question(self):
        #returns question text from selected Question in the list
        self.current_question = self.q_list[self.q_number]
        self.q_number += 1
        #corrects special characters
        question = html.unescape(self.current_question.question_text)
        return f"{self.q_number}) {question} (True/False)"

    def check_answer(self,user_response):
        #returns boolean and changes score depending on answer
        correct_answer = self.current_question.question_answer
        if user_response == correct_answer:
            self.score += 1
            return True
        else:
            return False