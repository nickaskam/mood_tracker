import uuid
import datetime
from question import Question
from questions_list import Question_List

class Response:
    def __init__(self, question_id: str, response_text: str):
        self.response_id = str(uuid.uuid4())
        self.response_time = datetime.datetime.now()
        self.question_id = question_id
        self.response_text = response_text

    def return_response_id(self):
        return self.response_id
    
    def return_response_time(self):
        return self.response_time
    
    def return_question_id(self):
        return self.question_id
    
    def return_response_text(self):
        return self.response_text

if __name__ == '__main__':
    question_text = "What is your mood today?"
    question = Question(question_text)

    question_list = [question]
    new_question_list = Question_List(question_list)
    
    response_text = "5 - High"
    response_test = Response(question.return_question_id(), response_text)
    print("Response ID:", response_test.return_response_id())
    print("Response Time:", response_test.return_response_time())
    question_id_in_response = response_test.return_question_id()
    print("Response Question ID:", question_id_in_response)
    print("Response Text:", response_test.return_response_text())

    retrieved_question_text = new_question_list.return_question_text_from_uuid(question_id_in_response)
    print("Question Text:", retrieved_question_text)