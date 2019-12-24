import shutil
import os
from templates import get_modules
from compatibility_patches import publish_patches
from templates.utils import locales

copy_directories = ["common", "events", "gfx", "interface", "localisation"]
copy_files = ["Readme.txt", "descriptor.mod",
              "thumbnail.png", "1.jpg", "2.jpg", "3.jpg", "4.jpg"]

mod_name = "dynamic_mod_menu"
publish_path = "publish"
destination = publish_path + "/" + mod_name


def copy():
    for directory in copy_directories:
        if os.path.exists(directory):
            shutil.copytree(directory, destination + "/" + directory)

    for file in copy_files:
        if os.path.exists(file):
            shutil.copy(file, destination + "/" + file)


def clean_up():
    if os.path.exists(publish_path):
        shutil.rmtree(publish_path, True)


def process_templates():
    for module in get_modules():
        module.process(destination)


if __name__ == "__main__":
    clean_up()
    copy()
    process_templates()
    locales.process_locales(destination)
    publish_patches(publish_path, "thumbnail.png")
