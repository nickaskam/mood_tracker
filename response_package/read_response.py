import csv
from datetime import datetime

CSV_LOCATION = '/Users/nickaskam/Documents/2025/mood_tracker/responses.csv'

# For testing only, look for response regardless of what the user requested
response_requested = '8968a4bb-b00f-4417-82d2-6a80ce5fe0e2'

class Read_Response:
    def __init__(self, csv_file_location):
        self.csv_file_location = csv_file_location
        self.response_tracked = dict()

    def read_response(self, response_requested):
        print("\nReading Response:")
        with open('/Users/nickaskam/Documents/2025/mood_tracker/responses.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row[0] == response_requested:
                    print("Response Found!")

                    self.response_tracked = {
                        "responseId" : row[0],
                        "responseTime" : row[1],
                        "questionId" : row[2],
                        "responseText" : row[3],
                        "userId" : row[4]
                        }

    def print_response(self):
        print("Response ID: ", self.response_tracked["responseId"])
        print("Response Time: ", self.response_tracked["responseTime"])
        print("Question ID: ", self.response_tracked["questionId"])
        print("Reponse Text: ", self.response_tracked["responseText"])
        print("User ID: ", self.response_tracked["userId"])
        
    def getDayOfResponse(self):
        format_string = " %Y-%m-%d %H:%M:%S.%f"
        datetime_object = datetime.strptime(self.response_tracked["responseTime"], format_string)
        print("the Day of the week is: " + datetime_object.strftime("%A"))


if __name__ == "__main__":
    # use a response ID in csv
    response_requested = '8968a4bb-b00f-4417-82d2-6a80ce5fe0e2'

    new_reader = Read_Response(CSV_LOCATION)
    new_reader.read_response(response_requested)
    new_reader.print_response()

    new_reader.getDayOfResponse()
