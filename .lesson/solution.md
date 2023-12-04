# Solution

## Objective decomposition

Task decomposition has been already applied with the "Instructions".

- Gather the user's name
- Load questions for the file
- For each question
  - Display the question to the user
  - Collect the answer from the user
  - Check collected answer against the correct one
- Display the quiz score to the user
- Write a score record to the "scores.txt" file

## Solution implementation

```python
import csv
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

    username: str = ""
    while not username or len(username) > 10:
        username = input("Enter username: ")

    return username


def load_questions_from_csv(source: Union[str, Path]) -> Questions:
    """
    Load quiz data from the given source file

    :param source: path for the source file
    :type source: str | :class: `pathlib.Path`

    :return: quiz data
    :rtype: list

    """

    with open(source) as io_buff:
        csv_reader = csv.DictReader(io_buff, ["question", "options", "answer"])
        questions = map(
            lambda q: {**q, "options": q["options"].split(",")}, csv_reader
        )

        # noinspection PyTypeChecker
        return [question for question in questions]


def write_score_to_file(name: str, score: int) -> None:
    """
    Write user data to file

    :param name: user's name
    :type name: str
    :param score: gained score
    :type score: int

    """

    with open("scores.txt", "a") as io_buff:
        io_buff.write(f"{name:<12}{score}\n")


def display_question(question: Question) -> None:
    """
    Display a question to the user

    :param question: a question dictionary
    :type question: dict

    """

    # print empty line before and after the question text
    print("\n%s" % question["question"], end="\n\n")

    # print out the answer options with their numbers
    for opt_number, opt_value in enumerate(question["options"], 1):
        print(opt_number, opt_value)


def gather_answer(question: Question) -> int:
    """
    Collect a question answer from the user

    :param question: a question dictionary
    :type question: dict

    :return: the answer option number
    :rtype: int

    """

    user_choice: int = -1
    option_size: int = len(question["options"])

    while user_choice not in range(option_size):
        user_choice = int(input("Submit answer: ")) - 1

    return user_choice


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

    return question["answer"] == question["options"][option_idx]


def perform_quiz(questions: Questions) -> int:
    """
    Perform quiz and evaluate the user's response

    :param questions: a list of question dictionaries
    :type questions: list

    :return: the number of questions answered correctly
    :rtype: int

    """

    user_score: int = 0

    for question in questions:
        display_question(question)
        user_answer = gather_answer(question)
        user_score += is_correct(question, user_answer)

    return user_score


def main() -> None:
    """
    Run quiz script

    """

    name = gather_username()
    questions = load_questions_from_csv("questions.csv")
    score = perform_quiz(questions)
    write_score_to_file(name, score)
    print("\nQuiz score: %d\n" % score)


if __name__ == "__main__":
    main()
```
