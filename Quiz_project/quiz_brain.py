#TODO: Asking the questions
#TODO: Checking if the answer was correct
#TODO: Chcecking if we're at the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        #Her lager vi attributter som objektet skal ha
        self.score = 0
        self.question_number = 0
        self.question_list = q_list
        
    def still_has_questions(self):
        #returns a boolean depending on the value of questions_number
        #if self.question_number < len(self.question_list):
        #            return True
        #return False
        #De funker likt den over og under
        return self.question_number < len(self.question_list)

    def next_question(self):
        #Retrieve the item at the current question_number from the question_list
        #use the input() function to show the user the question text and ask for the user's anser
        current_question = self.question_list[self.question_number]
        
        #For at tallet bak Q.(TALL) skal starte med 1
        self.question_number += 1
        user_answers = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        self.checkAnswer(user_answers, current_question.answer)

    def checkAnswer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"That is correct!")
        else:
            print(f"That is unfortuantely wrong. The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
