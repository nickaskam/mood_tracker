if __name__ == "__main__":
    from response import Response
else:
    from response_package.response import Response

class ResponseReceived:
    def __init__(self):
        pass

if __name__ == "__main__":
    dummy_user_id = "61b457e8-5b25-4cf1-9283-3d89fe794743"
    dummy_question_id = "53edce4c-3682-4b27-906b-371b9e0fd241"
    response_text = "5 - High"

    response_test = Response(
                                dummy_question_id, 
                                response_text, 
                                user_id=dummy_user_id
                            )

    response_test_id = response_test.return_response_id()
    response_dictionary1 = response_test.return_response_dictionary()
    response_time1 = str(response_dictionary1[response_test_id]["response_time"])
    question_id1 = response_dictionary1[response_test_id]["question_id"]
    response_text1 = response_dictionary1[response_test_id]["response_text"]
    user_id1 = response_dictionary1[response_test_id]["user_id"]
    
    # print("Response ID:", response_id_text)
    end_character = '\n'
    new_line = response_test_id + ", " + response_time1 + ", " + question_id1 \
                + ", " + response_text1 + ", " + user_id1 + end_character
    # print(new_line)

    print("sending response to csv...")
    f = open('/Users/nickaskam/Documents/2025/mood_tracker/responses.csv', "a", newline='')
    f.write(new_line)
    print("done")
    f.close()