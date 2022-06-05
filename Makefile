
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

run:
	@docker-compose build
	@docker-compose up

docs:
	@echo "Click here: http://localhost:8000/docs"
