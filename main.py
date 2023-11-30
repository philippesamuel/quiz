import click

import data
from question_model import Question
from quiz_brain import QuizBrain


def main() -> None:
    question_bank = [Question(**q) for q in data.question_data]
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()
    click.echo("You've completed the quiz")
    click.echo(f"Your final score was: {quiz.score}/{quiz.number_of_questions}")


if __name__ == '__main__':
    main()
