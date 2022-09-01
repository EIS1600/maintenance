from MUI_Handling.re_patterns import MUI_HEADER_PATTERN


def create_yml_header():
    with open('template.yml', 'r', encoding='utf-8') as yml_template:
        yml_header = yml_template.read()
    # TODO: populate template with MUI related information
    return '\n\n' + yml_header + '\n'


def extract_yml_data(mui_file):
    with open(mui_file, 'r', encoding='utf-8') as file:
        for line in file:
            if MUI_HEADER_PATTERN.match(line):
                mui_yml_header = line
                line = next(file)
                while not MUI_HEADER_PATTERN.match(line):
                    mui_yml_header += line
                    line = next(file)
                mui_yml_header += line
                return mui_yml_header


def update_yml_header():
    # TODO: update YAML header with MUI related information from automated analyses and manual tags
    pass

