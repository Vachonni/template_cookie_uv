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

---
For more information, see the [Cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/).
