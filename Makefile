
help:
	@echo "---------------HELP-----------------"
	@echo "To run the project type make run, given pre-requirements are installed"
	@echo "To test the project type make test"
	@echo "To setup the project on docker type make docker-setup"
	@echo "To run with docker use make docker-run"
	@echo "To release to heroku use make release-heroku, requires access to Pedro's heroku account"
	@echo "------------------------------------"

docker-setup:
	@docker-compose build

docker-run:
	@docker-compose up

test:
	@python3 -m pytest

docs:
	@echo "Click here: http://localhost:8000/docs"

run:
	@echo "Click here: http://localhost:8000/docs"
	@uvicorn src.main:app --reload

release-heroku:
	@docker build .
	@heroku container:push web
	@heroku container:release web
	@echo "Click here: https://bluestorm-admission-test.herokuapp.com/docs"
