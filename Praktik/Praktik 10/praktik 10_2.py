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

def save_image(img, n_colors, max_iter):
    dirname = 'K-means Compressor'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    filename = f'{dirname}/5-{n_colors}-colors-{max_iter}-iter.jpg'
    cv2.imwrite(filename, img)

filename = 'image5.jpg'
img = load_image(filename)

img_data = img.reshape((-1, 3))

# Количество цветов для сжатия
# n_colors_list = [2, 3, 4, 8, 16, 32, 64, 128, 256]
n_colors_list = [64]

# Максимальное количество итераций
# max_iter_list = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
max_iter_list = [300]

for n_colors in n_colors_list:
    start_time = time.time()
    for max_iter in max_iter_list:
        kmeans = KMeans(n_clusters=n_colors, max_iter=max_iter, random_state=0).fit(img_data)
        compressed_img_data = kmeans.cluster_centers_[kmeans.labels_]
        compressed_img_data = np.clip(compressed_img_data.astype('uint8'), 0, 255)
        compressed_img = compressed_img_data.reshape(img.shape)
        save_image(compressed_img, n_colors, max_iter)

        plt.imshow(compressed_img)
        plt.title(f'{n_colors} colors, {max_iter} iter')
        plt.show()
    end_time = time.time()
    print(f'{n_colors} colors: {end_time - start_time:.2f} seconds')