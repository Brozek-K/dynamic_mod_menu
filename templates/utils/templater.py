__begin_id = "### BEGIN TEMPLATE ###"
__end_id = "### END TEMPLATE ###"


def process_file(path, *args):
    lines = []
    with open(path, "r") as file:
        write = True
        for line in file.readlines():
            if __begin_id in line:
                lines.append(line)
                write = False
            if __end_id in line:
                write = True
            if write:
                lines.append(line)

    with open(path, "w+") as file:
        id = 0
        for line in lines:
            file.write(line)
            if __begin_id in line:
                for mod_line in args[id]:
                    file.write(mod_line + "\n")
                id += 1
