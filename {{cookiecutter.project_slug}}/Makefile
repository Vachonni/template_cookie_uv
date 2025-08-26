
# Makefile for {{cookiecutter.project_name}}.

# To run a make command, use `make <command>`...
# ...from any directory, use `make -C /complete/path/to/this/repo <command>`


# GitHub Container Registry path (without image name or tag)
GITHUB_REGISTRY={{cookiecutter.project_name}}

.PHONY: help pytest docker-build-dev docker-run-dev docker-up-dev docker-run-staging docker-run-prod 

help:
	@echo "Available targets:"
	@echo "  pytest            Run tests using pytest."
	@echo "  docker-build-dev  Build the dev Docker image only (does not run)."
	@echo "  docker-run-dev    Run the dev Docker container (does not rebuild)."
	@echo "  docker-up-dev     Build and run the dev Docker container."
	@echo "  docker-run-staging  Pull and run the staging Docker image with .env.staging."
	@echo "  docker-run-prod     Pull and run the prod Docker image with .env.prod."

pytest:
	uv run pytest

docker-build-dev: 
	# Build the Docker image for development
	docker-compose build {{cookiecutter.project_slug}}
docker-run-dev: 
	# Note: This will not rebuild the image, use `docker-build-dev` first if
	docker-compose up --no-build {{cookiecutter.project_slug}}
docker-up-dev: 
	# This will build the image and start the container
	docker-compose up --build {{cookiecutter.project_slug}}

docker-run-staging: 
	docker pull $(GITHUB_REGISTRY)/{{cookiecutter.project_slug}}:staging
	docker run \
	  --env-file .env.staging \
	  -p {{cookiecutter.staging_host_port}}:{{cookiecutter.app_port}} \
# 	  -v /Users/nicholas/Databases:/app/DatabasesMount \
	  $(GITHUB_REGISTRY)/{{cookiecutter.project_slug}}:staging

docker-run-prod: 
	docker pull $(GITHUB_REGISTRY)/{{cookiecutter.project_slug}}:prod
	docker run \
	  --env-file .env.prod \
	  -p {{cookiecutter.prod_host_port}}:{{cookiecutter.app_port}} \
# 	  -v /Users/nicholas/Databases:/app/DatabasesMount \
	  $(GITHUB_REGISTRY)/{{cookiecutter.project_slug}}:prod
