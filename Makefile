# ==============================================================================
# Makefile for CredKit CRM
# ==============================================================================

# Use sudo for docker commands as required by the environment
DOCKER_COMPOSE = sudo docker compose -f infra/docker/docker-compose.yml

.PHONY: help up down logs ps build seed test lint migrate

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  up        - Start all services in detached mode"
	@echo "  down      - Stop and remove all services"
	@echo "  logs      - Tail the logs of all services"
	@echo "  ps        - List running services"
	@echo "  build     - Build or rebuild services"
	@echo "  seed      - Seed the database"
	@echo "  test      - Run tests for all applications"
	@echo "  lint      - Lint all applications"
	@echo "  migrate   - Run database migrations"


# Docker Compose commands
up:
	@echo "Starting all services..."
	$(DOCKER_COMPOSE) up -d --build

down:
	@echo "Stopping and removing all services..."
	$(DOCKER_COMPOSE) down

logs:
	@echo "Tailing logs..."
	$(DOCKER_COMPOSE) logs -f

ps:
	@echo "Listing services..."
	$(DOCKER_COMPOSE) ps

build:
	@echo "Building services..."
	$(DOCKER_COMPOSE) build

# Application specific commands
seed:
	@echo "Seeding database..."
	$(DOCKER_COMPOSE) run --rm api python /ops/scripts/seed.py

test:
	@echo "Running tests..."
	$(DOCKER_COMPOSE) run --rm api pytest --rootdir /app/tests
	# $(DOCKER_COMPOSE) run --rm web npm test

lint:
	@echo "Linting..."
	$(DOCKER_COMPOSE) run --rm api ruff check .
	# $(DOCKER_COMPOSE) run --rm web npm run lint

migrate:
	@echo "Running database migrations..."
	$(DOCKER_COMPOSE) run --rm api alembic upgrade head
