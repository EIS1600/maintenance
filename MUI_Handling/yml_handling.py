from MUI_Handling.re_patterns import MUI_HEADER_PATTERN, MUI_NEWLINE_PATTERN
import importlib.resources as pkg_resources


yml_template = pkg_resources.read_text(__package__, 'template.yml')


def create_yml_header():
    yml_header = yml_template
    # TODO: populate template with MUI related information
    return yml_header + '\n'


def extract_yml_header_and_text(mui_file, mui_id, is_header):
    with open(mui_file, 'r', encoding='utf-8') as file:
        text = ''
        mui_yml_header = ''
        for line in iter(file):
            if MUI_HEADER_PATTERN.match(line):
                # Omit the #MUI#Header# line as it is only needed inside the MUI.EIS1600 file, but not in yml_data.yml
                next(file)
                line = next(file)
                mui_yml_header = '#' + mui_id + '\n---\n'
                while not MUI_HEADER_PATTERN.match(line):
                    mui_yml_header += line
                    line = next(file)
                # Skip empty line after #MUI#Header#
                next(file)
            else:
                text += line
            # Replace new lines which separate YAML header from text
            if not is_header:
                text, n = MUI_NEWLINE_PATTERN.subn('\n\n', text)
        return mui_yml_header, text


def update_yml_header():
    # TODO: update YAML header with MUI related information from automated analyses and manual tags
    pass
