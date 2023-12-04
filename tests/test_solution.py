import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import Mock, mock_open, patch

from main import (display_question, gather_answer, gather_username, is_correct,
                  load_questions_from_csv, main, perform_quiz,
                  write_score_to_file)


class TestSolution(unittest.TestCase):

    @unittest.expectedFailure
    def test_gather_username(self):
        with patch("builtins.input", return_value="ABC"):
            self.assertEqual(gather_username(), "ABC")

    @unittest.expectedFailure
    def test_gather_username_validate(self):
        inputs = [
            "",
            "a" * 15,
            "a" * 14,
            "a" * 13,
            "a" * 12,
            "a" * 11,
            "a" * 10,
        ]
        with patch("builtins.input", side_effect=inputs) as mock_input:
            gather_username()
            self.assertEqual(mock_input.call_count, len(inputs))

    @unittest.expectedFailure
    def test_write_scores(self):
        mock_file = mock_open()
        with patch("builtins.open", mock_file):
            write_score_to_file("abc", 10)
        handler = mock_file()
        handler.write.assert_called_once_with(f"abc         10\n")

    @unittest.expectedFailure
    def test_write_scores_append(self):
        mock_file = mock_open()
        with patch("builtins.open", mock_file):
            write_score_to_file("abc", 20)
            mock_file.assert_called_once_with("scores.txt", "a")

    @unittest.expectedFailure
    def test_load_questions(self):
        raw_data = (
            """Question no 1.,"option 1,option 2,option 3",option 2\n"""
            """Question no 2.,"option 1,option 2,option 3",option 1\n"""
            """Question no 3.,"option 1,option 2,option 3",option 3\n"""
        )
        questions_data = mock_open(read_data=raw_data)

        with patch("builtins.open", questions_data):
            questions = load_questions_from_csv("testing_file")

        expected = [
            {
                "question": "Question no 1.",
                "options": ["option 1", "option 2", "option 3"],
                "answer": "option 2"
            },
            {
                "question": "Question no 2.",
                "options": ["option 1", "option 2", "option 3"],
                "answer": "option 1"
            },
            {
                "question": "Question no 3.",
                "options": ["option 1", "option 2", "option 3"],
                "answer": "option 3"
            },
        ]

        self.assertListEqual(questions, expected)

    @unittest.expectedFailure
    def test_display_question(self):
        question = {
            "question": "What is the capital of Ukraine?",
            "options": ["Kharkiv", "Vinnytsia", "Kyiv", "Poltava"],
            "answer": "Kyiv",
        }

        with StringIO() as io_buff, redirect_stdout(io_buff):
            display_question(question)
            stdout = io_buff.getvalue()

        pattern = (
            r"\sWhat is the capital of Ukraine\?\s{2}"
            r"1\s+Kharkiv\s"
            r"2\s+Vinnytsia\s"
            r"3\s+Kyiv\s"
            r"4\s+Poltava\s"
        )
        self.assertRegex(stdout, pattern)

    # noinspection PyTypeChecker
    @unittest.expectedFailure
    def test_gather_answer(self):
        question = {
            "options": ["option 1", "option 2", "option 3", "option 4"]
        }
        with patch("builtins.input", return_value="3"):
            self.assertEqual(gather_answer(question), 2)

    # noinspection PyTypeChecker
    @unittest.expectedFailure
    def test_gather_answers_repeat(self):
        with patch("builtins.input", side_effect=["-1", "0", "1"]) \
             as mock_input:
            gather_answer({"options": ["option 1"]})
            self.assertEqual(mock_input.call_count, 3)

        with patch("builtins.input", side_effect=["5", "3", "2"]) \
             as mock_input:
            gather_answer({"options": ["option 1", "option 2"]})
            self.assertEqual(mock_input.call_count, 3)

        with patch("builtins.input", side_effect=["1"]) as mock_input:
            gather_answer({"options": ["option 1", "option 2"]})
            self.assertEqual(mock_input.call_count, 1)

    # noinspection PyTypeChecker
    @unittest.expectedFailure
    def test_gather_answer_message(self):
        with patch("builtins.input", return_value="1") as mock_input:
            gather_answer({"options": ["option 1"]})
            mock_input.assert_called_with("Submit answer: ")

    # noinspection PyTypeChecker
    @unittest.expectedFailure
    def test_is_correct(self):
        self.assertTrue(is_correct(
            dict(answer="option 1", options=["option 1", "option 2"]), 0
        ))
        self.assertTrue(is_correct(
            dict(answer="option 2", options=["option 1", "option 2"]), 1
        ))
        self.assertTrue(is_correct(
            dict(answer="option 2", options=["option 2", "option 1"]), 0
        ))

    # noinspection PyTypeChecker
    @unittest.expectedFailure
    def test_not_is_correct(self):
        answer_check = is_correct(
            dict(answer="option 1", options=["option 1", "option 2"]), 1
        )
        self.assertFalse(answer_check)
        self.assertIsNotNone(answer_check)
        answer_check = is_correct(
            dict(answer="option 2", options=["option 1", "option 2"]), 0
        )
        self.assertFalse(answer_check)
        self.assertIsNotNone(answer_check)
        answer_check = is_correct(
            dict(answer="option 2", options=["option 2", "option 1"]), 1
        )
        self.assertFalse(answer_check)
        self.assertIsNotNone(answer_check)

    @unittest.expectedFailure
    def test_quiz_score(self):
        questions = [
            {
                "question": "Question no 1.",
                "options": ["option 1", "option 2", "option 3"],
                "answer": "option 2"
            },
            {
                "question": "Question no 2.",
                "options": ["option 1", "option 2", "option 3"],
                "answer": "option 1"
            },
            {
                "question": "Question no 3.",
                "options": ["option 1", "option 2", "option 3"],
                "answer": "option 3"
            },
        ]

        with patch("builtins.input") as mock_input, \
             patch("main.display_question"):
            mock_input.return_value = "1"
            self.assertEqual(perform_quiz(questions), 1)
            mock_input.return_value = "2"
            self.assertEqual(perform_quiz(questions), 1)
            mock_input.return_value = "3"
            self.assertEqual(perform_quiz(questions), 1)

        with patch("builtins.input") as mock_input, \
             patch("main.display_question"):
            mock_input.side_effect = ["2", "1", "3"]
            self.assertEqual(perform_quiz(questions), 3)
            mock_input.side_effect = ["1", "3", "3"]
            self.assertEqual(perform_quiz(questions), 1)
            mock_input.side_effect = ["3", "1", "3"]
            self.assertEqual(perform_quiz(questions), 2)

    @unittest.expectedFailure
    def test_quiz_display_each_question(self):
        question = {"question": "Q", "options": ["o1", "o2"], "answer": "A"}
        number_of_questions = 15
        question_generator = (question for _ in range(number_of_questions))
        mock_questions = Mock()
        mock_questions.__iter__ = Mock(return_value=question_generator)

        with patch("main.display_question") as mock, \
             patch("main.gather_answer"), \
             patch("main.is_correct"):
            perform_quiz(mock_questions)
            self.assertEqual(mock.call_count, number_of_questions)
            mock.assert_called_with(question)

    @unittest.expectedFailure
    def test_quiz_gather_answer_each_question(self):
        question = {"question": "Q", "options": ["o1", "o2"], "answer": "A"}
        number_of_questions = 10
        question_generator = (question for _ in range(number_of_questions))
        mock_questions = Mock()
        mock_questions.__iter__ = Mock(return_value=question_generator)

        with patch("main.display_question"), \
             patch("main.gather_answer") as mock, \
             patch("main.is_correct"):
            perform_quiz(mock_questions)
            self.assertEqual(mock.call_count, number_of_questions)
            mock.assert_called_with(question)

    @unittest.expectedFailure
    def test_quiz_check_correct_each_question(self):
        question = {"question": "Q", "options": ["o1", "o2"], "answer": "A"}
        number_of_questions = 12
        question_generator = (question for _ in range(number_of_questions))
        mock_questions = Mock()
        mock_questions.__iter__ = Mock(return_value=question_generator)

        with patch("main.display_question"), \
             patch("main.gather_answer", return_value="answer"), \
             patch("main.is_correct") as mock:
            perform_quiz(mock_questions)
            self.assertEqual(mock.call_count, number_of_questions)
            mock.assert_called_with(question, "answer")

    @unittest.expectedFailure
    def test_quiz_functions_called_once(self):
        with patch("main.gather_username") as func_get_username, \
             patch("main.perform_quiz") as func_get_score, \
             patch("main.write_score_to_file") as func_write_score:
            main()
            func_get_username.assert_called_once()
            func_get_score.assert_called_once()
            func_write_score.assert_called_once()

    @unittest.expectedFailure
    @patch("main.gather_username")
    @patch("main.write_score_to_file")
    @patch("main.perform_quiz", return_value=10)
    def test_main_displays_score(self, *args):
        with StringIO() as io_buff, redirect_stdout(io_buff):
            main()
            stdout = io_buff.getvalue()

        pattern = r"\nQuiz score:\s+10\n"
        self.assertRegex(stdout, pattern)
