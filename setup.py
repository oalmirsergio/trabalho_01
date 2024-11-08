from setuptools import setup, find_packages
setup(
    name = 'jogovelha',
    version = 0.1,
    description = 'Game tic tac toe developed on NES work',
    install_requires = ['random','tabulate','abc','sys','os'],
    packages = find_packages(),
)
