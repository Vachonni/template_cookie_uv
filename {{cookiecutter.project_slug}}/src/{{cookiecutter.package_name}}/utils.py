import logging

from {{cookiecutter.package_name}}.config.logs import setup_logging

setup_logging()
logger = logging.getLogger(__name__)
