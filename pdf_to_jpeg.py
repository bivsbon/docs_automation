# import module
from pdf2image import convert_from_path
import os

counter = 1


def convert_all(path):
    global counter
    if os.path.isdir(path):
        for filename in os.listdir(path):
            new_path = os.path.join(path, filename)
            convert_all(new_path)
    else:
        images = convert_from_path(path, poppler_path=r'poppler-22.11.0/Library/bin')

        for i in range(len(images)):
            # Save pages as images in the pdf
            images[i].save('img_kh\\' + str(counter) + '.jpg', 'JPEG')
            print(counter)
            counter += 1


def main():
    convert_all('pdf')


if __name__ == "__main__":
    main()
