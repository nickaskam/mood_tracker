import csv

CSV_LOCATION = '/Users/nickaskam/Documents/2025/mood_tracker/responses.csv'

# For testing only, look for response regardless of what the user requested
response_requested = '8968a4bb-b00f-4417-82d2-6a80ce5fe0e2'

class Read_Response:
    def __init__(self, csv_file_location):
        self.csv_file_location = csv_file_location

    def read_response(self, response_requested):
        print("\nReading Response:")
        with open('/Users/nickaskam/Documents/2025/mood_tracker/responses.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row[0] == response_requested:
                    print("Response ID: ", row[0])
                    print("Response Time: ", row[1])
                    print("Question ID: ", row[2])
                    print("Reponse Text: ", row[3])
                    print("User ID: ", row[4])


if __name__ == "__main__":
    # use a response ID in csv
    response_requested = '8968a4bb-b00f-4417-82d2-6a80ce5fe0e2'

    new_reader = Read_Response(CSV_LOCATION)
    new_reader.read_response(response_requested)
