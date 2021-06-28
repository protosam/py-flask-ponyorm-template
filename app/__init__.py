#!/usr/bin/env python3
# Set the server variable to reused
import os
from os.path import dirname, basename, join
import glob
from flask import Flask

# web server setup
server = Flask(__name__, template_folder=join(os.getcwd(), "templates"))

# get list of all the .py files
modules = glob.glob(join(dirname(__file__), "*.py"))

# prepate __all__ to be iterated on
__all__ = []

# add all the modules
for module in modules:
    if basename(module[:-3]) not in [ "__init__" ]:
        __all__.append(basename(module[:-3]))
