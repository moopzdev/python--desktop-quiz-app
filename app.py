# main app
from question import Question
from data import question_data
from controller import Controller
from ui import UserInterface

# New Questions
all_questions = []

for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = Question(text, answer)
    all_questions.append(question)

controller = Controller(all_questions)

userInterface = UserInterface(controller)
