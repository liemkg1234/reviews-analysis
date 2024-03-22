# Build and start
build:
	docker build -t reviews-analysis-endpoint -f Dockerfile_endpoints .
	docker build -t reviews-analysis-ui -f Dockerfile_UI .

start:
	docker compose -f docker-compose.yml down
	docker compose -f docker-compose.yml up -d

stop:
	docker compose -f docker-compose.yml down