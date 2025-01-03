from question import Question

class Question_List:
    """
    putting together question(s) to keep track
    input a list of Question(s)
    """
    def __init__(self, questions: list[Question]):
        self.questions = questions

    def print_questions(self):
        for question in self.questions:
            print(question.return_question_text())
        return
    
    def return_one_question(self, index):
        return self.questions[index].return_question_text()
    
if __name__ == "__main__":
    question1_text = "What is your mood?"
    question1 = Question(question1_text)

    question2_text = "Do you feel accomplished today?"
    question2 = Question(question2_text)

    question_list = [question1, question2]
    new_question_list = Question_List(question_list)

    print("Questions Asked:")
    new_question_list.print_questions()
    print("Specific Question:")
    print(new_question_list.return_one_question(1))