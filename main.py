from question import Question

if __name__ == '__main__':
    question_to_ask = 'How are you?'
    new_question = Question(question_to_ask)
    print(new_question.return_question_text())

    new_question_text = "Do you feel accomplished?"
    new_question.change_question_text(new_question_text)
    print("Updated Question: ", new_question.return_question_text())