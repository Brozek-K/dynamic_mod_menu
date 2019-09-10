from templates.utils import settings, templater

event_1_2_template = """
            {if_statement} = {{
                limit = {{
                    check_variable = {{
                        which = dynamic_mod_menu_items_shown
                        value = {count}
                    }}
                }}
                    {sub_template}
            }}"""
event_1_sub_template_mod = """
                {if_statement} = {{
                    limit = {{
                        has_global_flag = dmm_mod_{secondary_count}
                        check_variable = {{
                            which = dynamic_mod_menu_processed_id
                            value < {secondary_count}
                        }}
                    }}
                    set_global_flag = dmm_mod_{count}_{secondary_count}_active
                    change_variable = {{
                        which = dynamic_mod_menu_items_shown
                        value = 1
                    }}
                    set_variable = {{
                        which = dynamic_mod_menu_processed_id
                        value = {secondary_count}
                    }}
                }}"""
event_2_sub_template_mod = """
                {if_statement} = {{
                    limit = {{
                        has_global_flag = dmm_mod_{secondary_count}
                        check_variable = {{
                            which = dynamic_mod_menu_processed_id
                            value > {secondary_count}
                        }}
                    }}
                    set_global_flag = dmm_mod_{count}_{secondary_count}_active
                    change_variable = {{
                        which = dynamic_mod_menu_items_shown
                        value = 1
                    }}
                    set_variable = {{
                        which = dynamic_mod_menu_processed_id
                        value = {secondary_count}
                    }}
                }}"""
event_1_2_sub_template_mod_else = """
                else = {{
                    set_variable = {{
                        which = dynamic_mod_menu_processed_id
                        value = {variable}
                    }}
                }}"""
event_3_template = """
        remove_global_flag = dmm_mod_{count}_{secondary_count}_active"""
event_4_template = """
        remove_global_flag = dmm_mod_{count}_opened"""
event_5_template = """
        {if_statement} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value = {count}
                }}
            }}
            set_variable = {{
                which = dynamic_mod_menu_last_processed_id
                value = {count}
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
        {if_statement} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_last_processed_id
                    value = {count}
                }}
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value >= {count}
                }}
            }}
            set_variable = {{
                which = dynamic_mod_menu_processed_id
                value = {secondary_count}
            }}
        }}"""
event_7_template = """
        {if_statement} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_last_processed_id
                    value = {count}
                }}
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value <= {count}
                }}
            }}
            set_variable = {{
                which = dynamic_mod_menu_processed_id
                value = {secondary_count}
            }}
        }}"""
event_8_template = """
        {if_statement} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_last_id
                    value = {count}
                }}
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value >= {count}
                }}
            }}
            set_global_flag = dynamic_mod_menu_no_new_pages
        }}"""
event_9_template = """
        {if_statement} = {{
            limit = {{
                check_variable = {{
                    which = dynamic_mod_menu_first_id
                    value = {count}
                }}
                check_variable = {{
                    which = dynamic_mod_menu_processed_id
                    value <= {count}
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
                mod_text += event_1_sub_template_mod.format(
                    count=i, secondary_count=j, if_statement="if")
                first_line = False
            else:
                mod_text += event_1_sub_template_mod.format(
                    count=i, secondary_count=j, if_statement="else_if")
        mod_text += event_1_2_sub_template_mod_else.format(
            variable="@last_empty_id")
        if (i == 1):
            mod_lines.append(
                event_1_2_template.format(count=i - 1, sub_template=mod_text, if_statement="if"))
        else:
            mod_lines.append(
                event_1_2_template.format(count=i - 1, sub_template=mod_text, if_statement="else_if"))
    return mod_lines


def event_2_process():
    mod_lines = []
    for i in range(settings.items_per_page, 0, -1):
        mod_text = ""
        first_line = True
        for j in range(settings.total, i - 1, -1):
            if first_line:
                mod_text += event_2_sub_template_mod.format(
                    count=i, secondary_count=j, if_statement="if")
                first_line = False
            else:
                mod_text += event_2_sub_template_mod.format(
                    count=i, secondary_count=j, if_statement="else_if")
        mod_text += event_1_2_sub_template_mod_else.format(
            variable="@first_empty_id")
        if (i == settings.items_per_page):
            mod_lines.append(event_1_2_template.format(
                count=abs(i - settings.items_per_page), sub_template=mod_text, if_statement="if"))
        else:
            mod_lines.append(event_1_2_template.format(
                count=abs(i - settings.items_per_page), sub_template=mod_text, if_statement="else_if"))
    return mod_lines


def event_3_process():
    mod_lines = []
    for i in range(1, settings.items_per_page + 1):
        for j in range(i, settings.total + 1):
            mod_lines.append(event_3_template.format(
                count=i, secondary_count=j))
    return mod_lines


def event_4_process():
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(event_4_template.format(count=i))
    return mod_lines


def event_5_process():
    mod_lines = []
    for i in range(1, settings.total + 1):
        if (i == 1):
            mod_lines.append(event_5_template.format(
                count=i, if_statement="if"))
        else:
            mod_lines.append(event_5_template.format(
                count=i, if_statement="else_if"))
    mod_lines.append(event_5_template_else)
    return mod_lines


def event_6_process():
    mod_lines = []
    for i in range(0, settings.total + 1):
        if (i == 0):
            mod_lines.append(event_6_template.format(
                count=i, secondary_count=i + 1, if_statement="if"))
        else:
            mod_lines.append(
                event_6_template.format(count=i, secondary_count=i + 1, if_statement="else_if"))
    return mod_lines


def event_7_process():
    mod_lines = []
    for i in range(1, settings.total + 2):
        if (i == 1):
            mod_lines.append(event_7_template.format(
                count=i, secondary_count=i - 1, if_statement="if"))
        else:
            mod_lines.append(event_7_template.format(
                count=i, secondary_count=i - 1, if_statement="else_if"))
    return mod_lines


def event_8_process():
    mod_lines = []
    for i in range(0, settings.total + 2):
        if i == 0:
            mod_lines.append(event_8_template.format(
                count=i, if_statement="if"))
        else:
            mod_lines.append(event_8_template.format(
                count=i, if_statement="else_if"))
    return mod_lines


def event_9_process():
    mod_lines = []
    for i in range(0, settings.total + 2):
        if i == 0:
            mod_lines.append(event_9_template.format(
                count=i, if_statement="if"))
        else:
            mod_lines.append(event_9_template.format(
                count=i, if_statement="else_if"))
    return mod_lines


def process(publish_dir):
    templater.process_file(
        publish_dir + "/events/dynamic_mod_menu_pagination.txt",
        event_1=event_1_process(),
        event_2=event_2_process(),
        event_3=event_3_process(),
        event_4=event_4_process(),
        event_5=event_5_process(),
        event_6=event_6_process(),
        event_7=event_7_process(),
        event_8=event_8_process(),
        event_9=event_9_process())
