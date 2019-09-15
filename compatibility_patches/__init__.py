import os
import glob
import shutil
from templates.utils import interface_appender
from templates.interface.main_bottom_gui import template

path = os.path.relpath(os.path.dirname(__file__))


def publish_patches(publish_path, image):
    packages = __get_packages()
    for package in packages:
        new_package = publish_path + "/" + \
            package.replace(path + os.path.sep, "")
        __copy(package, new_package)
        __process_template(new_package)
        __copy_image(image, publish_path + "/" +
                     package.replace(path + os.path.sep, "").split(os.path.sep)[0])


def __copy_image(image, destination):
    shutil.copy(image, destination)


def __process_template(destination):
    interface_appender.process_file(destination, "maingui_bottombar", template)


def __copy(file, destination):
    dir_name = os.path.dirname(destination)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    shutil.copy(file, destination)


def __get_packages():
    return glob.glob(path + "/**/*.gui", recursive=True)
