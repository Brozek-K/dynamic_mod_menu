from templates.utils import settings, templater

template_button = ' dmm_mod{category}_{count}:0 "Dynamic Mod Menu{category_name} {count}"'
template_title = ' dmm_mod{category}.{count}.title:0 "Slot Cleared"'
template_desc = ' dmm_mod{category}.{count}.desc:0 "Dynamic Mod Menu{category_name} {count} slot will been cleared from your game in 2 game days."'

categories = ["events", "gfx", "utilities", "other"]


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template_button.format(
            category="", category_name="", count=i))
        mod_lines.append(template_title.format(
            category="", category_name="", count=i))
        mod_lines.append(template_desc.format(
            category="", category_name="", count=i))
        for category in categories:
            mod_lines.append(template_button.format(
                category="_" + category, category_name=" " + category.capitalize(), count=i))
            mod_lines.append(template_title.format(
                category="_" + category, category_name=" " + category.capitalize(), count=i))
            mod_lines.append(template_desc.format(
                category="_" + category, category_name=" " + category.capitalize(), count=i))
    templater.process_file(
        publish_dir + "/localisation/english/dmm_localization_l_english.yml", localisation=mod_lines)
