def parse_docstring(docstring: str):
    data = {}
    docstring = docstring.strip()
    lines = docstring.splitlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        dirty_line = line.split(":")
        data[dirty_line[0]] = dirty_line[1].strip()
    return data
