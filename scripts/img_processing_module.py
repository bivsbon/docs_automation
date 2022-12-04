import cv2
import torch


class ImgProcessingModule:
    def __init__(self):
        self.model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'best.pt')
        self.model.conf = 0.3

    def get_fields(self, path_img):
        "Lay 4 truong thong tin tu anh"
        img = cv2.imread(path_img)
        results = self.model(img[:, :, ::-1])
        data = results.pandas().xyxy[0]
        data = data.sort_values(by=['class']).reset_index(drop=True)
        list_img = []
        for i in range(len(data)):
            xmin = int(data['xmin'][i])
            ymin = int(data['ymin'][i])
            xmax = int(data['xmax'][i])
            ymax = int(data['ymax'][i])
            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 0), thickness=5)
            list_img.append(img[ymin:ymax, xmin: xmax])
        cv2.imshow('img', img)
        cv2.waitKey(0)

        return list_img

    def get_fields_index(self, path_img, i):
        img = cv2.imread(path_img)
        results = self.model(img[:, :, ::-1])
        data = results.pandas().xyxy[0]
        data = data.sort_values(by=['class']).reset_index(drop=True)
        xmin = int(data['xmin'][i])
        ymin = int(data['ymin'][i])
        xmax = int(data['xmax'][i])
        ymax = int(data['ymax'][i])

        return img[ymin:ymax, xmin: xmax]


module = ImgProcessingModule()
module.get_fields('../img_kh/2.jpg')
