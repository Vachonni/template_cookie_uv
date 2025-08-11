"""Schemas for project {{cookiecutter.project_name}}"""

from enum import Enum

class AppEnvEnum(str, Enum):
    DEV = "dev"
    PROD = "prod"
    STAGING = "staging"
