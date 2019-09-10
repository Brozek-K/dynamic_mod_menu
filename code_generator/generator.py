import os
import codecs

event_template = """
namespace = dmm_mod{1}

country_event = {{
    id = dmm_mod{1}.{0}
    title = "dmm_mod{1}.{0}.title"
    desc = "dmm_mod{1}.{0}.desc"
    picture = GFX_evt_psionics
    is_triggered_only = yes

    trigger = {{
        has_global_flag = dmm_mod{1}_{0}
    }}

    after = {{
        remove_global_flag = dmm_mod{1}_{0}_opened
    }}

    option = {{
        name = "dmm_options.close"
    }}
}}"""

button_template = """
spriteTypes = {{
	spriteType = {{
		name = "GFX_dmm_mod{1}_{0}"
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
	}}
}}"""

localization_template = """
l_english:
 dmm_mod{1}_{0}:0 \"Dynamic Mod Menu {2} {0}\"
 dmm_mod{1}.{0}.title:0 \"Dynamic Mod Menu {2} {0}\"
 dmm_mod{1}.{0}.desc:0 \"Dynamic Mod Menu {2} {0}\""""


on_actions_template = """
on_game_start = {{
	events = {{
		    dmm_mod{1}_{0}_flag.1
        }}
}}
"""

global_flag_template = """
namespace = dmm_mod{1}_{0}_flag

event = {{
	id = dmm_mod{1}_{0}_flag.1
	hide_window = yes
	fire_only_once = yes
	is_triggered_only = yes

	trigger = {{
        NOT = {{
            has_global_flag = dmm_mod{1}_{0}
        }}
    }}

	immediate = {{
		set_global_flag = dmm_mod{1}_{0}
	}}
}}"""


categories = {
    "general": "",
    "events": "_events",
    "gfx": "_gfx",
    "utilities": "_utilities",
    "other": "_other"
}


def pick_id():
    id = 0
    while id == 0:
        try:
            value = input("Pick an number id from 1-251: ")
            eval_exit_requested(value)
            user_id = int(value)
            if user_id < 251:
                id = user_id
        except ValueError:
            pass
    return id


def pick_category():
    category = None
    while category == None:
        try:
            value = input(
                "Type a desired category, valid categories are: \"general\", \"events\", \"gfx\", \"utilities\" and \"other\": ")
            eval_exit_requested(value)
            if value in categories:
                category = {'name': value, 'value': categories[value]}
        except ValueError:
            pass
    return category


def eval_exit_requested(command):
    if command.lower() == "exit" or command.lower() == "quit":
        exit()


def save(path, template, bomEncoding=False):
    if bomEncoding:
        with codecs.open(path, "w+", "utf-8-sig") as file:
            file.write(template)
    else:
        with open(path, "w+") as file:
            file.write(template)


if __name__ == "__main__":
    print("When propmted type \"exit\" or \"quit\" to kill the script.")
    category = pick_category()
    cat_name = category['name']
    cat_value = category['value']
    id = pick_id()
    if not os.path.exists("events"):
        os.mkdir("events")
    if not os.path.exists("interface"):
        os.mkdir("interface")
    if not os.path.exists("localisation"):
        os.mkdir("localisation")
    if not os.path.exists("localisation/english"):
        os.mkdir("localisation/english")
    if not os.path.exists("localisation/english/replace"):
        os.mkdir("localisation/english/replace")
    if not os.path.exists("common"):
        os.mkdir("common")
    if not os.path.exists("common/on_actions"):
        os.mkdir("common/on_actions")
    save("events/000_dmm_mod{0}_".format(cat_value) + str(id) +
         ".txt", event_template.format(id, cat_value))
    save("events/dmm_mod{0}_flag_".format(cat_value) + str(id) +
         ".txt", global_flag_template.format(id, cat_value))
    save("interface/zzz_dmm_mod{0}_".format(cat_value) + str(id) +
         ".gfx", button_template.format(id, cat_value))
    save("localisation/english/replace/dmm_mod{0}_".format(cat_value) +
         str(id) + "_l_english.yml", localization_template.format(id, cat_value, cat_name.capitalize()), 1)
    save("common/on_actions/dmm_mod{0}_".format(cat_value) +
         str(id) + ".txt", on_actions_template.format(id, cat_value))
