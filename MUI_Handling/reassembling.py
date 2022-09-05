from MUI_Handling.yml_handling import extract_yml_header_and_text


def reassemble_text(file_path, uri):
    ids = ['header', 'preface']
    with open(file_path + '.IDs', 'r', encoding='utf-8') as ids_file:
        ids.extend([line[:-1] for line in ids_file.readlines()])

    with open(file_path + '.EIS1600', 'w', encoding='utf-8') as text_file:
        with open(file_path + '.yml_data.yml', 'w', encoding='utf-8') as yml_data:
            for i, mui_id in enumerate(ids):
                mui_file_path = file_path + '/' + uri + '.' + mui_id + '.EIS1600'
                yml_header, text = extract_yml_header_and_text(mui_file_path, mui_id, i == 0)
                text_file.write(text)
                yml_data.write(yml_header)
