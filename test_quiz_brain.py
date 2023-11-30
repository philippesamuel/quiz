from question_model import Question
from quiz_brain import QuizBrain


def test_next_question(monkeypatch):
    question_list = [
        Question(text="Are you sure?", answer=True),
        Question(text="Really?", answer=False)
            ]
    # mock user input
    monkeypatch.setattr('builtins.input', lambda _: "False")
    quiz_brain = QuizBrain(question_list=question_list)
    quiz_brain.next_question()
