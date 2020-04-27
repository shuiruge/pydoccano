import json

from setuptools import setup, find_packages

from pydoccano import __version__


setup(
    name='pydoccano',
    version=__version__,
    description='This package for API of doccano',
    author='Bogdan Evstratenko)',
    author_email='evstrat.bg@gmail.com',
    url='https://github.com/evstratbg/pydoccano',
    packages=find_packages(),
    python_requires='>=3.7',
)
