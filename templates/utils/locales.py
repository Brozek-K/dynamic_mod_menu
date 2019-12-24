import glob
import os

locales = ["l_braz_por", "l_french", "l_german",
           "l_polish", "l_russian", "l_simp_chinese", "l_spanish"]

default_locale = "l_english"


def process_locales(destination):
    localisation_dir = destination + "/localisation"
    english = localisation_dir + "/english"
    files = glob.glob(english + "/**/*.yml", recursive=True)
    for locale in locales:
        path = __locale_to_path(localisation_dir, locale)
        if not os.path.exists(path):
            os.makedirs(path)
        for file in files:
            content = ""
            with open(file, "r") as f:
                content = f.read().replace(default_locale, locale)

            out = __parse_destination_locale_path(file, path, locale)
            if not os.path.exists(os.path.dirname(out)):
                os.makedirs(os.path.dirname(out))
            with open(out, "w+") as f:
                f.write(content)


def __locale_to_path(root_dir, locale):
    return root_dir + "/" + locale.replace("l_", "")


def __parse_destination_locale_path(original_path, root_locale_path, locale):
    path = os.path.basename(original_path).replace(default_locale, locale)
    if "replace" in original_path:
        return root_locale_path + "/replace/" + path
    return root_locale_path + "/" + path
