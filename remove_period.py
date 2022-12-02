import cv2 as cv
import time
import os
from math import atan, degrees

directory = 'img'
WIDTH = 780
HEIGHT = 113


def find_ref_x_right(img, x, y):
    found = False
    while not found:
        th = 95
        if (pixel_is_black(img, y, x, threshold=th) or pixel_is_black(img, y - 1, x, threshold=th) or
                pixel_is_black(img, y - 2, x, threshold=th) or pixel_is_black(img, y + 1, x, threshold=th) or
                pixel_is_black(img, y + 2, x, threshold=th)):
            found = True
        else:
            x -= 1
    return x


def find_ref_x_left(img, x, y):
    found = False
    while not found:
        th = 95
        if (pixel_is_black(img, y, x, threshold=th) or pixel_is_black(img, y - 1, x, threshold=th) or
                pixel_is_black(img, y - 2, x, threshold=th) or pixel_is_black(img, y + 1, x, threshold=th) or
                pixel_is_black(img, y + 2, x, threshold=th)):
            found = True
        else:
            x += 1
    return x


def find_ref_y(img, x, y):
    x = 400
    y = 50
    found = False
    while not found:
        b = img[y][x][0]
        g = img[y][x][1]
        r = img[y][x][2]
        if b < 100 and g < 100 and r < 100:
            found = True
        else:
            y += 1
    return y


def pixel_is_black(img, y, x, threshold=0):
    b = img[y][x][0]
    g = img[y][x][1]
    r = img[y][x][2]
    return b <= threshold and g <= threshold and r <= threshold


def pixel_is_white(img, y, x):
    b = img[y][x][0]
    g = img[y][x][1]
    r = img[y][x][2]
    return b == 255 and g == 255 and r == 255


def pixel_is_red(img, y, x):
    b = img[y][x][0]
    g = img[y][x][1]
    r = img[y][x][2]
    return r > 220 and g < 180 and b < 180


def check_first_case(img, i, j):
    if (pixel_is_black(img, i + 1, j) and pixel_is_black(img, i, j + 1) and
            pixel_is_black(img, i + 1, j + 1) and
            pixel_is_white(img, i - 2, j - 2) and pixel_is_white(img, i - 2, j - 1) and
            pixel_is_white(img, i - 2, j) and pixel_is_white(img, i - 2, j + 1) and
            pixel_is_white(img, i - 2, j + 2) and pixel_is_white(img, i - 2, j + 3) and
            pixel_is_white(img, i - 1, j - 2) and pixel_is_white(img, i - 1, j + 3) and
            pixel_is_white(img, i, j - 2) and pixel_is_white(img, i, j + 3) and
            pixel_is_white(img, i + 1, j - 2) and pixel_is_white(img, i + 1, j + 3) and
            pixel_is_white(img, i + 2, j - 2) and pixel_is_white(img, i + 2, j + 3) and
            pixel_is_white(img, i + 3, j - 2) and pixel_is_white(img, i + 3, j + 3) and
            pixel_is_white(img, i + 3, j - 1) and pixel_is_white(img, i + 3, j) and
            pixel_is_white(img, i + 3, j + 1) and pixel_is_white(img, i + 3, j + 2)):
        return True
    else:
        return False


def check_second_case(img, i, j):
    if (pixel_is_black(img, i + 1, j) and pixel_is_black(img, i, j + 1) and
            pixel_is_black(img, i + 1, j + 1) and pixel_is_black(img, i, j + 2) and
            pixel_is_black(img, i + 1, j + 2) and
            pixel_is_white(img, i - 2, j - 2) and pixel_is_white(img, i - 2, j - 1) and
            pixel_is_white(img, i - 2, j) and pixel_is_white(img, i - 2, j + 1) and
            pixel_is_white(img, i - 2, j + 2) and pixel_is_white(img, i - 2, j + 3) and
            pixel_is_white(img, i - 1, j - 2) and pixel_is_white(img, i - 1, j + 4) and
            pixel_is_white(img, i, j - 2) and pixel_is_white(img, i, j + 4) and
            pixel_is_white(img, i + 1, j - 2) and pixel_is_white(img, i + 1, j + 4) and
            pixel_is_white(img, i + 2, j - 2) and pixel_is_white(img, i + 2, j + 4) and
            pixel_is_white(img, i + 3, j - 2) and pixel_is_white(img, i + 3, j + 3) and
            pixel_is_white(img, i + 3, j - 1) and pixel_is_white(img, i + 3, j) and
            pixel_is_white(img, i - 2, j + 4) and pixel_is_white(img, i + 3, j + 4) and
            pixel_is_white(img, i + 3, j + 1) and pixel_is_white(img, i + 3, j + 2)):
        return True
    else:
        return False


