import uuid

class Question:
    """
    The structure for the daily question that the mood tracker will give the user
    inputs: question to be answered
    """
    def __init__(self, question_text: str, question_frequency: str = 'undefined'):
        self.question_id = str(uuid.uuid4())
        self.question_text = question_text
        self.question_frequency = self.clean_frequency_name(question_frequency)

    def return_question_id(self):
        return self.question_id

    def return_question_text(self):
        return self.question_text
    
    def change_question_text(self, new_question_text: str):
        self.question_text = new_question_text
    
    def clean_frequency_name(self, question_frequency: str):
        if question_frequency.lower() == 'daily':
            return "Daily"
        elif question_frequency.lower() == 'weekly':
            return "Weekly"
        elif question_frequency.lower() == 'monthly':
            return "Monthly"
        else:
            return "Undefined"
    
    def return_question_frequency(self):
        return self.question_frequency
    
    def change_question_frequency(self, new_question_frequency: str):
        self.question_frequency = self.clean_frequency_name(new_question_frequency)
    
if __name__ == '__main__':
    question_to_ask = 'How are you?'
    frequency = 'daily'
    new_question = Question(question_to_ask, question_frequency=frequency)
    print(new_question.return_question_text())

    new_question_text = "Do you feel accomplished?"
    new_question.change_question_text(new_question_text)
    print("Updated Question: ", new_question.return_question_text())

    print("Question ID: ", new_question.return_question_id())

    print("Question Frequency: ", new_question.return_question_frequency())

    new_frequency = 'MoNtHly'
    new_question.change_question_frequency(new_frequency)
    print("New Question Frequency: ", new_question.return_question_frequency())