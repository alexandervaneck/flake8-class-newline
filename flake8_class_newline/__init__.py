import optparse
import tokenize
import warnings

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
                next_row = row_number + 1

                # now find if the next row is a newline

                for sub_token in tokens:
                    if sub_token.start_row == next_row:
                        if sub_token.type != 54 and sub_token.type != 58:
                            errors.append(
                                {
                                    'line': token.start_row,
                                    'col': token.start_col,
                                    'message': self.message
                                }
                            )
                            break

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
        return '{}, {}, {}, {}, {}'.format(self.type, self.string, self.start,
                                           self.start_row, self.start_col)
