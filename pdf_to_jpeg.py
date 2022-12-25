from pdf2image import convert_from_path


def convert_pdf_to_jpeg(file, name):
    img = convert_from_path(file, poppler_path=r'poppler-22.11.0/Library/bin')
    img[0].save(name, 'JPEG')
