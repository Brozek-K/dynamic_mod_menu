from templates.utils import settings, templater

template = """
            if = {{
                limit = {{
                    check_variable = {{
                        which = dynamic_mod_menu_items_processed
                        value = {0}
                    }}
                }}                
                    {1}                
            }}"""
template_else = """
            else_if = {{
                limit = {{
                    check_variable = {{
                        which = dynamic_mod_menu_items_processed
                        value = {0}
                    }}
                }}                
                    {1}                
            }}"""
template_mod = """
                if = {{
                    limit = {{
                        has_global_flag = dmm_mod_{1}
                        NOT = {{
                            has_global_flag = dmm_mod_{1}_active
                        }}
                    }}
                    set_global_flag = dmm_mod_{0}_{1}_active
                    set_global_flag = dmm_mod_{1}_active
                    change_variable = {{
                        which = dynamic_mod_menu_items_shown
                        value = 1
                    }}                    
                }}"""
template_mod_else = """
                else_if = {{
                    limit = {{
                        has_global_flag = dmm_mod_{1}
                        NOT = {{
                            has_global_flag = dmm_mod_{1}_active
                        }}
                    }}
                    set_global_flag = dmm_mod_{0}_{1}_active
                    set_global_flag = dmm_mod_{1}_active
                    change_variable = {{
                        which = dynamic_mod_menu_items_shown
                        value = 1
                    }}                    
                }}"""
template_remove_flag = """
        remove_global_flag = dmm_mod_{0}_{1}_active"""
template_remove_flag2 = """
        remove_global_flag = dmm_mod_{0}_active"""
template_remove_flag3 = """
        remove_global_flag = dmm_mod_{0}_opened"""


def process(publish_dir):
    event_1_mod_lines = []
    event_2_mod_lines = []
    event_3_mod_lines = []
    event_4_mod_lines = []
    for i in range(1, settings.total + 1):
        mod_text = ""
        event_3_mod_lines.append(template_remove_flag2.format(i))
        first_line = True
        for j in range(i, settings.total + 1):
            if first_line:
                mod_text += template_mod.format(i, j)
                first_line = False
            else:
                mod_text += template_mod_else.format(i, j)
            event_3_mod_lines.append(template_remove_flag.format(i, j))
            event_4_mod_lines.append(template_remove_flag3.format(i, j))
        if (i == 1):
            event_1_mod_lines.append(template.format(i, mod_text))
        else:
            event_1_mod_lines.append(template_else.format(i, mod_text))

    for i in range(settings.total, 0, -1):
        mod_text = ""
        first_line = True
        for j in range(settings.total, i - 1, -1):
            if first_line:
                mod_text += template_mod.format(i, j)
                first_line = False
            else:
                mod_text += template_mod_else.format(i, j)
        if (i == settings.total):
            event_2_mod_lines.append(template.format(i, mod_text))
        else:
            event_2_mod_lines.append(template_else.format(i, mod_text))

    templater.process_file(
        publish_dir + "/events/dynamic_mod_menu_pagination.txt",
        event_1_mod_lines,
        event_2_mod_lines,
        event_3_mod_lines,
        event_4_mod_lines)
