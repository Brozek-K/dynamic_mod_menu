import winreg
import os
import glob
import zipfile
import io

path = os.path.relpath(os.path.dirname(__file__))


def validate():
    steam_apps = __find_steam_workshop_path()
    packages = __get_packages()
    for package in packages:
        package_name = package.replace(
            path + os.path.sep, "").split(os.path.sep)[0]
        package_path = path + "/" + package.replace(
            path + os.path.sep, "").split(os.path.sep)[0]
        package_id = __find_workshop_id(package_path)
        steam_package_path = steam_apps + "/" + package_id
        steam_content = __get_steam_package_content(
            package, steam_package_path)
        local_content = __get_existing_package_content(package)
        is_same = __clean__content(
            local_content) == __clean__content(steam_content)
        print("{package} is {status}".format(package=package_name,
                                             status="Up to date" if is_same else "NOT up to date"))
        if not is_same:
            __update_local_content(package, steam_content)
            print("{package} has been synced".format(package=package_name))


def __update_local_content(path, content):
    with open(path, "w+") as file:
        file.write(content)


def __clean__content(content):
    return content.replace(" ", "")


def __get_steam_package_content(package, steam_package_path):
    interface_path = package.replace(path + os.path.sep, "")
    interface_path = interface_path.replace(
        interface_path.split(os.path.sep)[0] + os.path.sep, "").replace(os.path.sep, "/")
    zip_file_path = glob.glob(steam_package_path + "/*.zip")
    # Seriously Python? https://docs.python.org/3/library/zipfile.html
    # Changed in version 3.6: Removed support of mode='U'. Use io.TextIOWrapper for reading compressed text files in universal newlines mode.
    with zipfile.ZipFile(zip_file_path[0], "r") as archive:
        with archive.open(interface_path) as file:
            return io.TextIOWrapper(file, "utf-8").read()
    return None


def __get_existing_package_content(package):
    with open(package, "r") as file:
        return file.read()


def __find_workshop_id(package_path):
    path = package_path + "/workshop_id.txt"
    with open(path, "r") as file:
        for line in file.readlines():
            if "patch_item_id=" in line:
                return line.replace("patch_item_id=", "").strip()
    return None


def __find_steam_workshop_path():
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.OpenKey(reg, "SOFTWARE\\WOW6432Node\\Valve\\Steam")
    path = winreg.QueryValueEx(key, "InstallPath")
    winreg.CloseKey(key)
    steam_apps = "/steamapps/workshop/content/281990"
    return path[0].strip(os.path.sep) + steam_apps


def __get_packages():
    return glob.glob(path + "/**/*.gui", recursive=True)
