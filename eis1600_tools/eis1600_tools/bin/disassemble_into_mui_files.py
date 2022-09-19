import sys
import os

from eis1600_tools.mui_handling import disassembling


if __name__ == "__main__":
    try:
        infilename = sys.argv[1]
    except IndexError:
        print('Pass in an EIS1600 file to begin')
        print(help)
        sys.exit()

    path, uri = os.path.split(infilename)
    uri, ext = os.path.splitext(uri)
    print(f'Disassemble {uri + ext} and storing MUI files in {path + "/" + uri + "/"}')
    disassembling.disassemble_text(path + '/' + uri, uri)

    print('Done')
