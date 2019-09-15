from templates.utils import interface_appender

template = """
		# Dynamic Mod Menu
		containerWindowType = {
			name = "dynamic_mod_menu_toolbar"
			position = { x = -480 y = -36 }
			size = { width = 80 height = 36 }
			orientation = lower_right
			clipping = yes

			background = {
				name = "dynamic_mod_menu_bg"
				quadTextureSprite = "GFX_topbar_background"
				position = { x = 0 y = 0  }
			}

			iconType = {
				name = "dynamic_mod_menu_bottombar_details"
				spriteType = "GFX_bottombar_details"
				position = { x= 0 y = -5 }
			}

			iconType = {
				name = "toggle_dynamic_mod_menu"
				spriteType = "GFX_topbar_dynamic_mod_menu_button"
				position = { x = -67 y = -37 }
				orientation = "LOWER_RIGHT"
				alwaystransparent = yes
			}

			effectButtonType = {
				name = "mod_menu_button"
				quadTextureSprite = "GFX_button_60_29"
				position = { x = -82 y = -46 }
				orientation = lower_right
				effect = "dynamic_mod_menu_open_launcher"
				shortcut="alt+m"
			}
		}
		# End Dynamic Mod Menu"""


def process(publish_dir):
    interface_appender.process_file(
        publish_dir + "/interface/main_bottom.gui", "maingui_bottombar", template)
