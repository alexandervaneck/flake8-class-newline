from flake8_class_newline import ClassNewLineChecker
import os
from unittest import TestCase


class TestChecks(TestCase):
    def test_checks_class_new_lines(self):
        class Options(object):
            allow_docstrings = False

        ClassNewLineChecker.parse_options(Options)

        checker = ClassNewLineChecker(
            None,
            filename=get_absolute_path('data/classes.py')
        )

        errors = list(checker.run())
        for line_number in [1, 10, 16]:
            self.assertIn(
                (
                    line_number,
                    0,
                    'Q000: Class definition does not have a new line.',
                    type(checker)
                ),
                errors
            )

    def test_checks_class_new_lines_with_docstrings(self):
        class Options(object):
            allow_docstrings = True

        ClassNewLineChecker.parse_options(Options)

        checker = ClassNewLineChecker(
            None,
            filename=get_absolute_path('data/classes.py')
        )

        errors = list(checker.run())
        for line_number in [1]:
            self.assertIn(
                (
                    line_number,
                    0,
                    'Q000: Class definition does not have a new line.',
                    type(checker)
                ),
                errors
            )


def get_absolute_path(filepath):
    return os.path.join(os.path.dirname(__file__), filepath)
