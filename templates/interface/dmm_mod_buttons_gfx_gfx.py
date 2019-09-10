from templates.utils import settings, templater

template = """
	spriteType = {{
		name = "GFX_dmm_mod_gfx_{count}"
		texturefile = "gfx/interface/buttons/button_200_34_animated.dds"
		effectFile = "gfx/FX/buttonstate_onlydisable.lua"
		noOfFrames = 3
		animation = {{
			animationmaskfile = "gfx/interface/buttons/button_200_34_mask.dds"
			animationtexturefile = "gfx/interface/buttons/button_142_animated_texture.dds"
			animationrotation = 180.0
			animationlooping = yes
			animationtime = 40.0
			animationdelay = 0.0
			animationblendmode = "overlay"       #add, multiply, overlay
			animationtype = "scrolling"      #scrolling, rotating, pulsing
			animationrotationoffset = {{ x = 0.0 y = 0.0 }}
			animationtexturescale = {{ x = 1.0 y = 1.0 }}
			animationframes = {{ 1 2 3 }}
		}}
		hitbox_margin = {{ x=11 y=11 }}
	}}"""


def process(publish_dir):
    mod_lines = []
    mod_lines.append("spriteTypes = {")
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(count=i))
    mod_lines.append("}")
    templater.process_file(
        publish_dir + "/interface/dmm_mod_buttons_gfx.gfx", buttons=mod_lines)
