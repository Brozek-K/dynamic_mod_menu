from templates.utils import settings, templater

template = """
        effectButtonType = {{
            name = "dmm_mod_other_{count}_{secondary_count}"
            quadTextureSprite = "GFX_dmm_mod_other_{secondary_count}"
            position = {{ x = {pos_x} y = {pos_y} }}            
            buttonFont = "cg_16b"
            buttonText = "dmm_mod_other_{secondary_count}"
            clicksound = no_sound
            oversound = no_sound
            effect = "dmm_mod_other_{count}_{secondary_count}"
        }}"""

default_x = 10
default_y = 120


def process(publish_dir):
    mod_lines = []
    pos = {
        'x': default_x,
        'y': default_y
    }
    for i in range(1, settings.items_per_page + 1):
        for j in range(i, settings.total + 1):
            mod_lines.append(template.format(
                count=i, secondary_count=j, pos_x=pos['x'], pos_y=pos['y']))
        pos['x'] += 220
        if i % settings.items_per_line == 0:
            pos['x'] = default_x
            pos['y'] += 54

    templater.process_file(
        publish_dir + "/interface/dynamic_mod_menu_ui_other.gui", buttons=mod_lines)
