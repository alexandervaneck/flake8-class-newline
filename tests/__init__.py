class AClassWithNewLine(object):

    an_arg = 'a_value'


class AClassWithoutNewLine(object):
    an_arg = 'value'


class ClassWithDoubleDocstringShouldBeIgnored(object):
    """
     a dicstrubg
    """
    an_arg = 'value'


class ClassWithSingleDocstringShouldBeIgnored(object):
    '''
    a docstring
    '''
    an_arg = 'value'
