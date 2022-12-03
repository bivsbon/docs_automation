import openpyxl as xl
import os
from img_processing_module import get_fields
from file_mapper import get_mapping


def different(s1, s2):
    if len(s1) != len(s2):
        return True
    else:
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
            if count == 2:
                return True
    return False


def main():
    img_dir = 'img'
    excel_dir = 'excel'
    crit_cols_conf = {
        1: [1, 2, 3],
        2: [14, 7, 3]
    }

    # TODO: find some ways to input mode
    mode = 1

    mappings = get_mapping()
    # mapping[0] is img directory, mapping[1] is Excel file
    for mapping in mappings:
        path = os.path.join(excel_dir, mapping[1])
        wb = xl.load_workbook(path)
        sheet = wb.active
        crit_cols = crit_cols_conf[mode]

        for image in os.path.join(img_dir, mapping[0]):
            fields = get_fields(mode, image)

            for i in range(crit_cols):
                for i in range(2, sheet.max_row + 1):
                    cell = sheet.cell(row=i, column=crit_cols[i])
                    if different(str(cell.value), fields[i]):
                        # Fill the value in
                        cell.value = fields[i]
        wb.save(path)


if __name__ == "__main__":
    main()
