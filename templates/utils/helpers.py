def prepare_for_format(text):
    # escape curly brackets
    text = text.replace("{", "{{").replace("}", "}}")
    # inject formatting brackets
    text = text.replace("[", "{").replace("]", "}")
    return text
