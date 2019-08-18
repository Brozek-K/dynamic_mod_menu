from templates.utils import settings, templater

template = """
country_event = {{
    id = dmm_prepare_mod.{0}
    hide_window = yes
    is_triggered_only = yes

    trigger = {{
        has_global_flag = dmm_mod_{0}
    }}

    immediate = {{
        set_global_flag = dmm_mod_{0}_opened
        country_event = {{
            id = dmm_mod.{0}
        }}
    }}
}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(i))
    templater.process_file(
        publish_dir + "/events/dmm_prepare_mod.txt", mod_lines)
