from flake8_class_newline import new_line_checker
from unittest import TestCase


class TestChecks(TestCase):

    def check_file(self, lines, filename):
        errors = []
        for line_number, line in enumerate(lines):
            errors.append(
                list(
                    new_line_checker(
                        logical_line=line,
                        line_number=line_number + 1,
                        filename=filename
                    )
                )
            )

        return errors

    def test_checks_class_new_lines(self):
        expected_errors = [
            [],
            [((2, 0), 'CNL100 Class definition does not have a new line.')],
            [],
            [],
            [],
            [],
            [],
            [((8, 0), 'CNL100 Class definition does not have a new line.')],
            [],
            [],
            [],
        ]

        an_error_file = [
            'class ClassWithoutANewLineDecorator(object):',
            '   @property',
            '   def aaasome_arg(self):',
            '      return "a_string"',
            '',
            '',
            'class ClassWithoutANewLineMethod(object):',
            '   def aaasome_arg(self):',
            '      return "a_string"',
            '',
            '',
        ]
        # This should produce no error.
        no_error_file = [
            'class ClassWithANewLineDecorator(object):',
            '',
            '   @property',
            '   def aaasome_arg(self):',
            '      return "a_string"',
            '',
            '',
            'class ClassWithANewLineMethod(object):',
            '',
            '   def aaasome_arg(self):',
            '      return "a_string"',
            '',
            '',
            'class ClassWithoutANewLineArgument(object):',
            '   an_arg = "a_value"',
            '',
            '',
            'class ClassWithoutANewLineArgument(object):',
            '   definetly_an_argument = "a_value"',
            '',
            '',
            'class ClassWithMultipleBases(AClassWithNewLine,'
            '                             ClassWithDoubleDocstring,'
            '                             object):',  # The same logical line
            "   ''' A docstring '''",
            '   some_arg = "a_string"',
            '',
            '',
            'class ClassWithDoubleDocstringShouldBeIgnored(object):',
            '""" A docstring """',
            '   some_arg = "a_string"',
            '',
            '',
            'class ClassWithSingleDocstringShouldBeIgnored(object):',
            "   ''' A docstring '''",
            '   some_arg = "a_string"',
            '',
            '',
            'class ClassWithClassMetaobject):',
            "   class Meta:",
            '      an_arg = "a_value"',
            '',
            '',
        ]

        an_error_file_errors = self.check_file(an_error_file, 'a_file')
        no_error_file_errors = self.check_file(no_error_file, 'another_file')

        self.assertEqual(expected_errors, an_error_file_errors)
        self.assertEqual(
            [[] for _ in no_error_file_errors], no_error_file_errors
        )
