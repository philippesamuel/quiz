import click

from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question] | None = None) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = [] if question_list is None else question_list

    @property
    def number_of_questions(self) -> int:
        return len(self.question_list)

    def still_has_questions(self) -> bool:
        return self.question_number < self.number_of_questions

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        formatted_question = f"Q.{self.question_number}: {current_question.text} (True/False)?"
        user_answer = click.prompt(formatted_question, type=click.BOOL)
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: bool, correct_answer: bool) -> None:
        if user_answer == correct_answer:
            click.echo("You got it right!")
            self.score += 1
        else:
            click.echo("That's wrong.")
        click.echo(f"The correct answer was {correct_answer}.")
        click.echo(f"Your current score is: {self.score}/{self.question_number}")
        click.echo()  # new line


def main():
    question_list = [
        Question(text="Are you sure.", answer=True),
        Question(text="Really.", answer=False)
    ]
    quiz_brain = QuizBrain(question_list=question_list)
    quiz_brain.next_question()
    quiz_brain.next_question()
    quiz_brain.next_question()


if __name__ == '__main__':
    main()
