import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import time

def load_image(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def save_image(img, n_colors):
    dirname = 'Scikit Compressor'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    filename = f'{dirname}/2-{n_colors}-colors.jpg'
    cv2.imwrite(filename, img)

filename = 'image2.jpg'
img = load_image(filename)

img_data = img.reshape((-1, 3))

n_colors_list = [2, 3, 4, 8, 16, 32, 64, 128, 256]

for n_colors in n_colors_list:
    start_time = time.time()
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(img_data)
    compressed_img_data = kmeans.cluster_centers_[kmeans.labels_]
    compressed_img_data = np.clip(compressed_img_data.astype('uint8'), 0, 255)
    compressed_img = compressed_img_data.reshape(img.shape)
    save_image(compressed_img, n_colors)
    end_time = time.time()

    print(f'{n_colors} colors: {end_time - start_time:.2f} seconds')

    plt.imshow(compressed_img)
    plt.title(f'{n_colors} colors')
    plt.show()