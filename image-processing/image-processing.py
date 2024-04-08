#!/usr/bin/python
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import random


def main():
    img = get_random_image()
    plot_color_histgram(img)


def naive_brighten(img, a):
    print(img[0, 0])
    result = cv2.add(img, a)
    print(result[0, 0])
    return result


def get_random_image():
    imgs = os.listdir("imgs/")
    return cv2.cvtColor(cv2.imread("imgs/" + random.choice(imgs)),
                        cv2.COLOR_BGR2RGB)


def plot_color_histgram(img):
    x, y, c = img.shape
    array = img.reshape(x * y, c)
    colors = ['red', 'green', 'blue']
    for i, c in enumerate(colors):
        plt.plot(np.arange(x*y), np.sort(array[:, i]), c=c)
    plt.show()


if __name__ == "__main__":
    main()
