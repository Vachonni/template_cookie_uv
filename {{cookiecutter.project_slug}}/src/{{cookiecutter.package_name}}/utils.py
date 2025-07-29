import logging

from {{cookiecutter.package_name}}.config.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)
