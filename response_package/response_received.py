
from response_package import Response
from user_package import User
from question_package import Question

CSV_LOCATION = '/Users/nickaskam/Documents/2025/mood_tracker/responses.csv'

class Response_Received:
    def __init__(self, response: Response):
        self.response = response
        self.input_response_into_csv()

    def input_response_into_csv(self):
        response_test_id = self.response.return_response_id()
        response_dictionary1 = self.response.return_response_dictionary()
        response_time1 = str(response_dictionary1[response_test_id]["response_time"])
        question_id1 = response_dictionary1[response_test_id]["question_id"]
        response_text1 = response_dictionary1[response_test_id]["response_text"]
        user_id1 = response_dictionary1[response_test_id]["user_id"]
    
        end_character = '\n'
        new_line = response_test_id + ", " + response_time1 + ", " + question_id1 \
                + ", " + response_text1 + ", " + user_id1 + end_character

        print("sending response to csv...")
        f = open(CSV_LOCATION, "a", newline='')
        f.write(new_line)
        print("done")
        f.close()


if __name__ == "__main__":
    goal_text = "to improve"
    user_1 = User("Nick", "A", "nick@a.com", goal_text)
    
    user1_id = user_1.return_user_id()
    # print(user1_id)

    dummy_user_id = user1_id

    question_to_ask = 'How are you?'
    frequency = 'daily'
    new_question = Question(question_to_ask, question_frequency=frequency)
    # print(new_question.return_question_id())

    dummy_question_id = new_question.return_question_id()
    response_text = "5 - High"

    response_test = Response(
                                dummy_question_id, 
                                response_text, 
                                user_id=dummy_user_id
                            )

    print("inputting response into CSV")
    new_response_received = Response_Received(response_test)