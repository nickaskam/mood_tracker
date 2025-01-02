
class Question:
    def __init__(self, question_text: str):
        self.question_text = question_text

    def return_question_text(self):
        return self.question_text
    
    def change_question_text(self, new_question_text: str):
        self.question_text = new_question_text
    
if __name__ == '__main__':
    question_to_ask = 'How are you?'
    new_question = Question(question_to_ask)
    print(new_question.return_question_text())

    new_question_text = "Do you feel accomplished?"
    new_question.change_question_text(new_question_text)
    print("Updated Question: ", new_question.return_question_text())