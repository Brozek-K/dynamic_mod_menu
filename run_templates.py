import generate_mods_gfx
import generate_pagination_next
import generate_test_flags

modules = [generate_mods_gfx, generate_pagination_next, generate_test_flags]


def create_templates():
    for module in modules:
        module.process()


if __name__ == "__main__":
    create_templates()
