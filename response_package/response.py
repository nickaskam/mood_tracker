import uuid
import datetime

class Response:
    def __init__(self, question_id: str, response_text: str, user_id: str = None):
        self.response_id = str(uuid.uuid4())
        self.response_time = datetime.datetime.now()
        self.question_id = question_id
        self.response_text = response_text
        self.user_id = user_id

    def return_response_id(self):
        return self.response_id
    
    def return_response_time(self):
        return self.response_time
    
    def return_question_id(self):
        return self.question_id
    
    def return_response_text(self):
        return self.response_text

if __name__ == '__main__':

    
    response_text = "5 - High"
    response_test = Response("45", response_text, user_id="1")
    print("Response ID:", response_test.return_response_id())
    print("Response Time:", response_test.return_response_time())
    question_id_in_response = response_test.return_question_id()
    print("Response Question ID:", question_id_in_response)
    print("Response Text:", response_test.return_response_text())