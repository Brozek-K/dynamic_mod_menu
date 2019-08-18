from templates.utils import settings, templater

template = """
country_event = {{
    id = dmm_mod.{0}
    title = "dmm_mod.{0}.title"
    desc = "dmm_mod.{0}.desc"
    picture = GFX_evt_psionics
    is_triggered_only = yes

    trigger = {{
        has_global_flag = dmm_mod_{0}
    }}

    option = {{
        remove_global_flag = dmm_mod_{0}_opened
        name = "dmm_options.1.close"
    }}
}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(i))
    templater.process_file(
        publish_dir + "/events/dmm_mod.txt", mod_lines)
