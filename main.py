"""
Quiz Assignment

"""

from pathlib import Path
from typing import List, TypedDict, Union

# user defined type alias
Question = TypedDict("Question", {
    "question": str,
    "options": List[str],
    "answer": str,
})
Questions = List[Question]


def gather_username() -> str:
    """
    Gather the name from the user

    :return: the name user has entered
    :rtype: str

    """


def load_questions_from_csv(source: Union[str, Path]) -> Questions:
    """
    Load quiz data from the given source file

    :param source: path for the source file
    :type source: str | :class: `pathlib.Path`

    :return: quiz data
    :rtype: list

    """


def write_score_to_file(name: str, score: int) -> None:
    """
    Write user data to file

    :param name: user's name
    :type name: str
    :param score: gained score
    :type score: int

    """


def display_question(question: Question) -> None:
    """
    Display a question to the user

    :param question: a question dictionary
    :type question: dict

    """


def gather_answer(question: Question) -> int:
    """
    Collect a question answer from the user

    :param question: a question dictionary
    :type question: dict

    :return: the answer option number
    :rtype: int

    """


def is_correct(question: Question, option_idx: int) -> bool:
    """
    Check if the given answer option is correct for the question

    :param question: a question dictionary
    :type question: dict
    :param option_idx: the answer option number starting from 1
    :type option_idx: int

    :return: check result
    :rtype: bool

    """


def perform_quiz(questions: Questions) -> int:
    """
    Perform quiz and evaluate the user's response

    :param questions: a list of question dictionaries
    :type questions: list

    :return: the number of questions answered correctly
    :rtype: int

    """


def main() -> None:
    """
    Run quiz script

    """


if __name__ == "__main__":
    main()
