from flake8_class_newline import new_line_checker
from unittest import TestCase


class TestChecks(TestCase):
    def test_checks_class_new_lines(self):
        errors = []
        expected_errors = [
            None,
            (0, 'CNL100: Class definition does not have a new line.'),
            None,
            None,
            None,
            None,
            None
        ]

        lines = [
            'class ClassWithoutANewLine(object):',
            'aaasome_arg = "a_string"',
            '',
            '',
            'class ClassWithNewLine(object):',
            '   ',
            'some_arg = "a_string"'
        ]

        for line_number, line in enumerate(lines):
            errors.append(
                new_line_checker(
                    physical_line=line, line_number=line_number
                )
            )

        self.assertEqual(expected_errors, errors)
