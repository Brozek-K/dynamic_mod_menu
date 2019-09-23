from templates.utils import settings, templater

template = """
	option = {{
		name = "dmm_mod_utilities_{count}"
		custom_gui = "dynamic_mod_menu_ui_options_scroll_utilities_{count}"
		trigger = {{
			has_global_flag = dmm_mod_utilities_{count}
		}}
		allow = {{
			NOR = {{
				has_global_flag = dmm_mod_utilities_{count}_opened
				has_global_flag = dmm_mod_utilities_{count}_disabled
			}}
		}}		
		hidden_effect = {{
			remove_global_flag = dynamic_mod_menu_opened_utilities
			country_event = {{
				id = dynamic_mod_menu_scroll_utilities.1
			}}
			country_event = {{
				id = dmm_prepare_mod_utilities.{count}
			}}				
		}}
	}}"""


def options():
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(count=i))
    return mod_lines


def process(publish_dir):
    templater.process_file(
        publish_dir + "/events/dynamic_mod_menu_scroll_utilities.txt",
        options=options())
