class ClassWithoutANewLine(object):
    aaasome_arg = 'a_string'


class ClassWithNewLine(object):

    some_arg = 'a_string'


class ClassFollowedByDoubleQuoteDocString(object):
    """
    A docstring
    """


class ClassFollowedBySingleQuoteDocString(object):
    '''
    A docstring
    '''
