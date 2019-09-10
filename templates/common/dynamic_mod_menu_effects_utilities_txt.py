from templates.utils import settings, templater

template = """
dmm_mod_utilities_{main_event}_{secondary_event} = {{
    potential = {{
        has_global_flag = dmm_mod_utilities_{main_event}_{secondary_event}_active
    }}
    allow = {{
        NOT = {{
            has_global_flag = dmm_mod_utilities_{secondary_event}_opened
        }}
    }}
    effect = {{
        hidden_effect = {{            
            country_event = {{
                id = dmm_prepare_mod_utilities.{secondary_event}
            }}
        }}
    }}
}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.items_per_page + 1):
        for j in range(i, settings.total + 1):
            mod_lines.append(template.format(main_event=i, secondary_event=j))

    templater.process_file(
        publish_dir + "/common/button_effects/dynamic_mod_menu_effects_utilities.txt",
        effects=mod_lines)
