from templates.utils import settings, templater

last_id_var = "dynamic_mod_menu_gfx_last_id"
first_id_var = "dynamic_mod_menu_gfx_first_id"
event_2_3_template = """
        {if_statement} = {{
            limit = {{
                has_global_flag = dmm_mod_gfx_{count}
            }}
            set_variable = {{
                which = {variable}
                value = {count}
            }}
        }}"""
event_100_template = """
        remove_global_flag = dmm_mod_gfx_{count}
        remove_global_flag = dmm_mod_gfx_{count}_disabled"""
event_101_110_template = "        set_global_flag = dmm_mod_gfx_{count}"


def event_2_process():
    mod_lines = []
    for i in range(1, settings.total + 1):
        if i == 1:
            mod_lines.append(event_2_3_template.format(
                count=i, variable=first_id_var, if_statement="if"))
        else:
            mod_lines.append(event_2_3_template.format(
                count=i, variable=first_id_var, if_statement="else_if"))
    return mod_lines


def event_3_process():
    mod_lines = []
    for i in range(settings.total, 0, -1):
        if i == settings.total:
            mod_lines.append(event_2_3_template.format(
                count=i, variable=last_id_var, if_statement="if"))
        else:
            mod_lines.append(event_2_3_template.format(
                count=i, variable=last_id_var, if_statement="else_if"))
    return mod_lines


def event_100_process():
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(event_100_template.format(count=i))
    return mod_lines


def event_101_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 3):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_102_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 4):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_103_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 5):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_104_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 6):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_105_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 2):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_106_process():
    mod_lines = []
    for i in range(1, settings.total + 1, 1):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_107_process():
    mod_lines = []
    for i in range(1, 41, 1):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_108_process():
    mod_lines = []
    for i in range(1, 51, 1):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_109_process():
    mod_lines = []
    for i in range(21, 61, 1):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def event_110_process():
    mod_lines = []
    for i in range(21, 41, 1):
        mod_lines.append(event_101_110_template.format(count=i))
    return mod_lines


def process(publish_dir):
    templater.process_file(
        publish_dir + "/events/dynamic_mod_menu_gfx.txt",
        event_2=event_2_process(),
        event_3=event_3_process(),
        event_100=event_100_process(),
        event_101=event_101_process(),
        event_102=event_102_process(),
        event_103=event_103_process(),
        event_104=event_104_process(),
        event_105=event_105_process(),
        event_106=event_106_process(),
        event_107=event_107_process(),
        event_108=event_108_process(),
        event_109=event_109_process(),
        event_110=event_110_process())
