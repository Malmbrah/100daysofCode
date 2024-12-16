import data
import question_model
from quiz_brain import QuizBrain

imported_data = data.question_data
question_maker = question_model

question_bank = []

#Går gjennom hver spørsmål og svar
for question in imported_data:
    #Lager en ny variabel som inneholder texten fra spørsmålet og svaret
    new_question = question_model.Question(question["text"], question["answer"])
    #Lagrer det i vår bank
    question_bank.append(new_question)
    

quiz = QuizBrain(question_bank)
counter = 0
while quiz.still_has_questions:
    counter += 1
    #Måtte gjøre dette med counteren for ellers så går spillet for langt
    if counter == len(quiz.question_list) + 1:
        break 
    quiz.next_question()

print(f"You have completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}")