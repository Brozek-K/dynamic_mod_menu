from templates.utils import settings, templater

template_open = "            has_global_flag = dmm_mod_{0}"


def process_open():
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template_open.format(i))
    return mod_lines


def process(publish_dir):
    templater.process_file(
        publish_dir + "/common/button_effects/dynamic_mod_menu_effects.txt",
        process_open())
