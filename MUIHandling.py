import re


UID = r'#?\$(?P<UID>\d{12})\$#?\s'
UID_PATTERN = re.compile(UID)
HEADING_PATTERN = re.compile(UID + r'(?P<level>\|{1,4})')
MUI_PATTERN = re.compile(UID + r'\$(?P<entry_type>(?P<type>[A-Z]{3})_(?P<cat>[A-Z]{3}))\$')
SUBUNIT_PATTERN = re.compile(UID + r'::(?:(?P<type>[A-Z]+)::\s)+')

NODE = '├── '
END = '└── '
TAB = '│   '


# class State:
#     def __init__(self, level_1, level_2, level_3, level_4, mui, subunit):
#         self.level_1 = level_1
#         self.level_2 = level_2
#         self.level_3 = level_3
#         self.level_4 = level_4
#         self.mui = mui
#         self.subunit = subunit


def set_level(level):
    outline = ''
    while level > 0:
        outline += TAB
        level -= 1

    return outline + NODE


def split_text(eis_file, ids_file):
    level = 1
    with open(eis_file, 'r') as text:
        with open(ids_file, 'w', encoding='utf8') as ids_tree:
            for text_line in text:
                if UID_PATTERN.match(text_line):
                    outline = ''
                    if HEADING_PATTERN.match(text_line):
                        m = HEADING_PATTERN.match(text_line)
                        level = len(m.group('level'))

                        outline = set_level(level)
                        outline += m.group('UID') + '\n'
                    elif MUI_PATTERN.match(text_line):
                        m = MUI_PATTERN.match(text_line)

                        outline = set_level(level + 1)
                        outline += m.group('UID') + '\n'
                    elif SUBUNIT_PATTERN.match(text_line):
                        m = SUBUNIT_PATTERN.match(text_line)

                        outline = set_level(level + 2)
                        outline += m.group('UID') + '\n'

                    if outline:
                        ids_tree.write(outline)


if __name__ == '__main__':
    text_path = 'texts_EIS1600/0795IbnRajabHanbali.DhaylTabaqatHanabila.Shamela0031366-ara1.EIS1600'
    ids_file_path = 'texts_EIS1600/0795IbnRajabHanbali.DhaylTabaqatHanabila.Shamela0031366-ara1.IDs'

    split_text(text_path, ids_file_path)

