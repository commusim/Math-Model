import matplotlib.pyplot as plt

from back_excl import *
import numpy as np
import sklearn
from sklearn.cluster import KMeans


def AMPD(data):
    """
    实现AMPD算法
    :param data: 1-D numpy.ndarray
    :return: 波峰所在索引值的列表
    """
    p_data = np.zeros_like(data, dtype=np.int32)
    count = data.shape[0]
    arr_rowsum = []
    for k in range(1, count // 2 + 1):
        row_sum = 0
        for i in range(k, count - k):
            if data[i] > data[i - k] and data[i] > data[i + k]:
                row_sum -= 1
        arr_rowsum.append(row_sum)
    min_index = np.argmin(arr_rowsum)
    max_window_length = min_index
    for k in range(1, max_window_length + 1):
        for i in range(k, count - k):
            if data[i] > data[i - k] and data[i] > data[i + k]:
                p_data[i] += 1
    return np.where(p_data == max_window_length)[0]


peak = [[[], [], []],
        [[], [], []]]
threshold = [[[], [], []],
             [[], [], []]]
for i in range(2):
    # pic_f_env, ax = plt.subplots(1, 1, figsize=(16, 9))
    # ax.set_ylim(0, 2800)
    # ax.set_yticks(range(0, 2801, 400))
    for j in range(3):
        # ax.plot(range(3300), data_f_env[i][j], color=color[j])
        peak[i][j].append(AMPD(data_f_env[i][j]))
        data_tmp = data_f_env[i][j][peak[i][j]]
        threshold[i][j].append(KMeans(3, max_iter=1000, n_init="auto").fit(data_tmp[0].reshape(-1, 1)))
        # ax.scatter(peak[i][j], data_f_env[i][j][peak[i][j]], 100, color="black")
    # plt.savefig("pic/peak_%d" % i)
    # plt.show()


def getcolor(y, channel):
    color_classify = ["red", "green", "lightgray"]
    threshold = [[400, 2000],
                 [200, 1200],
                 [200, 1200]]
    if y < threshold[channel][0]:
        color = color_classify[2]
    elif y < threshold[channel][1]:
        color = color_classify[1]
    else:
        color = color_classify[0]
    return color


for pic in range(2):
    pic_p_f_env, ax = plt.subplots(1, 1, figsize=(16, 9))
    ax.set_ylim(0, 2800)
    ax.set_yticks(range(0, 2801, 400))
    for channel in range(3):
        pra_cla = threshold[pic][channel][0].labels_
        ax.plot(range(3300), data_f_env[pic][channel], color=color[channel])
        for classify in range(pra_cla.size):
            x = peak[pic][channel][0][classify]
            y = data_f_env[pic][channel][x]
            ax.scatter(x, y, 100, color=getcolor(y,channel))
    plt.savefig("pic/_classify_result_%d" % pic)
    plt.show()
