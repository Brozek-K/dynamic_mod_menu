from templates.utils import settings, templater

template = """
    spriteType = {{
		name = "GFX_dmm_mod_id_{0}"
		texturefile = "gfx/interface/buttons/dynamic_mod_menu_text_button.dds"
		noOfFrames = 1
    }}\n"""


def process(publish_dir):
    mod_lines = []
    mod_lines.append("spriteTypes = {\n")
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(i))
    mod_lines.append("}")
