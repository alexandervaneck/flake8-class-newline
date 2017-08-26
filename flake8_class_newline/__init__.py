import optparse
import tokenize

# Polyfill stdin loading/reading lines
# https://gitlab.com/pycqa/flake8-polyfill/blob/1.0.1/src/flake8_polyfill/stdin.py#L52-57
try:
    from flake8.engine import pep8

    stdin_get_value = pep8.stdin_get_value
    readlines = pep8.readlines
except ImportError:
    from flake8 import utils
    import pycodestyle

    stdin_get_value = utils.stdin_get_value
    readlines = pycodestyle.readlines

from flake8_class_newline.__version__ import __version__


class ClassNewLineChecker(object):
    name = __name__
    version = __version__
    message = 'Q000: Class definition does not have a new line.'

    def __init__(self, tree, filename='(none)', builtins=None):
        self.filename = filename

    @staticmethod
    def _register_opt(parser, *args, **kwargs):
        """
        Handler to register an option for both Flake8 3.x and 2.x.
        This is based on:
        https://github.com/PyCQA/flake8/blob/3.0.0b2/docs/source/plugin-development/cross-compatibility.rst#option-handling-on-flake8-2-and-3
        It only supports `parse_from_config` from the original function and it
        uses the `Option` object returned to get the string.
        """
        try:
            # Flake8 3.x registration
            parser.add_option(*args, **kwargs)
        except (optparse.OptionError, TypeError):
            # Flake8 2.x registration
            parse_from_config = kwargs.pop('parse_from_config', False)
            option = parser.add_option(*args, **kwargs)
            if parse_from_config:
                parser.config_options.append(
                    option.get_opt_string().lstrip('-'))

    @classmethod
    def add_options(cls, parser):
        cls._register_opt(
            parser, '--allow-docstrings',
            action='store_true', parse_from_config=True,
            help='If docstrings should be allowed to be on the line '
                 'directly under the class definition. (default: False)'
        )

    @classmethod
    def parse_options(cls, options):
        cls.config = {
            'allow_docstrings': False
        }

        if hasattr(options, 'allow_docstrings') and options.allow_docstrings:
            cls.config['allow_docstrings'] = options.allow_docstrings

    def get_file_contents(self):
        if self.filename in ('stdin', '-', None):
            return stdin_get_value().splitlines(True)
        else:
            return readlines(self.filename)

    def run(self):
        file_contents = self.get_file_contents()

        errors = []

        tokens = [
            Token(t) for t in tokenize.generate_tokens(
                lambda L=iter(file_contents): next(L)
            )
        ]

        for token in tokens:
            if token.type == tokenize.NAME and token.string == 'class':
                # we found a class definition
                row_number = token.start_row
                next_row_number = row_number + 1

                next_row = []

                for sub_token in tokens:
                    if sub_token.start_row == next_row_number:
                        next_row.append(sub_token)

                    if sub_token.start_row > next_row_number:
                        break

                first_row_token = next_row[0]
                if first_row_token.type != 54 and first_row_token.type != 58:
                    is_error = True

                    if self.config['allow_docstrings'] and len(next_row) > 1:
                        start_with_indent = (
                            first_row_token.type == tokenize.INDENT
                        )

                        second_row_token = next_row[1]

                        first_three_letters = second_row_token.string[0:3]
                        quotes = "'''" == first_three_letters
                        double_quotes = '"""' == first_three_letters
                        starts_with_quotes = quotes or double_quotes

                        if start_with_indent and starts_with_quotes:
                            is_error = False

                    if is_error:
                        errors.append(
                            {
                                'line': token.start_row,
                                'col': token.start_col,
                                'message': self.message
                            }
                        )

        for error in errors:
            yield (
                error.get('line'),
                error.get('col'),
                error.get('message'),
                type(self)
            )


class Token:
    """Python 2 and 3 compatible token"""

    def __init__(self, token):
        self.token = token

    @property
    def type(self):
        return self.token[0]

    @property
    def string(self):
        return self.token[1]

    @property
    def start(self):
        return self.token[2]

    @property
    def start_row(self):
        return self.token[2][0]

    @property
    def start_col(self):
        return self.token[2][1]

    def __getitem__(self, item):
        return self.token[item]

    def __repr__(self):
        return 'Token(type {}, string {}, start_row {}, start_col {})'.format(
            self.type,
            self.string,
            self.start_row,
            self.start_col
        )
