import re
from pathlib import Path

UID = r'#\$(?P<UID>\d{12})\$#?\s'
UID_PATTERN = re.compile(UID)
HEADER_END_PATTERN = re.compile(r'#META#Header#End#')


def create_yml_header():
    # TODO
    pass


def reassamble_text():
    # TODO
    pass


def extract_yml_data():
    # TODO
    # path = 'yml_data.yml'
    pass


def update_yml_header():
    # TODO
    pass


def split_text(file_path):
    eis_file = file_path + '.EIS1600'
    ids_file = file_path + '.IDs'
    mui_dir = Path(file_path + '/')
    uid = ''
    mui_text = ''

    mui_dir.mkdir(exist_ok=True)

    with open(eis_file, 'r', encoding='utf8') as text:
        with open(ids_file, 'w', encoding='utf8') as ids_tree:
            for text_line in text:
                if HEADER_END_PATTERN.match(text_line):
                    uid = 'header'
                    mui_text += text_line
                    with open(mui_dir.__str__() + '/' + uid + '.mui', 'w', encoding='utf8') as mui_file:
                        mui_file.write(mui_text + '\n')
                    mui_text = ''
                    uid = 'preface'
                    text_line = next(text)  # Empty line after header is added in the header.mui -> skip this line
                elif UID_PATTERN.match(text_line):
                    with open(mui_dir.__str__() + '/' + uid + '.mui', 'w', encoding='utf8') as mui_file:
                        mui_file.write(mui_text)
                    uid = UID_PATTERN.match(text_line).group('UID')
                    ids_tree.write(uid + '\n')
                    mui_text = text_line
                else:
                    mui_text += text_line


if __name__ == '__main__':
    path = 'texts_EIS1600/0795IbnRajabHanbali.DhaylTabaqatHanabila.Shamela0031366-ara1'

    split_text(path)

