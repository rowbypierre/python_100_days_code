from question import Question
from data import question_data
from quiz import Quiz

quiz_questions = []

for question in question_data:
    new_question = question["question"]
    new_question_answer = question["answer"]
    quiz_question = Question(new_question,new_question_answer)
    quiz_questions.append(quiz_question)

quiz = Quiz(quiz_questions)

while quiz.more_questions_remain():
    quiz.next_question()
    quiz.next_question()
    quiz.is_quiz_complete()
