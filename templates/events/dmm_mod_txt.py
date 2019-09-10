from templates.utils import settings, templater

template = """
country_event = {{
    id = dmm_mod.{count}
    title = "dmm_mod.{count}.title"
    desc = "dmm_mod.{count}.desc"
    picture = GFX_evt_psionics
    is_triggered_only = yes

    trigger = {{
        has_global_flag = dmm_mod_{count}
    }}

    after = {{
        remove_global_flag = dmm_mod_{count}_opened
    }}

    option = {{        
        name = "dmm_options.1.close"
    }}
}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(count=i))
    templater.process_file(
        publish_dir + "/events/dmm_mod.txt", events=mod_lines)
