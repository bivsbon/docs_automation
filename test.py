from pdf_to_jpeg import convert_pdf_to_jpeg
from model.model import TextRecognizer
from img_processing_module import ImgProcessingModule

text_model = TextRecognizer("weights/name.pth")
date_model = TextRecognizer("weights/date.pth")
img_processing_module = ImgProcessingModule(3)


def func():
    convert_pdf_to_jpeg('pdf_test/KS.2010.01.001.PDF', 'img_ks/1.jpg')
    fields = img_processing_module.get_fields('img_ks/1.jpg')
    print(text_model.predict(fields[0]))
    print(date_model.predict(fields[1]))


func()
