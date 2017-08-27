new_lines_on = []


def new_line_checker(physical_line, line_number):
    if physical_line.startswith('class'):
        new_lines_on.append(line_number + 1)

    if line_number in new_lines_on:
        if not physical_line.isspace():
            # this means there's something on the line
            return 0, 'CNL100: Class definition does not have a new line.'

    return None


new_line_checker.name = 'new_line_checker'
new_line_checker.version = '1.2.0'
