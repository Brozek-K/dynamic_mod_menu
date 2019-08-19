from templates.utils import settings, templater

event_1_2_template = """
            {2} = {{
                limit = {{
                    check_variable = {{
                        which = dynamic_mod_menu_items_shown
                        value = {0}
                    }}
                }}
                    {1}
            }}"""
event_1_sub_template_mod = """
                {2} = {{
                    limit = {{
                        has_global_flag = dmm_mod_{1}
                        check_variable = {{
                            which = dynamic_mod_menu_processed_id
                            value < {1}
                        }}
                    }}
                    set_global_flag = dmm_mod_{0}_{1}_active
                    change_variable = {{
                        which = dynamic_mod_menu_items_shown
                        value = 1
                    }}
                    set_variable = {{
                        which = dynamic_mod_menu_processed_id
                        value = {1}
                    }}
                }}"""
event_2_sub_template_mod = """
                {2} = {{
                    limit = {{
                        has_global_flag = dmm_mod_{1}
                        check_variable = {{
                            which = dynamic_mod_menu_processed_id
                            value > {1}
                        }}
                    }}
                    set_global_flag = dmm_mod_{0}_{1}_active
                    change_variable = {{
                        which = dynamic_mod_menu_items_shown
                        value = 1
                    }}
                    set_variable = {{
                        which = dynamic_mod_menu_processed_id
                        value = {1}
                    }}
                }}"""
event_1_2_sub_template_mod_else = """
                else = {{
                    set_variable = {{
                        which = dynamic_mod_menu_processed_id
                        value = {0}
                    }}
                }}"""
event_3_template = """
        remove_global_flag = dmm_mod_{0}_{1}_active"""
event_4_template = """
        remove_global_flag = dmm_mod_{0}_opened"""
event_5_template = """
        {1} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value = {0}
                }}
            }}
            set_variable = {{
                which = dynamic_mod_menu_last_processed_id
                value = {0}
            }}
        }}"""
event_5_template_else = """
        else = {
            set_variable = {
                which = dynamic_mod_menu_processed_id
                value = @first_empty_id
            }
            set_variable = {
                which = dynamic_mod_menu_last_processed_id
                value = @first_empty_id
            }
        }"""
event_6_template = """
        {2} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_last_processed_id
                    value = {0}
                }}
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value >= {0}
                }}
            }}
            set_variable = {{
                which = dynamic_mod_menu_processed_id
                value = {1}
            }}
        }}"""
event_7_template = """
        {2} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_last_processed_id
                    value = {0}
                }}
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value <= {0}
                }}
            }}
            set_variable = {{
                which = dynamic_mod_menu_processed_id
                value = {1}
            }}
        }}"""
event_8_template = """
        {1} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_last_id
                    value = {0}
                }}
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value >= {0}
                }}
            }}
            set_global_flag = dynamic_mod_menu_no_new_pages
        }}"""
event_9_template = """
        {1} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_first_id
                    value = {0}
                }}
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value <= {0}
                }}
            }}
            set_global_flag = dynamic_mod_menu_no_prev_pages
        }}"""


def event_1_process():
    mod_lines = []
    for i in range(1, settings.items_per_page + 1):
        mod_text = ""
        first_line = True
        for j in range(i, settings.total + 1):
            if first_line:
                mod_text += event_1_sub_template_mod.format(i, j, "if")
                first_line = False
            else:
                mod_text += event_1_sub_template_mod.format(i, j, "else_if")
        mod_text += event_1_2_sub_template_mod_else.format("@last_empty_id")
        if (i == 1):
            mod_lines.append(
                event_1_2_template.format(i - 1, mod_text, "if"))
        else:
            mod_lines.append(
                event_1_2_template.format(i - 1, mod_text, "else_if"))
    return mod_lines


def event_2_process():
    mod_lines = []
    for i in range(settings.items_per_page, 0, -1):
        mod_text = ""
        first_line = True
        for j in range(settings.total, i - 1, -1):
            if first_line:
                mod_text += event_2_sub_template_mod.format(i, j, "if")
                first_line = False
            else:
                mod_text += event_2_sub_template_mod.format(
                    i, j, "else_if")
        mod_text += event_1_2_sub_template_mod_else.format("@first_empty_id")
        if (i == settings.items_per_page):
            mod_lines.append(event_1_2_template.format(
                abs(i - settings.items_per_page), mod_text, "if"))
        else:
            mod_lines.append(event_1_2_template.format(
                abs(i - settings.items_per_page), mod_text, "else_if"))
    return mod_lines


def event_3_process():
    mod_lines = []
    for i in range(1, settings.items_per_page + 1):
        for j in range(i, settings.total + 1):
            mod_lines.append(event_3_template.format(i, j))
    return mod_lines


def event_4_process():
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(event_4_template.format(i))
    return mod_lines


def event_5_process():
    mod_lines = []
    for i in range(1, settings.total + 1):
        if (i == 1):
            mod_lines.append(event_5_template.format(i, "if"))
        else:
            mod_lines.append(event_5_template.format(i, "else_if"))
    mod_lines.append(event_5_template_else)
    return mod_lines


def event_6_process():
    mod_lines = []
    for i in range(0, settings.total + 1):
        if (i == 0):
            mod_lines.append(event_6_template.format(i, i + 1, "if"))
        else:
            mod_lines.append(
                event_6_template.format(i, i + 1, "else_if"))
    return mod_lines


def event_7_process():
    mod_lines = []
    for i in range(1, settings.total + 2):
        if (i == 1):
            mod_lines.append(event_7_template.format(i, i - 1, "if"))
        else:
            mod_lines.append(event_7_template.format(i, i - 1, "else_if"))
    return mod_lines


def event_8_process():
    mod_lines = []
    for i in range(0, settings.total + 2):
        if i == 0:
            mod_lines.append(event_8_template.format(i, "if"))
        else:
            mod_lines.append(event_8_template.format(i, "else_if"))
    return mod_lines


def event_9_process():
    mod_lines = []
    for i in range(0, settings.total + 2):
        if i == 0:
            mod_lines.append(event_9_template.format(i, "if"))
        else:
            mod_lines.append(event_9_template.format(i, "else_if"))
    return mod_lines


def process(publish_dir):
    templater.process_file(
        publish_dir + "/events/dynamic_mod_menu_pagination.txt",
        event_1_process(),
        event_2_process(),
        event_3_process(),
        event_4_process(),
        event_5_process(),
        event_6_process(),
        event_7_process(),
        event_8_process(),
        event_9_process())
