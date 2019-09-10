from templates.utils import settings, templater

template = """
		effectButtonType = {{
			name = "dmm_options_{main_count}_{secondary_count}"
			quadTextureSprite = "GFX_button_animated_110_34"
			position = {{ x = {pos_x} y = {pos_y} }}
			buttonFont = "cg_16b"
			buttonText = "dmm_options.{category}"
			clicksound = no_sound
			oversound = no_sound
			effect = "dynamic_mod_menu_open_{category}_{main_count}"
		}}"""

default_x = 0
default_y = 120

categories = ["general", "events", "gfx", "utilities", "other"]


def process(publish_dir):
    mod_lines = []
    pos = {
        'x': default_x,
        'y': default_y
    }
    for i in range(1, len(categories) + 1):
        for j in range(i, len(categories) + 1):
            mod_lines.append(template.format(
                main_count=i, secondary_count=j, category=categories[j-1], pos_x=pos['x'], pos_y=pos['y']))
        pos['x'] += 120
        if i % 4 == 0:
            pos['x'] = default_x
            pos['y'] += 54

    templater.process_file(
        publish_dir + "/interface/dynamic_mod_menu_ui_launcher.gui", buttons=mod_lines)
