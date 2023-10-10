# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

people = [5.42, 5.52, 5.63, 5.74, 5.87, 6.02, 6.14, 6.28, 6.46, 6.59,
          6.72, 6.62, 6.58, 6.72, 6.91, 7.04, 7.25, 7.45, 7.63, 7.85,
          8.06, 8.29, 8.52, 8.71, 8.92, 9.08, 9.24, 9.37, 9.49, 9.62,
          9.75, 9.87, 10.00, 10.16, 10.30, 10.43, 10.58, 10.75, 10.93, 11.10,
          11.27, 11.43, 11.58, 11.71, 11.85, 11.98, 12.11, 12.25, 12.36, 12.47,
          12.57, 12.67, 12.76, 12.84, 12.92, 12.99, 13.07, 13.14, 13.21, 13.28,
          13.34, 13.40, 13.47, 13.54, 13.60, 13.67, 13.74, 13.82, 13.90, 13.95,
          14.00, 14.11, 14.12, 14.11]
people = np.array(people)
years = np.arange(1949, 2023)


# 定义logistic回归模型
def logistic_increase_function(t, K, r):
    # t:time   t_0:initial time    P_0:initial_value    K:capacity  r:increase_rate
    P_0 = people[0]
    t_0 = years[0]
    exp_value = np.exp(r * (t - t_0))
    return (K * exp_value * P_0) / (K + (exp_value - 1) * P_0)


# 最小二乘法回归参数并进行预测
[popt, pcov] = curve_fit(logistic_increase_function, years, people)
predict = logistic_increase_function(2023, popt[0], popt[1])

# 将预测数据进行可视化展现
people = np.append(people, predict)
years = np.append(years, 2023)
fig, ax = plt.subplots(1, 1)
ax.plot(years, people)
ax.plot(2023, predict, marker='.')
ax.set_xlabel("years", fontstyle='italic')
ax.set_ylabel("people", fontstyle='oblique')
plt.savefig("logistic")
fig.show()
