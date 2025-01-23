if __name__ == "__main__":
    from response import Response
else:
    from response_package.response import Response

import csv

class ResponseReceived:
    def __init__(self):
        pass

if __name__ == "__main__":
    response_text = "5 - High"
    response_test = Response("45", response_text, user_id="1")
    response_id_text = str(response_test.return_response_id()) + '\n'
    print("Response ID:", response_id_text)

    print("sending response to csv...")
    f = open('responses.csv', "w")
    f.write(response_id_text)
    f.close()