#!/usr/bin/env python3
from .shared.base import db
from os.path import dirname, basename, isfile, join
import glob

# get list of all the .py files
modules = glob.glob(join(dirname(__file__), "*.py"))

# prepate __all__ to be iterated on
__all__ = []

# add all the modules
for module in modules:
    if basename(module[:-3]) not in [ "__init__" ]:
        __all__.append(basename(module[:-3]))


# import all the models to ensure things like this work:
#   db.generate_mapping(create_tables=True)
import importlib
for module in modules:
    if basename(module[:-3]) not in [ "__init__" ]:
        importlib.import_module("." + basename(module[:-3]), "models")

# Use the loader to do setup stuff
from .shared import loader