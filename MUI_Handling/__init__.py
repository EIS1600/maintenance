from MUI_Handling.disassembling import disassemble_text


if __name__ == '__main__':
    uri = '0795IbnRajabHanbali.DhaylTabaqatHanabila.Shamela0031366-ara1'
    path = '../texts_EIS1600/' + uri

    disassemble_text(path, uri)

