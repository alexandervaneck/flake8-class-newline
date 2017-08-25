from flake8_class_newline import ClassNewLineChecker
import os
from unittest import TestCase


class TestChecks(TestCase):
    def test_checks_class_new_lines(self):
        checker = ClassNewLineChecker(
            None,
            filename=get_absolute_path('data/classes.py')
        )
        self.assertEqual(
            [(
                1,
                0,
                'Q000: Class definition does not have a new line.',
                type(checker)
            )],
            list(checker.run())
        )


def get_absolute_path(filepath):
    return os.path.join(os.path.dirname(__file__), filepath)
