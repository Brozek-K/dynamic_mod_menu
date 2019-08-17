import glob
import os


def get_modules():
    modules = []
    __path = os.path.relpath(os.path.dirname(__file__))
    for file in glob.glob(__path + "/" + "*.py"):
        if not "__init__.py" in file:
            module = __path + "." + os.path.splitext(os.path.basename(file))[0]
            modules.append(__import__(module, fromlist=[None]))
    return modules
