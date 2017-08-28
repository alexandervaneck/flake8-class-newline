Flake8 Extension to lint for a method newline after a Class definition
===========================================

.. image:: https://travis-ci.org/AlexvEck/flake8-class-newline.svg?branch=master
    :target: https://travis-ci.org/AlexvEck/flake8-class-newline
   :alt: Build Status

Usage
-----

If you are using flake8, you can install this package through pip.

.. code:: shell

    pip install flake8-class-newline

This plugin is then automatically triggered when you run;

.. code:: shell

    flake8

It produces only 1 error type; "CNL100: Class definition does not have a new line."

NOTE; Documentation blocks (or docblocks) should be on the newline, they are therefore ignored by this plugin. See https://www.python.org/dev/peps/pep-0008/#documentation-strings


Example
-----

PEP8 says we should surround every class method with a single blank line. See https://www.python.org/dev/peps/pep-0008/#blank-lines
However flake8 is ambiguous about the first method having a blank line above it.

Basically;

.. code:: python

    class AClassWithoutANewLine(object):
        def a_method(self):
            return 'a_value'

    class AClassWithoutANewLineProperty(object):
        @property
        def a_method(self):
            return 'a_value'

or

.. code:: python

    class AClassWithANewLine(object):

        def a_method(self):
            return 'a_value'

    class AClassWithANewLineProperty(object):

        @property
        def a_method(self):
            return 'a_value'



This plugin was made to enforce the latter.

NOTE; properties of a class do not need a surrounding blank line, only methods.

Special Notice
-----

This package was inspired by flake8-quotes created by @zheller.
Thanks for the inspiration!