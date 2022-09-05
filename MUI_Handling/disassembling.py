from pathlib import Path

from MUI_Handling.yml_handling import create_yml_header
from MUI_Handling.re_patterns import HEADER_END_PATTERN, UID_PATTERN


def disassemble_text(file_path, uri):
    eis_file = file_path + '.EIS1600'
    ids_file = file_path + '.IDs'
    mui_dir = Path(file_path + '/')
    uid = ''
    mui_text = ''

    mui_dir.mkdir(exist_ok=True)
    mui_uri = mui_dir.__str__() + '/' + uri + '.'

    with open(eis_file, 'r', encoding='utf8') as text:
        with open(ids_file, 'w', encoding='utf8') as ids_tree:
            for text_line in iter(text):
                if HEADER_END_PATTERN.match(text_line):
                    uid = 'header'
                    mui_text += text_line
                    with open(mui_uri + uid + '.EIS1600', 'w', encoding='utf8') as mui_file:
                        mui_file.write(mui_text + '\n')
                    mui_text = ''
                    uid = 'preface'
                    next(text)  # Skip empty line after header
                elif UID_PATTERN.match(text_line):
                    with open(mui_uri + uid + '.EIS1600', 'w', encoding='utf8') as mui_file:
                        mui_file.write(mui_text)
                    uid = UID_PATTERN.match(text_line).group('UID')
                    ids_tree.write(uid + '\n')
                    mui_text = create_yml_header()
                    mui_text += text_line
                else:
                    mui_text += text_line
            # last MUI needs to be written to file when the for-loop is finished
            with open(mui_uri + uid + '.EIS1600', 'w', encoding='utf8') as mui_file:
                mui_file.write(mui_text)
