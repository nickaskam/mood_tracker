from question_package import Question
from response_package import Response

class Response_Validator:
    def __init__(self, question: Question, response: Response):
        self.question = question
        self.response = response
        self.valid_response = self.check_valid_response(question, response)

    def check_valid_response(self, question: Question, response: Response):
        response_question_id = response.return_question_id()
        question_id = question.return_question_id()
        
        if response_question_id == question_id:
            return True
        
        return False
    
    def return_valid_response(self):
        return self.valid_response

if __name__ == "__main__":
    new_question_text = "hello, how are you?"
    new_question_frequency = "monthly"
    new_question = Question(new_question_text, new_question_frequency)

    new_response_text = "okay"
    new_response = Response(new_question.return_question_id(), new_question_text)

    check_valid_response = Response_Validator(new_question, new_response)
    print("Was this a valid response?", check_valid_response.return_valid_response())
