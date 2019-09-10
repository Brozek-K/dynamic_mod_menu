from templates.utils import settings, templater

template_open_general = "            has_global_flag = dmm_mod_{count}"
template_open_events = "            has_global_flag = dmm_mod_events_{count}"
template_open_gfx = "            has_global_flag = dmm_mod_gfx_{count}"
template_open_utilities = "            has_global_flag = dmm_mod_utilities_{count}"
template_open_other = "            has_global_flag = dmm_mod_other_{count}"


def process_open_launcher():
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template_open_general.format(count=i))
        mod_lines.append(template_open_events.format(count=i))
        mod_lines.append(template_open_gfx.format(count=i))
        mod_lines.append(template_open_other.format(count=i))
        mod_lines.append(template_open_utilities.format(count=i))
    return mod_lines


def process(publish_dir):
    templater.process_file(
        publish_dir + "/common/button_effects/dynamic_mod_menu_effects_main.txt",
        open_flags_launcher=process_open_launcher())
