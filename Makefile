
help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    deps	Ensure dependancies are installed"
	@echo  "    check	Checks that build is sane"
	@echo  "    test	Runs tests"

checkdeps:
	@pip install -q pylint docutils

deps:
	@pip install -q jinja2

check: checkdeps
	@python setup.py -q check -m -r -s
	@pylint -E setup.py simpleasset

test: check deps
	@python setup.py -q test

nose: check deps
	@nosetests --with-coverage --cover-package=simpleasset --with-spec --spec-color

