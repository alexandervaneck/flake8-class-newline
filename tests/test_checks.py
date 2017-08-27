from flake8_class_newline import new_line_checker
from unittest import TestCase


class TestChecks(TestCase):
    def check_file(self, lines, filename):
        errors = []
        for line_number, line in enumerate(lines):
            errors.append(
                new_line_checker(
                    physical_line=line,
                    line_number=line_number + 1,
                    filename=filename
                )
            )

        return errors

    def test_checks_class_new_lines(self):
        expected_errors = [
            None,
            (0, 'CNL100: Class definition does not have a new line.'),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ]

        a_file = [
            'class ClassWithoutANewLine(object):',
            'aaasome_arg = "a_string"',
            '',
            '',
            'class ClassWithNewLine(object):',
            '   ',
            'some_arg = "a_string"',
            'class ClassWithDoubleDocstringShouldBeIgnored(object):',
            '""" A docstring """',
            'some_arg = "a_string"',
            'class ClassWithSingleDocstringShouldBeIgnored(object):',
            "''' A docstring '''",
            'some_arg = "a_string"',

        ]
        # This should produce no error.
        # the error line of file 1 should not be propagated to file 2.
        another_file = [
            'class ClassWithoutANewLine(object):',
            '',
            'aaasome_arg = "a_string"',
        ]

        a_file_errors = self.check_file(a_file, 'a_file')
        another_file_errors = self.check_file(another_file, 'another_file')

        self.assertEqual(expected_errors, a_file_errors)
        self.assertEqual([None, None, None], another_file_errors)