def check_third_case(img, i, j):
    if (pixel_is_black(img, i + 1, j) and pixel_is_black(img, i, j + 1) and
            pixel_is_black(img, i + 1, j + 1) and pixel_is_black(img, i + 2, j) and
            pixel_is_black(img, i + 2, j + 1) and
            pixel_is_white(img, i - 2, j - 2) and pixel_is_white(img, i - 2, j - 1) and
            pixel_is_white(img, i - 2, j) and pixel_is_white(img, i - 2, j + 1) and
            pixel_is_white(img, i - 2, j + 2) and pixel_is_white(img, i - 2, j + 3) and
            pixel_is_white(img, i - 1, j - 2) and pixel_is_white(img, i - 1, j + 3) and
            pixel_is_white(img, i, j - 2) and pixel_is_white(img, i, j + 3) and
            pixel_is_white(img, i + 1, j - 2) and pixel_is_white(img, i + 1, j + 3) and
            pixel_is_white(img, i + 2, j - 2) and pixel_is_white(img, i + 2, j + 3) and
            pixel_is_white(img, i + 3, j - 2) and pixel_is_white(img, i + 3, j + 3) and
            pixel_is_white(img, i + 4, j - 1) and pixel_is_white(img, i + 4, j) and
            pixel_is_white(img, i + 4, j - 2) and pixel_is_white(img, i + 4, j + 3) and
            pixel_is_white(img, i + 4, j + 1) and pixel_is_white(img, i + 4, j + 2)):
        return True
    else:
        return False


def to_bin_img(img):
    threshold = 125
    for i in range(HEIGHT):
        for j in range(WIDTH):
            b = img[i][j][0]
            g = img[i][j][1]
            r = img[i][j][2]
            if b < threshold and g < threshold and r < threshold:
                img[i][j] = [0, 0, 0]
            else:
                img[i][j] = [255, 255, 255]
    return img


def filter_red(img):
    height, width = img.shape[:2]
    for i in range(height):
        for j in range(width):
            if pixel_is_red(img, i, j):
                img[i][j] = [255, 255, 255]


def calculate_angle(img, start_x):
    h = 600
    x1 = find_ref_x_right(img, start_x, 1300)
    x2 = find_ref_x_left(img, start_x, 1300 + h)

    result = atan((x1 - x2) / h)
    return result


def fix_img_angle(img):
    # dividing height and width by 2 to get the center of the image
    height, width = img.shape[:2]
    # get the center coordinates of the image to create the 2D rotation matrix
    center = (width / 2, height / 2)

    # using cv2.getRotationMatrix2D() to get the rotation matrix
    agl = degrees(calculate_angle(img.copy(), img.shape[1] - 40))  # start_x here
    rotate_matrix = cv.getRotationMatrix2D(center=center, angle=agl, scale=1)

    # rotate the image using cv2.warpAffine
    return cv.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))


start_time = time.time()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print('Processing file ' + f + '...')
    origin = cv.imread(f)
    origin = fix_img_angle(origin)
    x = find_ref_x_right(origin, origin.shape[1] - 40, 1800) - 1085  # start_x here
    y = find_ref_y(origin, 400, 50) + 50
    img = origin[y:y + HEIGHT, x:x + WIDTH]
    filter_red(img)
    bin_img = to_bin_img(img.copy())
    sub = bin_img[round(HEIGHT / 2):HEIGHT, 0:WIDTH]

    for i in range(2, 26):
        for j in range(2, WIDTH - 4):
            if pixel_is_black(sub, i, j):
                if check_first_case(sub, i, j):
                    for x in range(4):
                        for y in range(4):
                            img[i + y + 44][j + x - 1] = [255, 255, 255]
                if check_second_case(sub, i, j):
                    for x in range(6):
                        for y in range(4):
                            img[i + y + 44][j + x - 1] = [255, 255, 255]
                if check_third_case(sub, i, j):
                    for x in range(4):
                        for y in range(6):
                            img[i + y + 44][j + x - 1] = [255, 255, 255]
            # if pixel_is_black(sub, i, j):
            #     print('(%d, %d)' % (j, i))

    cv.imwrite('processed\\' + filename, img)
end_time = time.time()
print("Took %f seconds" % (end_time - start_time))
