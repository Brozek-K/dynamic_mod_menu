from templates.utils import settings, templater

template_button = ' dmm_mod_{count}:0 "Dynamic Mod Menu {count}"'
template_title = ' dmm_mod.{count}.title:0 "Dynamic Mod Menu {count}"'
template_desc = ' dmm_mod.{count}.desc:0 "Dynamic Mod Menu {count}"'


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template_button.format(count=i))
        mod_lines.append(template_title.format(count=i))
        mod_lines.append(template_desc.format(count=i))
    templater.process_file(
        publish_dir + "/localisation/english/dmm_localization_l_english.yml", localisation=mod_lines)
