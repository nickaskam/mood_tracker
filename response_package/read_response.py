import csv
from datetime import datetime

CSV_LOCATION = '/Users/nickaskam/Documents/2025/mood_tracker/responses.csv'

# For testing only, look for response regardless of what the user requested
response_requested = '8968a4bb-b00f-4417-82d2-6a80ce5fe0e2'

class Read_Response:
    def __init__(self, csv_file_location):
        self.csv_file_location = csv_file_location
        self.response_tracked = dict()
        self.day_of_the_week = ""
        self.responses_from_user = list()
        self.weekdays_of_responses = list()

    def read_response(self, response_requested) -> None:
        # print("\nReading Response:")
        with open(self.csv_file_location, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row[0] == response_requested:
                    # print("Response Found!")

                    self.response_tracked = {
                        "responseId" : row[0],
                        "responseTime" : row[1],
                        "questionId" : row[2],
                        "responseText" : row[3],
                        "userId" : row[4]
                        }

    def print_response(self) -> None:
        print("Response ID: ", self.response_tracked["responseId"])
        print("Response Time: ", self.response_tracked["responseTime"])
        print("Question ID: ", self.response_tracked["questionId"])
        print("Reponse Text: ", self.response_tracked["responseText"])
        print("User ID: ", self.response_tracked["userId"])
        
    def get_day_of_response(self) -> str:
        format_string = " %Y-%m-%d %H:%M:%S.%f"
        datetime_object = datetime.strptime(self.response_tracked["responseTime"], format_string)
        self.day_of_the_week = datetime_object.strftime("%A")

        # print("the Day of the week is: " + self.day_of_the_week)

        return self.day_of_the_week
        

    def from_user_get_response_ids(self, user_id: str) -> None:
        """
        from a user ID, get all of the responses and place into list
        """
        # print("\nReading Response:")
        with open(self.csv_file_location, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row[4].replace(" ", "") == user_id:
                    self.responses_from_user.append(row[0])

    def return_responses(self, user_id: str) -> list:
        """
        return a list of all of the response ids from a user
        """
        self.from_user_get_response_ids(user_id)
        return self.responses_from_user
    
    def return_weekdays_of_responses(self, user_id: str) -> list:
        """
        from a user ID, return a list of the weekdays that they answered
        """
        responses = self.return_responses(user_id)

        for response in responses:
            self.read_response(response)
            self.weekdays_of_responses.append(self.get_day_of_response())

        return self.weekdays_of_responses



if __name__ == "__main__":
    # use a response ID in csv
    response_requested = '8968a4bb-b00f-4417-82d2-6a80ce5fe0e2'

    new_reader = Read_Response(CSV_LOCATION)
    new_reader.read_response(response_requested)
    new_reader.print_response()

    new_reader.get_day_of_response()

    print("Responses from user: \n", new_reader.return_responses("61b457e8-5b25-4cf1-9283-3d89fe794743"))
    print("Weekdays of responses from user: \n", new_reader.return_weekdays_of_responses("61b457e8-5b25-4cf1-9283-3d89fe794743"))
