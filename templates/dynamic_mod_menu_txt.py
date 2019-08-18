from templates.utils import settings, templater

template = "        set_global_flag = dmm_mod_{0}"


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1, 3):
        mod_lines.append(template.format(i))
    templater.process_file(
        publish_dir + "/events/dynamic_mod_menu.txt", mod_lines)
