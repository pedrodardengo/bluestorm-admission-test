
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "To run without docker use make local-run, given pre-requirements are installed"
	@echo "To release to heroku use make release-heroku, requires access to Pedro's heroku account"
	@echo "------------------------------------"

setup:
	@docker-compose build

run:
	@docker-compose up

test:
	@python3 -m pytest

docs:
	@echo "Click here: http://localhost:8000/docs"

local-run:
	@uvicorn src.main:app --reload

release-heroku:
	@docker build .
	@heroku container:push web
	@heroku container:release web
	@echo "Click here: https://bluestorm-admission-test.herokuapp.com/docs"
