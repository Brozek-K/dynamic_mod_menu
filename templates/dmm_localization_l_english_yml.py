from templates.utils import settings, templater

template = ' dmm_mod_{0}:0 "Dynamic Mod Menu {0}"'


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1, 1):
        mod_lines.append(template.format(i))
    templater.process_file(
        publish_dir + "/localisation/english/dmm_localization_l_english.yml", mod_lines)
