__begin_id = "### BEGIN TEMPLATE:{id} ###"
__end_id = "### END TEMPLATE:{id} ###"


def process_file(path, **args):
    lines = []
    with open(path, "r") as file:
        write = True
        for line in file.readlines():
            if __get_starting_matching_item(line, args):
                lines.append(line)
                write = False
            if __get_ending_matching_item(line, args):
                write = True
            if write:
                lines.append(line)

    with open(path, "w+") as file:
        matching_item = 0
        ending_item = 0
        for line in lines:
            file.write(line)
            if not line.endswith("\n"):
                file.write("\n")
            mod_lines = __get_starting_matching_item(line, args)
            if mod_lines:
                matching_item += 1
                for mod_line in mod_lines:
                    file.write(mod_line)
                    if not mod_line.endswith("\n"):
                        file.write("\n")
            if __get_ending_matching_item(line, args):
                ending_item += 1
        if matching_item != ending_item:
            raise AttributeError("There is an error in template tags.")


def __get_starting_matching_item(line, args):
    for k in args.keys():
        if __begin_id.format(id=k) in line:
            return args[k]

    return None


def __get_ending_matching_item(line, args):
    for k in args.keys():
        if __end_id.format(id=k) in line:
            return args[k]

    return None
