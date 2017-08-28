new_lines_on = {}


def new_line_checker(logical_line, line_number, filename):
    if filename not in new_lines_on:
        new_lines_on[filename] = []

    if logical_line.startswith('class'):
        new_lines_on[filename].append(line_number + 1)

    if line_number in new_lines_on[filename]:
        # if the line is not only whitespace and not empty
        double_quotes = logical_line.strip().startswith('"""')
        quotes = logical_line.strip().startswith("'''")

        is_method = logical_line.strip().startswith('def')
        is_decorator = logical_line.strip().startswith('@')
        is_callable = is_method or is_decorator

        not_only_space = not logical_line.isspace() and logical_line
        not_is_docstring = not (quotes or double_quotes)

        if not_only_space and not_is_docstring and is_callable:
            # this means there's something on the line
            offset = line_number, 0
            yield offset, 'CNL100: Class definition does not have a new line.'


new_line_checker.name = 'new_line_checker'
new_line_checker.version = '1.5.0'
