
##Cookiecutter: Python Project

A Cookiecutter project template for projects in Python.

### Getting Started

    pip install cookiecutter

    cookiecutter gh:posidron/cookiecutter-python-project

Cookiecutter will ask for some basic info and generate a base Python project for you.


### Publish to GitHub

    cd <project_name>
    git init
    git add .
    git commit -m "Introduce <project_name>"
    git remote add origin git@github.com:<github_username>/<project_name>.git
    git push -u origin master


### Features
* Pre-configured setup for Travis.
* Makefile for automating common development tasks:
    * Installing dependencies using pip
    * Running tests
    * Running source code bug and quality checker
    * Building documentation
    * Creating and releasing distributions to PyPI