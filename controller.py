class Controller:
    def __init__(self, data):
        self.question_list = data
        self.question_number = 0
        self.score = 0
        self.current = None

    def nextQuestion(self):
        self.current = self.question_list[self.question_number]
        self.question_number += 1
        # print("Question", self.question_number, ":", current.text, "?")
        # user_answer = input("Inputted Answer:")
        # print(user_answer)
        # self.checkAnswer(user_answer, current.answer)
        return f"{self.question_number} ) {self.current.text}"

    def hasQuestion(self):
        return self.question_number < len(self.question_list)

    def checkAnswer(self, userInput):
        correct_answer = self.current.answer
        if(userInput.lower() == correct_answer.lower()):
            self.score += 1
            print("Current Score:", self.score)
        else:
            print("Wrong Answer")
            print("The correct answer is", correct_answer)
