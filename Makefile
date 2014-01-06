
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

nosedeps:
	@pip install -q nose coverage pinocchio

check: checkdeps
	@pylint -E setup.py simpleasset
	@-python setup.py -q check -m -r -s

test: check deps
	@python setup.py -q test

nose: nosedeps deps
	@nosetests --with-coverage --cover-erase --cover-branches --cover-package=simpleasset --with-spec --spec-color

tox:
	@pip install -q tox
	@tox

lint:
	@-pylint -r n --msg-template='{msg_id}: {line}, {column}: {msg} ({symbol}){obj}' setup.py simpleasset scripts/*.py
