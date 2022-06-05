
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "Given all pre requirements are adequately installed use make local-run to run without docker"
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
