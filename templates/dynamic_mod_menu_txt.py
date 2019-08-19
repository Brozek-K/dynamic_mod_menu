from templates.utils import settings, templater

last_id_var = "dynamic_mod_menu_last_id"
first_id_var = "dynamic_mod_menu_first_id"
event_2_3_template = """
        {2} = {{
            limit = {{
                has_global_flag = dmm_mod_{0}
            }}
            set_variable = {{
                which = {1}
                value = {0}
            }}
        }}"""
event_100_template = "        remove_global_flag = dmm_mod_{0}"
event_101_110_template = "        set_global_flag = dmm_mod_{0}"


def event_2_process():
    mod_lines = []
    for i in range(1, settings.total + 1):
        if i == 1:
            mod_lines.append(event_2_3_template.format(i, first_id_var, "if"))
        else:
            mod_lines.append(event_2_3_template.format(
                i, first_id_var, "else_if"))
    return mod_lines


def event_3_process():
    mod_lines = []
    for i in range(settings.total, 0, -1):
        if i == settings.total:
            mod_lines.append(event_2_3_template.format(i, last_id_var, "if"))
        else:
            mod_lines.append(event_2_3_template.format(
                i, last_id_var, "else_if"))
    return mod_lines


def event_100_process():
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(event_100_template.format(i))
    return mod_lines


def event_101_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 3):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_102_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 4):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_103_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 5):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_104_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 6):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_105_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 2):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_106_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 1):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_107_process():
    mod_lines = []
    for i in range(1, 41, 1):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_108_process():
    mod_lines = []
    for i in range(1, 51, 1):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_109_process():
    mod_lines = []
    for i in range(21, 61, 1):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def event_110_process():
    mod_lines = []
    for i in range(21, 41, 1):
        mod_lines.append(event_101_110_template.format(i))
    return mod_lines


def process(publish_dir):
    templater.process_file(
        publish_dir + "/events/dynamic_mod_menu.txt",
        event_2_process(),
        event_3_process(),
        event_100_process(),
        event_101_process(),
        event_102_process(),
        event_103_process(),
        event_104_process(),
        event_105_process(),
        event_106_process(),
        event_107_process(),
        event_108_process(),
        event_109_process(),
        event_110_process())
