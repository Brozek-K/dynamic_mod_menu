from templates.utils import settings, templater

template_button = ' dmm_mod_{0}:0 "Dynamic Mod Menu {0}"'
template_title = ' dmm_mod.{0}.title:0 "Dynamic Mod Menu {0}"'
template_desc = ' dmm_mod.{0}.desc:0 "Dynamic Mod Menu {0}"'


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template_button.format(i))
        mod_lines.append(template_title.format(i))
        mod_lines.append(template_desc.format(i))
    templater.process_file(
        publish_dir + "/localisation/english/dmm_localization_l_english.yml", mod_lines)
