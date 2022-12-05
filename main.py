import openpyxl as xl
import os
from img_processing_module import ImgProcessingModule
from file_mapper import get_mappings
from model.model import predict
from openpyxl.styles import PatternFill


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
        1: [16, 17, 27, 28]
    }

    # TODO: find some ways to input mode
    mode = 1
    img_module = ImgProcessingModule(mode)

    # Get mapping between image directory and Excel file
    mappings = get_mappings()
    # mapping[0] is img directory, mapping[1] is Excel file
    for mapping in mappings:
        # Load Excel sheet
        path = os.path.join(excel_dir, mapping[1])
        wb = xl.load_workbook(path)
        sheet = wb.active
        crit_cols = crit_cols_conf[mode]

        img_dir2 = os.path.join(img_dir, mapping[0])
        # Loop through images sheet rows and images
        # for i in range(2, sheet.max_row + 1):
        for i in range(2, 7):
            img_path = f'{img_dir2}\\{i-1}.jpg'
            fields = img_module.get_fields(img_path)

            # Check if number of detected fields match number of columns
            if len(fields) == len(crit_cols):
                for field_index in range(len(fields)):
                    col_index = field_index
                    prediction = predict(fields[field_index])
                    cell = sheet.cell(row=i, column=crit_cols[col_index])

                    # Check if prediction is the same as value in Excel
                    # if different(str(cell.value), prediction):
                    if prediction != str(cell.value):
                        # Fill the value in
                        print(f"Changing {str(cell.value)} into {prediction} in coord {cell.coordinate}")
                        cell.value = prediction
                        cell.fill = PatternFill(start_color="FFE900", end_color="FFE900", fill_type="solid")

            else:
                # TODO: Field detection error
                print(f"Field detection error at index {i}")

        wb.save("modified.xlsx")


if __name__ == "__main__":
    main()
