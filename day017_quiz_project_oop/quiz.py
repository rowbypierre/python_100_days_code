class Quiz:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.correct_answers = 0

    def more_questions_remain(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False)?\n> ")
        self.answer_check(user_answer, current_question.answer)

    def answer_check(self, user_answer, correct_answer):
        evaluation = user_answer.lower() == correct_answer.lower()
        if evaluation:
            self.correct_answers += 1
            print("!!!Correct!!!")
        else:
            print("!!!Incorrect!!!")

        print(f"Answer:\t\t{correct_answer.capitalize()}"
              f"\nCorrect:\t{self.correct_answers}\\{self.question_number}"
              f"\n")

    def is_quiz_complete(self):
        if self.question_number == len(self.questions_list):
            print("Quiz completed."
                  f"\nFinal score:\t{self.correct_answers}\\{self.question_number}")
