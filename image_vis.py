import os
import glob
import matplotlib.pyplot as plt
import cv2


def show_images(images, titles=None, row=4, col=4):
    fig, ax = plt.subplots(nrows=row, ncols=col)
    for r in range(row):
        for c in range(col):
            ax[r, c].imshow(images[r*row + c])
            if titles:
                ax[r, c].set_title(titles[r*row + c])
            ax[r, c].axis('off')
    plt.show()


if __name__ == '__main__':
    path = '/home/tuannam/Downloads/data/facereg/lfw'
    images_path = glob.glob('/home/tuannam/Downloads/data/facereg/lfw/**/*.jpg')
    images = []
    titles = []
    for i in range(16):
        image = cv2.imread(images_path[i])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        images.append(image)
        titles.append(str(i + 1))

    show_images(images, titles)