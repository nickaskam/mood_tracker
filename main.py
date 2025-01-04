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

    question2_updated_text = "Did you get a lot done today?"
    new_question_list.change_question(1, question2_updated_text)
    print("Updated question 2 text:")
    new_question_list.print_questions()

    print("What are the IDs for the questions: ", new_question_list.return_question_ids())