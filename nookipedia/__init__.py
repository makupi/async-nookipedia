from importlib_metadata import version
import logging

from .nookipedia import Nookipedia

__version__ = version("async-nookipedia")
logging.getLogger("async-nookipedia").addHandler(logging.NullHandler())
