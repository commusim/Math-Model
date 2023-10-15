from drawpic import draw
from fliter import wavelet_noising
import pywt
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

excel_file = ["大米数据1.xls", "大米数据2.xls", "背景数据.xls"]
data = [pd.read_excel(excel_file[0]), pd.read_excel(excel_file[1]), pd.read_excel(excel_file[2])]
color = ["red", "green", "blue"]

back_excl = [data[0] - data[2], data[1] - data[2]]
data_f_env = [[wavelet_noising(back_excl[0]["red"]),
               wavelet_noising(back_excl[0]["green"]),
               wavelet_noising(back_excl[0]["blue"])],
              [wavelet_noising(back_excl[1]["red"]),
               wavelet_noising(back_excl[1]["green"]),
               wavelet_noising(back_excl[1]["blue"])
               ]]
if __name__ == "__main__":
    for _ in range(2):
        draw(data_f_env[_], "pic/excel_filter_%d" % _, 0)
