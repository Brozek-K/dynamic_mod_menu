import templater
import settings
template = "set_global_flag = dmm_mod_id_{0}"


def process():
    mod_lines = []
    for i in range(1, settings.total + 1, 3):
        mod_lines.append(template.format(i))
    templater.process_file("events/dynamic_mod_menu.txt", mod_lines)


if __name__ == "__main__":
    process()
