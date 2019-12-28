# Shitty pylint
# pylint: disable=no-value-for-parameter
import glob
import os
from templates.utils import locales
from importlib.machinery import SourceFileLoader

paths = ["common", "events", "interface", "localisation"]


def get_modules():
    modules = []
    curr_path = os.path.relpath(os.path.dirname(__file__))
    files = glob.glob(curr_path + "/" + "*.py")
    for path in paths:
        files.extend(glob.glob(curr_path + "/" + path + "/" + "*.py"))
    for file in files:
        if not "__init__.py" in file:
            name = os.path.splitext(os.path.basename(file))[0]
            module = SourceFileLoader(name, file).load_module()
            modules.append(module)
    return modules


def localize(destination):
    locales.process_locales(destination)
