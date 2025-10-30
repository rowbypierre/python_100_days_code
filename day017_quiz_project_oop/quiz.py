import random


class Quiz:
    def __init__(self, question_list):
        """Initialize quiz with question bank."""
        self.question_number = 0
        self.question_list = question_list
        self.correct_answers = 0
        self.quiz_length = len(self.question_list)

    def questions_remain(self):
        """Confirm (bool) if unprompted questions remain."""
        return self.question_number < self.quiz_length

    def next_question(self):
        """
        Prompt quiz taker next question.

        Prompt:
            - user_answer (str)

        Return: 
            - None
        """
        random.shuffle(self.question_list)
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.question} (True/False)?\n> "
        )
        self.answer_check(user_answer, current_question.answer)

    def answer_check(self, user_answer, correct_answer):
        """Compare two answers (str) for match. """
        evaluation = user_answer.lower() == correct_answer.lower()
        if evaluation:
            self.correct_answers += 1
            print("!!!Correct!!!")
        else:
            print("!!!Incorrect!!!")

        print(
            f"Answer:\t\t\t{correct_answer.capitalize()}"
            f"\nCorrect Answers:\t{self.correct_answers}"
            f"\nQuestions Answered:\t{self.question_number}\n"
        )

    def is_quiz_complete(self):
        """Print final score if quiz is completed (no questions remain)."""
        if not self.questions_remain():
            print(
                "Quiz completed."
                f"\nFinal score:\t{self.correct_answers}\\{self.quiz_length}"
            )
