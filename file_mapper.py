from csv import reader


def get_mapping():
    mapping = []
    with open('./file_mapping.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            mapping.append(row)
    return mapping