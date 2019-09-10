# Shitty pylint
# pylint: disable=no-value-for-parameter
import glob
import os
from importlib.machinery import SourceFileLoader

paths = ["common", "events", "interface", "localisation"]


def get_modules():
    modules = []
    __path = os.path.relpath(os.path.dirname(__file__))
    files = glob.glob(__path + "/" + "*.py")
    for path in paths:
        files.extend(glob.glob(__path + "/" + path + "/" + "*.py"))
    for file in files:
        if not "__init__.py" in file:
            path = os.path.relpath(file)
            name = os.path.splitext(os.path.basename(file))[0]
            module = SourceFileLoader(name, file).load_module()
            modules.append(module)
    return modules
