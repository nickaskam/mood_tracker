from question_package import Question, Question_List
from response_package import Response, Response_Received, Read_Response, Response_Validator
from user_package import User

CSV_LOCATION = '/Users/nickaskam/Documents/2025/mood_tracker/responses.csv'

if __name__ == '__main__':
    #question1_text = input("What is your question? ")
    question1_text = "How do you feel?"
    frequency_question = "What would you like the frequency to be? Monthly, Weekly or Daily? "
    question1_frequency = "daily"
    question1 = Question(question1_text, question1_frequency)

    question2_text = "Do you feel accomplished?"
    question2_frequency = "Monthly"
    question2 = Question(question2_text, question2_frequency)

    question_list1 = [question1, question2]
    new_question_list1 = Question_List(question_list1)

    print("question list")
    new_question_list1.print_questions()
    
    user_1 = User("Nick", "A", "nick@a.com")
    
    response_text = "5 - High"
    response_test = Response(question1.return_question_id(), response_text, user_id=user_1.return_user_id())
    
    print("checking to see if valid response")
    # give valid test response
    was_response_valid = Response_Validator(new_question_list1.return_one_question(0), response_test, user_1)
    print("was this valid?", was_response_valid.return_valid_response())
    
    response_test_id = response_test.return_response_id()
    response_test_dict = response_test.return_response_dictionary()
    
    print("Response ID:", response_test.return_response_id())
    print("Response Time:", response_test.return_response_time())
    question_id_in_response = response_test.return_question_id()
    print("Response Question ID:", question_id_in_response)
    print("Response Text:", response_test_dict[response_test_id]["response_text"])

    print("inputting response into CSV...")
    new_response_received = Response_Received(response_test)

    retrieved_question_text = new_question_list1.return_question_text_from_uuid(question_id_in_response)
    print("Question Text:", retrieved_question_text)

    # For testing only, look for response regardless of what the user requested
    response_requested = '8968a4bb-b00f-4417-82d2-6a80ce5fe0e2'

    new_reader = Read_Response(CSV_LOCATION)
    new_reader.read_response(response_requested)
    new_reader.print_response()