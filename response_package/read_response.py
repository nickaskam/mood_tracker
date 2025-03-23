import csv

response_requested = input("Enter a response ID that you want: ")

# For testing only, look for response regardless of what the user requested
response_requested = '8968a4bb-b00f-4417-82d2-6a80ce5fe0e2'

with open('/Users/nickaskam/Documents/2025/mood_tracker/responses.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if row[0] == response_requested:
            print("\nResponse ID: ", row[0])
            print("Response Time: ", row[1])
            print("Question ID: ", row[2])
            print("Reponse Text: ", row[3])
            print("User ID: ", row[4])