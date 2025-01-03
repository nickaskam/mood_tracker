from question import Question
from questions_list import Question_List

if __name__ == '__main__':
    question1_text = "What is your mood?"
    question1 = Question(question1_text)

    question2_text = "Do you feel accomplished today?"
    question2 = Question(question2_text)

    question_list = [question1, question2]
    new_question_list = Question_List(question_list)

    print("Questions Asked:")
    new_question_list.print_questions()
    print("Specific Question:")
    print(new_question_list.return_one_question(1))