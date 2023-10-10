import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# 定义均值和协方差矩阵
mean = [0, 0, 0]
cov = [[1, 0.5, 0.2],
       [0.5, 1, 0.3],
       [0.2, 0.3, 1]]

# 创建三维高斯正态分布
rv = multivariate_normal(mean, cov)

# 生成三维坐标网格
x, y, z = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
pos = np.dstack((x, y, z))

# 计算概率密度
pdf = rv.pdf(pos)
density = pdf

# 创建画布
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维高斯正态分布的等密度曲面
ax.contourf(x, y, z, density, cmap='viridis', levels=20)

# 绘制两个立方体
cube1 = plt.matplotlib.patches.Rectangle((-0.5, -0.5, -0.5), 1, 1, 1, linewidth=1, edgecolor='r', facecolor='none', label='Small Cube')
cube2 = plt.matplotlib.patches.Rectangle((-1, -1, -1), 2, 2, 2, linewidth=1, edgecolor='b', facecolor='none', label='Large Cube')

# 添加立方体到图中
ax.add_patch(cube1)
ax.add_patch(cube2)

# 设置图例
ax.legend(handles=[cube1, cube2])

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.title('三维高斯正态分布与立方体')
plt.grid(True)
plt.axis('equal')
plt.show()
