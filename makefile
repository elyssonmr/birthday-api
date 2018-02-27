test: clean
	pytest --cov-report term-missing --cov=birthday tests/
check:
	flake8 --config=configs/flake8
	pylint .
clean:
	rm -rf .cache .coverage coverage *.pyc
