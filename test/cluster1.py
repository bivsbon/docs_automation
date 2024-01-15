from concurrent.futures import ThreadPoolExecutor, wait

import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

HORIZONTAL = 0
VERTICAL = 1

v_lines = []
h_lines = []


def near(x, y):
    return abs(x-y) < 5


def cluserize(lines):
    clusters = []
    for line in lines:
        added = False
        for cluster in clusters:
            for i in cluster:
                if near(line, i):
                    cluster.append(line)
                    added = True
                    break
            if added:
                break
        if not added:
            clusters.append([line])
    return list(map(mean, clusters))


def get_vertical_and_horizontal_lines(x1, y1, x2, y2):
    if abs(x1 - x2) < 50:
        v_lines.append(x1)
    elif abs(y1 - y2) < 50:
        h_lines.append(y1)


def update_x_cluster(x_cluster, x, y):
    lpx, lpy, hpx, hpy = x_cluster
    is_between_lpx_and_hpx = x in range(lpx, hpx) or x in range(hpx, lpx)
    near_lpx = abs(lpx - x) < 20
    near_hpx = abs(hpx - x) < 20
    if near_lpx or near_hpx or is_between_lpx_and_hpx:
        print('near')
        if y >= lpy:
            return (x, y, hpx, hpy), True
        elif y <= hpy:
            return (lpx, lpy, x, y), True
    else:
        print('no near')
        return x_cluster, False


def update_y_cluster(y_cluster, x, y):
    lpx, lpy, rpx, rpy = y_cluster
    is_between_lpy_and_rpy = y in range(lpy, rpy) or y in range(rpy, lpy)
    near_lpy = abs(lpy - y) < 5
    near_rpy = abs(rpx - y) < 5
    if near_lpy or near_rpy or is_between_lpy_and_rpy:
        if x >= rpx:
            return (lpx, lpy, x, y), True
        elif x <= lpx:
            return (x, y, rpx, rpy), True
    else:
        return y_cluster, False


def process(img_path):
    img = cv.imread(img_path, cv2.IMREAD_GRAYSCALE)
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    dst = cv.Canny(im_bw, 50, 200, None, 5)

    # print(img.shape)
    # print(rs_img.shape)
    #
    # Copy edges to the images that will display the results in BGR
    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)

    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 55, 0)

    if linesP is not None:
        for lineP in linesP:
            l = lineP[0]
            x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
            # print('({}, {}) -> ({}, {})'.format(x1, y1, x2, y2))
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 255, 255), 3, cv.LINE_AA)
            get_vertical_and_horizontal_lines(x1, y1, x2, y2)
    print(cluserize(v_lines))
    print(cluserize(h_lines))
    for h in cluserize(h_lines):
        for v in cluserize(v_lines):
            img = cv2.circle(img, center=(v, h), radius=10, color=(0, 0, 255), thickness=1)

    return img, cdstP


def process_and_save(img_path, out_path):
    img, cdstP = process(img_path)

    cv.imwrite(out_path, img)


def process_and_show(img_path, out_path):
    img, cdstP = process(img_path)

    # cv.imwrite(out_path, img)
    plt.figure()
    plt.imshow(img)
    plt.show()


# for i in range(200):
#     print(i+1)
#     process_and_save('../img/{}.jpg'.format(i+1), '../out/{}.jpg'.format(i+1))

order = 13
process_and_show('../img/{}.jpg'.format(order), '../out/{}.jpg'.format(order))