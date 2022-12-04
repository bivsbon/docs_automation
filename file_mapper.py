from csv import reader


def get_mappings():
    mappings = []
    with open('./file_mapping.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            mappings.append(row)
    return mappings
