import cv2
import torch
import os

directory = '../img_kh'
model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'best.pt')
model.conf = 0.3
counter = 1


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    "Lay 4 truong thong tin tu anh"
    img = cv2.imread(f)
    results = model(img[:, :, ::-1])
    data = results.pandas().xyxy[0]
    data = data.sort_values(by=['class']).reset_index(drop=True)
    list_img = []
    xmin = int(data['xmin'][1])
    ymin = int(data['ymin'][1])
    xmax = int(data['xmax'][1])
    ymax = int(data['ymax'][1])
    image = img[ymin:ymax, xmin: xmax]
    image.imwrite('dat')