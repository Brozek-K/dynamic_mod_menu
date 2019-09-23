from templates.utils import settings, templater

template = """
	containerWindowType = {{
		name = "dynamic_mod_menu_ui_options_scroll_{count}"
		position = {{
			x = 0
			y = 0
		}}
		size = {{
			width = 200
			height = 40
		}}
		moveable = no
		buttonType = {{
			name = "option_button"
			quadTextureSprite = "GFX_dmm_mod_{count}"
			position = {{ 
				x = 0
				y = 8
			}}
			font = "cg_16b"
			text = "OPTION_TEXT"
		}}
		OverlappingElementsBoxType = {{
			name = "trigger_icons"
			position = {{
				x = 0
				y = 10
			}}
			size = {{
				x = 200
				y = 38
			}}
		}}
	}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(count=i))

    templater.process_file(
        publish_dir + "/interface/dynamic_mod_menu_ui_scroll.gui", buttons=mod_lines)
