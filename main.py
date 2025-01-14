from question_package import Question, Question_List
from response_package import Response
from user_package import User

if __name__ == '__main__':
    question1_text = "What is your mood today?"
    question1_frequency = "Monthly"
    question1 = Question(question1_text, question1_frequency)

    question2_text = "Do you feel accomplished?"
    question2_frequency = "dailY"
    question2 = Question(question2_text, question2_frequency)

    question_list1 = [question1, question2]
    new_question_list1 = Question_List(question_list1)

    print("question list")
    new_question_list1.print_questions()
    
    user_1 = User("Nick", "A", "nick@a.com")
    
    response_text = "5 - High"
    response_test = Response(question1.return_question_id(), response_text, user_id=user_1.return_user_id())
    # need to add response validator here
    
    response_test_id = response_test.return_response_id()
    response_test_dict = response_test.return_response_dictionary()
    
    print("Response ID:", response_test.return_response_id())
    print("Response Time:", response_test.return_response_time())
    question_id_in_response = response_test.return_question_id()
    print("Response Question ID:", question_id_in_response)
    print("Response Text:", response_test_dict[response_test_id]["response_text"])

    retrieved_question_text = new_question_list1.return_question_text_from_uuid(question_id_in_response)
    print("Question Text:", retrieved_question_text)

    print("test")
    # new branch to test