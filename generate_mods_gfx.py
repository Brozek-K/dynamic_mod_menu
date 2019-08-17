import settings
template = """
    spriteType = {{
		name = "GFX_dmm_mod_id_{0}"
		texturefile = "gfx/interface/buttons/dynamic_mod_menu_text_button.dds"
		noOfFrames = 1
    }}\n"""


def process():
    with open("interface/dmm_mod_buttons.gfx", "w+") as file:
        file.write("spriteTypes = {\n")
        for i in range(1, settings.total + 1):
            file.write(template.format(i))
        file.write("}")


if __name__ == "__main__":
    process()