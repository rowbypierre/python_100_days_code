from question import Question
from data import question_data
from quiz import Quiz

qnas = [Question(pairs["question"], pairs["answer"]) for pairs in question_data]

quiz = Quiz(qnas)
while quiz.questions_remain():
    quiz.next_question()
    quiz.is_quiz_complete()
