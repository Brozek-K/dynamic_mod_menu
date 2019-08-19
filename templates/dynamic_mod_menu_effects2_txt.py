from templates.utils import settings, templater

template = """
dmm_mod_{0}_{1} = {{
    potential = {{
        has_global_flag = dmm_mod_{0}_{1}_active
    }}
    allow = {{
        NOT = {{
            has_global_flag = dmm_mod_{1}_opened
        }}
    }}
    effect = {{
        hidden_effect = {{            
            country_event = {{
                id = dmm_prepare_mod.{1}
            }}
        }}
    }}
}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.items_per_page + 1):
        for j in range(i, settings.total + 1):
            mod_lines.append(template.format(i, j))

    templater.process_file(
        publish_dir + "/common/button_effects/dynamic_mod_menu_effects2.txt",
        mod_lines)
