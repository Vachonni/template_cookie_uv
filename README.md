# Cookiecutter Template: Project Starter Guide

This repository is a Cookiecutter template for quickly bootstrapping a new Python project with uv, Docker, Makefile, and a modern project structure.

## How to Start a New Project

1. **Install Cookiecutter** (if not already installed):
   ```bash
   pip install cookiecutter
   ```

2. **Generate a New Project**:

   In the folder where you want to create your new project,
   run the following command and follow the prompts:
   ```bash
   cookiecutter gh:vachonni/template_cookie_uv
   ```
   You will be asked for values like `project_slug` and `package_name`.

3. **Navigate to Your New Project**:
   ```bash
   cd <project_slug>
   ```

4. **Create repository and connect it to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin git@github.com:<your-username>/<project_slug>.git
   git push -u origin main
   ```

## Note about GitHub Actions expressions in the template

This template contains GitHub Actions expressions like {% raw %}`${{ github.actor }}`{% endraw %} inside workflow and composite action YAML files. Cookiecutter renders templates using Jinja, which also uses {% raw %}`{{ ... }}`{% endraw %} style delimiters. To avoid Jinja attempting to evaluate GitHub Actions expressions during template rendering, those expressions are wrapped with Jinja raw blocks, for example:

   "{{ '{% raw %}${{ github.actor }}{% endraw %}' }}"

That preserves the original GitHub Actions expression in the generated repository so
GitHub can evaluate it at runtime. Do not remove the raw blocks when editing these
workflow files unless you know what you're doing.


## Port Number Convention by Environment

Default port mappings (host:container) are configurable via cookiecutter variables:

| Environment | Host Port Variable              | Default | Container Port (app_port) |
|-------------|---------------------------------|---------|---------------------------|
| Dev         | dev_host_port                   | {{cookiecutter.dev_host_port}} | {{cookiecutter.app_port}} |
| Staging     | staging_host_port               | {{cookiecutter.staging_host_port}} | {{cookiecutter.app_port}} |
| Production  | prod_host_port                  | {{cookiecutter.prod_host_port}} | {{cookiecutter.app_port}} |

---
For more information, see the [Cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/).
