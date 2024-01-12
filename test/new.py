import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

HORIZONTAL = 0
VERTICAL = 1

x_clusters = []
y_clusters = []


def get_vertical_and_horizontal_lines(x1, y1, x2, y2):
    updated = False
    global x_clusters
    global y_clusters
    if abs(x1 - x2) < 5:
        for i in range(len(x_clusters)):
            x_clusters[i], updated = update_x_cluster(x_clusters[i], x1, y1)
            x_clusters[i], updated = update_x_cluster(x_clusters[i], x2, y2)
        if not updated:
            if y1 > y2:
                x_clusters.append((x1, y1, x2, y2))
            else:
                x_clusters.append((x2, y2, x1, y1))
    elif abs(y1 - y2) < 5:
        for i in range(len(y_clusters)):
            y_clusters[i], updated = update_y_cluster(y_clusters[i], x1, y1)
            y_clusters[i], updated = update_y_cluster(y_clusters[i], x2, y2)
        if not updated:
            if x1 < x2:
                y_clusters.append((x1, y1, x2, y2))
            else:
                y_clusters.append((x2, y2, x1, y1))


def update_x_cluster(x_cluster, x, y):
    lpx, lpy, hpx, hpy = x_cluster
    is_between_lpx_and_hpx = x in range(lpx, hpx) or x in range(hpx, lpx)
    near_lpx = abs(lpx - x) < 5
    near_hpx = abs(hpx - x) < 5
    if near_lpx or near_hpx or is_between_lpx_and_hpx:
        if y > lpy:
            return (lpx, lpy, x, y), True
        elif y < hpy:
            return (x, y, hpx, hpy), True
    else:
        return x_cluster, False


def update_y_cluster(y_cluster, x, y):
    lpx, lpy, rpx, rpy = y_cluster
    is_between_lpy_and_rpy = y in range(lpy, rpy) or y in range(rpy, lpy)
    near_lpy = abs(lpy - y) < 5
    near_rpy = abs(rpx - y) < 5
    if near_lpy or near_rpy or is_between_lpy_and_rpy:
        if x > rpx:
            return (lpx, lpy, x, y), True
        elif x < lpx:
            return (x, y, rpx, rpy), True
    else:
        return y_cluster, False


img = cv.imread('../img/1.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv.Canny(img, 50, 200, None, 5)

# print(img.shape)
# print(rs_img.shape)
#
# Copy edges to the images that will display the results in BGR
cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)

linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 0)
hlines = []
vlines = []

if linesP is not None:
    for lineP in linesP:
        l = lineP[0]
        x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
        print('({}, {}) -> ({}, {})'.format(x1, y1, x2, y2))
        cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 255, 255), 3, cv.LINE_AA)
        # get_vertical_and_horizontal_lines(x1, y1, x2, y2)

print(len(x_clusters))
print(len(y_clusters))
# for cluster in x_clusters:
#     x1, y1, x2, y2 = cluster
#     cv.line(cdstP, (x1, y1), (x2, y2), (0, 255, 255), 5, cv.LINE_AA)
#
# for cluster in y_clusters:
#     x1, y1, x2, y2 = cluster
#     cv.line(cdstP, (x1, y1), (x2, y2), (0, 255, 255), 5, cv.LINE_AA)

for h in hlines:
    for v in vlines:
        img = cv2.circle(img, center=(v, h), radius=5, color=(0, 0, 255), thickness=-1)

# cv.imshow("Source", src)
# cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
# cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)

plt.figure()
plt.imshow(cdstP)
plt.show()
