# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation

### uv
This project uses [uv](https://github.com/astral-sh/uv) for fast Python dependency management.

If you don't have uv installed, on Linux/macOS, run:
```sh
curl -Ls https://astral.sh/uv/install.sh | bash
```
More info at:
[https://github.com/astral-sh/uv#installation](https://github.com/astral-sh/uv#installation)


### virtual environment
To create a virtual environment and install all dependencies:

```sh
uv sync --dev
```

For production, use:

```sh
uv sync
```


## Port Number Convention by Environment

Default port mappings (host:container) are configurable via cookiecutter variables:

| Environment | Host Port Variable              | Default | Container Port (app_port) |
|-------------|---------------------------------|---------|---------------------------|
| Dev         | dev_host_port                   | {{cookiecutter.dev_host_port}} | {{cookiecutter.app_port}} |
| Staging     | staging_host_port               | {{cookiecutter.staging_host_port}} | {{cookiecutter.app_port}} |
| Production  | prod_host_port                  | {{cookiecutter.prod_host_port}} | {{cookiecutter.app_port}} |


## Running Tests

To run tests using uv, use:
```sh
uv run pytest
```


## Self-hosted GitHub Actions Runner (macOS)

This project deploys containers to a local machine using a self-hosted GitHub Actions runner.

For setup, follow GitHub’s official guide: https://docs.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners

Notes for this repo:
- Install the runner under `~/actions-runner` (matches the Makefile target).
- Docker Desktop must be running (the deploy steps use `docker`).
- Workflows run on `runs-on: self-hosted` (default labels are fine).

Run the runner from the repo root:

```bash
make run-runner
```