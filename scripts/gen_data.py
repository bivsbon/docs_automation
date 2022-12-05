from concurrent.futures import ThreadPoolExecutor
from img_processing_module import ImgProcessingModule
import os
import cv2
import time

img_proc = ImgProcessingModule()
counter = 0
start_time = time.time()


def gen(file_index):
    global img_proc
    global start_time
    global counter
    file_name = str(file_index) + '.jpg'
    target_file = str(file_index+897) + '.jpg'
    f = os.path.join('../img_kh', file_name)
    cv2.imwrite('../dat/' + target_file, img_proc.get_fields_index(f, 2))
    counter += 1
    speed = counter / (time.time() - start_time)
    print(file_name + (' %.2f file/s' % speed))


executor = ThreadPoolExecutor(max_workers=5)

for i in range(1, 300):
    executor.submit(gen, i)
