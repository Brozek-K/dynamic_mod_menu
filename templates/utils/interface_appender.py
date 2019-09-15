el_id = "name={name}"


def process_file(path, target_el, append):
    lines = []
    append_id = None
    with open(path, "r") as file:
        opening_bracket_count = 0
        end_bracket_count = 0
        found_match = False
        counter = 0
        for line in file.readlines():
            if el_id.format(name=target_el) in line.strip().replace(" ", "").replace("\"", "").replace("'", ""):
                found_match = True
                opening_bracket_count += 1
            if found_match:
                if "{" in line:
                    opening_bracket_count += 1
                if "}" in line:
                    end_bracket_count += 1
                if opening_bracket_count == end_bracket_count:
                    append_id = counter
                    found_match = False
            counter += 1
            lines.append(line)

    if not append_id:
        raise AttributeError("No element found to append to.")
    lines.insert(append_id, append)

    with open(path, "w+") as file:
        for line in lines:
            file.write(line)
            if not line.endswith("\n"):
                file.write("\n")
