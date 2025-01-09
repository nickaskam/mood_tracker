if __name__ == "__main__":
    from question import Question
else:
    from question_package.question import Question

class Question_List:
    """
    putting together question(s) to keep track
    input a list of Question(s)
    """
    def __init__(self, questions: list[Question]):
        self.questions = questions

    def print_questions(self):
        index = 1
        for question in self.questions:
            print(index, '-', question.return_question_text())
            index += 1
        return
    
    def return_one_question(self, index: int):
        return self.questions[index].return_question_text()
    
    def change_question(self, index: int, updated_question_text):
        self.questions[index].change_question_text(updated_question_text)
        return
    
    def return_question_ids(self):
        question_id_list = []
        for question in self.questions:
            question_id_list.append(question.return_question_id())
        return question_id_list
    
    def return_question_text_from_uuid(self, question_uuid: str):
        for question in self.questions:
            if question.question_id == question_uuid:
                return question.question_text
        
        return "Question Not Found in Question List"
    
    def return_frequency_for_question(self, question_uuid: str):
        for question in self.questions:
            if question.question_id == question_uuid:
                return question.question_frequency
            
        return "Question Not Found in Question List"
    
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

    question2_updated_text = "Did you get a lot done today?"
    new_question_list.change_question(1, question2_updated_text)
    print("Updated question 2 text:")
    new_question_list.print_questions()

    print("What is the frequency for this question:", new_question_list.return_frequency_for_question(question1.return_question_id()))

    print("What are the IDs for the questions: ", new_question_list.return_question_ids())