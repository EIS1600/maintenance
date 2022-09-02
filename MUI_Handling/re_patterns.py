import re


UID = r'#\$(?P<UID>\d{12})\$#?\s'
UID_PATTERN = re.compile(UID)
HEADER_END_PATTERN = re.compile(r'#META#Header#End#')

MUI_HEADER_PATTERN = re.compile(r'#MUI#Header#')
MUI_NEWLINE_PATTERN = re.compile(r'\n{3,}')
