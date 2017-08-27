Flake8 Extension to lint for a newline after a Class definition
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


Special Notice
-----

This package was inspired by flake8-quotes created by @zheller.
Thanks for the inspiration!