.DEFAULT_GOAL := help

.PHONY: up
up: ## run the project
	@docker-compose run --service-ports --rm web

.PHONY: test
test: ## run the unittests
	@docker-compose run --service-ports --rm test

.PHONY: stop
stop: ## stop Docker containers without removing them
	@docker-compose stop

.PHONY: down
down: ## stop and remove Docker containers
	@docker-compose down --remove-orphans

.PHONY: rebuild
rebuild: ## rebuild base Docker images
	@docker-compose down --remove-orphans
	@docker-compose build --no-cache

.PHONY: fromscratch
fromscratch: rebuild up
