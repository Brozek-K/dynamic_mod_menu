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
        package_name = package.replace(
            path + os.path.sep, "").split(os.path.sep)[0]
        full_publish_path = publish_path + "/" + package_name
        __copy(path + "/" + package_name, full_publish_path)
        __process_template(full_publish_path, new_package)
        __copy_image(image, full_publish_path)


def __copy_image(image, destination):
    shutil.copy(image, destination)


def __process_template(root, destination):
    override_template_path = root + "/template_override.txt"
    if os.path.exists(override_template_path):
        with open(override_template_path, "r") as file:
            template_text = file.read()
    else:
        template_text = template
    interface_appender.process_file(
        destination, "maingui_bottombar", template_text)


def __copy(source, destination):
    shutil.copytree(source, destination)


def __get_packages():
    return glob.glob(path + "/**/*.gui", recursive=True)
