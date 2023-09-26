from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.7'
DESCRIPTION = 'Error Handling and Logging Toolkit for Python'
LONG_DESCRIPTION = 'A toolkit for enhanced error handling and logging in Python applications.'

# Setting up
setup(
    name="python-error",
    version=VERSION,
    author="PB2204 (Pabitra Banerjee)",
    author_email="<rockstarpabitra2204@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/pb2204/py-error-handling-toolkit',
    keywords=['python', 'error', 'log', 'error handling', 'debugging'],
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)