from question.question import Question
from question.questions_list import Question_List
from response.response import Response
from user.user import User

if __name__ == '__main__':
    question_text = "What is your mood today?"
    question = Question(question_text)

    question_list = [question]
    new_question_list = Question_List(question_list)
    
    user_1 = User("Nick", "A", "nick@a.com")
    
    response_text = "5 - High"
    response_test = Response(question.return_question_id(), response_text, user_id=user_1.return_user_id())
    print("Response ID:", response_test.return_response_id())
    print("Response Time:", response_test.return_response_time())
    question_id_in_response = response_test.return_question_id()
    print("Response Question ID:", question_id_in_response)
    print("Response Text:", response_test.return_response_text())

    retrieved_question_text = new_question_list.return_question_text_from_uuid(question_id_in_response)
    print("Question Text:", retrieved_question_text)