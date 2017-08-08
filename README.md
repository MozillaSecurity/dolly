![Logo](https://github.com/posidron/posidron.github.io/raw/master/static/images/dolly.png)


A cookie cutter project for Python projects.


### Getting Started

```bash
    pip install cookiecutter
    cookiecutter gh:mozillasecurity/dolly
```

Dolly will ask you for some basic project information and will then generate a base Python project for you with all the boilerplate.


### Publish to GitHub

```bash
cd <project_name>
git init
git add .
git commit -m "Introduce <project_name>"
git remote add origin git@github.com:<github_username>/<project_name>.git
git push -u origin master
```

### Features
* Pre-configured setup for Travis.
* Makefile for automating common development tasks:
    * Installing dependencies using pip
    * Running tests
    * Running source code bug and quality checker
    * Building documentation
    * Creating and releasing distributions to PyPI
