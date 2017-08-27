import io
import os
from setuptools import setup

__dir__ = os.path.dirname(__file__)


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


LONG_DESCRIPTION = read(os.path.join(__dir__, 'README.rst'))

version = {}
with open(
        os.path.join(__dir__, 'flake8_class_newline', '__version__.py')
) as file:
    exec(file.read(), version)

setup(
    name='flake8-class-newline',
    author='Alexander van Eck',
    author_email='alex@x-all.nl',
    version=version['__version__'],
    install_requires=[
        'flake8',
    ],
    long_description=LONG_DESCRIPTION,
    description='Flake8 lint for newline after class definitions.',
    packages=['flake8_class_newline'],
    test_suite='tests',
    include_package_data=True,
    entry_points={
        'flake8.extension': [
            'CNL100 = flake8_class_newline:new_line_checker'
        ],
    },
    license='MIT',
    zip_safe=True,
    keywords='flake8 lint class new line',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ]
)
