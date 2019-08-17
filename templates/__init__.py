import glob
import os
import importlib


def get_modules():
    modules = []
    __path = os.path.relpath(os.path.dirname(__file__))
    for file in glob.glob(__path + "/" + "*.py"):
        if not "__init__.py" in file:
            module = __path + "." + os.path.splitext(os.path.basename(file))[0]
            modules.append(importlib.import_module(module))
    return modules
