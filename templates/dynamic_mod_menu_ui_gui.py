from templates.utils import settings, templater

template = """
        effectButtonType = {{
            name = "dmm_mod_{0}_{1}"
            quadTextureSprite = "GFX_dmm_mod_id_{1}"
            position = {{ x = {2} y = {3} }}
            size = {{ x = 100 y = 50 }}
            buttonFont = "cg_16b"
            buttonText = "dmm_mod_{0}"
            clicksound = no_sound
            oversound = no_sound
            effect = "dmm_mod_{0}_{1}"
        }}"""

default_x = 25
default_y = 120


def process(publish_dir):
    mod_lines = []
    pos = {
        'x': default_x,
        'y': default_y
    }
    for i in range(1, settings.total + 1):
        for j in range(i, settings.total + 1):
            mod_lines.append(template.format(i, j, pos['x'], pos['y']))
        pos['x'] += 120
        if i % settings.items_per_line == 0:
            pos['x'] = default_x
            pos['y'] += 80
        if i % settings.items_per_page == 0:
            pos['x'] = default_x
            pos['y'] = default_y

    templater.process_file(
        publish_dir + "/interface/dynamic_mod_menu_ui.gui", mod_lines)
