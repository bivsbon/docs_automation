from img_processing_module import ImgProcessingModule
from model.model import predict
import cv2 as cv

img_module = ImgProcessingModule(mode=1)
fields = img_module.get_fields('test_img/3.jpg')
for field in fields:
    cv.imshow('img', field)
    cv.waitKey(0)
    print(predict(field))
