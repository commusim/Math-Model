import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

excel_file = ["大米数据1.xls", "大米数据2.xls", "背景数据.xls"]
data = [pd.read_excel(excel_file[0]), pd.read_excel(excel_file[1]), pd.read_excel(excel_file[2])]

color = ["red", "green", "blue"]


def draw(RGB_data, address):
    RGB_color = ["red", "green", "blue"]
    pic, ax = plt.subplots(1, 1, figsize=(16, 9))
    ax.set_ylim(0, 2100)
    ax.set_yticks(range(0, 2101, 300))
    for _ in range(3):
        test = RGB_data[_]
        ax.plot(range(3300), test, color=RGB_color[_])
    # plt.show()
    plt.savefig(address)


if __name__ == "__main__":
    # 绘制初始图像数据
    for i in range(3):
        pic_ori, ax = plt.subplots(1, 1, figsize=(16, 9))
        ax.set_ylim(0, 2100)
        ax.set_yticks(range(0, 2101, 300))
        for j in range(3):
            test = data[i][color[j]]
            ax.plot(range(3300), test, color=color[j])
        plt.show()
        # plt.savefig("pic/origin_%d" % i)

    # 绘制去背景图像数据
    for i in range(2):
        pic_back_excl, ax = plt.subplots(1, 1, figsize=(16, 9))
        ax.set_ylim(0, 2100)
        ax.set_yticks(range(0, 2101, 300))
        for j in range(3):
            back_excl = data[i][color[j]] - data[2][color[j]]
            ax.plot(range(3300), back_excl, color=color[j])
        plt.show()
        # plt.savefig("pic/back_excl_%d" % i)
