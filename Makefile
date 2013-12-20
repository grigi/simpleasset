
help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    deps	Ensure dependancies are installed"
	@echo  "    check	Checks that build is sane"
	@echo  "    test	Runs tests"

checkdeps:
	@pip install -q pylint docutils

deps:

check: checkdeps
	@python setup.py -q check -m -r -s
	@pylint -E setup.py simpleasset

test: check deps
	@python setup.py -q test
