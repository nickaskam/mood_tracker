from question_package import Question
from response_package import Response
from user_package import User

class Response_Validator:
    def __init__(self, question: Question, response: Response, user: User):
        self.question = question
        self.response = response
        self.valid_response = self.check_valid_response(question, response, user)

    def check_valid_response(self, question: Question, response: Response, user: User):
        valid_question_id = self.check_valid_ids_question_resopnse(question, response)
        valid_user_id = self.check_valid_ids_user_response(user, response)

        if not valid_question_id or not valid_user_id:
            return False
        
        else:
            return True

    def check_valid_ids_question_resopnse(self, question: Question, response: Response):
        response_question_id = response.return_question_id()
        question_id = question.return_question_id()
        
        try: 
            if response_question_id == question_id:
                return True

        except:
            print("Question ID and response Question ID do not match")
        
        return False
    
    def check_valid_ids_user_response(self, user: User, response: Response):
        response_user_id = response.return_user_id()
        user_id = user.return_user_id()

        try:
            if response_user_id == user_id:
                return True
            
        except:
            print("User ID and response user ID do not match")
        
        return False
    
    def return_valid_response(self):
        return self.valid_response

if __name__ == "__main__":
    new_question_text = "hello, how are you?"
    new_question_frequency = "monthly"
    new_question = Question(new_question_text, new_question_frequency)

    new_user = User("nick", "a", "nicka@gmail.com")

    new_response_text = "okay"
    new_response = Response(
                            new_question.return_question_id(), 
                            new_question_text, 
                            new_user.return_user_id()
                            )

    wrong_question = Question("is this the right question?")
    wrong_user = User("nick", "b", "nickb@gmail.com")
    check_valid_response = Response_Validator(new_question, new_response, new_user)
    print("Was this a valid response?", check_valid_response.return_valid_response())

    check_valid_response = Response_Validator(wrong_question, new_response, new_user)
    print("Was this a valid response with wrong question?", check_valid_response.return_valid_response())

    check_valid_response = Response_Validator(new_question, new_response, wrong_user)
    print("Was this a valid response with wrong user?", check_valid_response.return_valid_response())
