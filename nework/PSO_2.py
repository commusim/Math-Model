import numpy as np
import matplotlib.pyplot as plt
import torch
from mpl_toolkits.mplot3d import Axes3D



# 定义内圆和外圆的半径以及生成的样本点数量
inner_radius = 100
outer_radius = 350


# num_points = 1000


def generate_random_points_in_ring(inner_radius, outer_radius, num_points):
    # 生成随机极坐标角度
    theta = 2 * np.pi * np.random.rand(num_points)

    # 生成随机半径在内圆和外圆之间
    r = np.sqrt(np.random.uniform(inner_radius ** 2, outer_radius ** 2, num_points))

    # 将极坐标转换为直角坐标
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y


def fit_fun(x):  # 适应函数
    return 100.0 * (x[0] ** 2 + x[1] ** 2)


class Particle():
    # 初始化
    def __init__(self, x_max, max_vel, dim):
        # 二维位置信息
        self.__pos = generate_random_points_in_ring(inner_radius, outer_radius, 1)
        # 其他维度信息
        self.__siz = np.random.uniform(-x_max, x_max, (1, dim - 1))  # 粒子的位置

        self.__vel = np.random.uniform(-max_vel, max_vel, (1, dim))  # 粒子的速度
        self.__bestPos = np.zeros((1, dim))  # 粒子最好的位置
        self.__fitnessValue = fit_fun(self.__pos)  # 适应度函数值

    def set_pos(self, value):
        self.__pos = value

    def get_pos(self):
        return self.__pos

    def set_siz(self, value):
        self.__pos = value

    def get_siz(self):
        return self.__siz

    def set_best_pos(self, value):
        self.__bestPos = value

    def get_best_pos(self):
        return self.__bestPos

    def set_vel(self, value):
        self.__vel = value

    def get_vel(self):
        return self.__vel

    def set_fitness_value(self, value):
        self.__fitnessValue = value

    def get_fitness_value(self):
        return self.__fitnessValue


class PSO:
    def __init__(self, dim, size, iter_num, x_max, max_vel, tol, best_fitness_value=float('Inf'), C1=2, C2=2,
                 W=1):  # C1 C2是学习参数
        self.C1 = C1
        self.C2 = C2
        self.W = W
        self.dim = dim  # 粒子的维度
        self.size = size  # 粒子个数
        self.iter_num = iter_num  # 迭代次数
        self.x_max = x_max
        self.max_vel = max_vel  # 粒子最大速度
        self.tol = tol  # 截至条件
        self.best_fitness_value = best_fitness_value
        self.best_position = np.zeros((1, dim))  # 种群最优位置
        self.fitness_val_list = []  # 每次迭代最优适应值

        # 对种群进行初始化
        self.Particle_list = [Particle(self.x_max, self.max_vel, self.dim) for i in range(self.size)]

    def set_bestFitnessValue(self, value):
        self.best_fitness_value = value

    def get_bestFitnessValue(self):
        return self.best_fitness_value

    def set_bestPosition(self, value):
        self.best_position = value

    def get_bestPosition(self):
        return self.best_position


def train(totals):
    # 更新速度
    def update_vel(totals, part):
        vel_value = totals.W * part.get_vel() + totals.C1 * np.random.rand() * (part.get_best_pos() - part.get_pos()) \
                    + totals.C2 * np.random.rand() * (totals.get_bestPosition() - part.get_pos())
        vel_value[vel_value > totals.max_vel] = totals.max_vel
        vel_value[vel_value < -totals.max_vel] = -totals.max_vel
        part.set_vel(vel_value)

    # 更新位置
    def update_pos(totals, part):
        pos_value = part.get_pos() + part.get_vel()  # 更新位置
        part.set_pos(pos_value)  # 存储位置
        value = fit_fun(part.get_pos())
        if value < part.get_fitness_value():
            part.set_fitness_value(value)
            part.set_best_pos(pos_value)
        if value < totals.get_bestFitnessValue():
            totals.set_bestFitnessValue(value)
            totals.set_bestPosition(pos_value)

    for i in range(totals.iter_num):
        for part in totals.Particle_list:
            update_vel(totals, part)  # 更新速度
            update_pos(totals, part)  # 更新位置
        totals.fitness_val_list.append(totals.get_bestFitnessValue())  # 每次迭代完把当前的最优适应度存到列表
        print('第{}次最佳适应值为{}'.format(i, totals.get_bestFitnessValue()))
        if totals.get_bestFitnessValue() < totals.tol:
            break
    return totals.fitness_val_list, totals.get_bestPosition()


# test 香蕉函数
pso = PSO(1, 100, 10000, 30, 60, 1e-4, C1=2, C2=2, W=1)

fig1, ax1 = plt.subplots(1, 1, figsize=(7, 7))
for i in range(pso.size):
    x = pso.Particle_list[i].get_pos()[0]
    y = pso.Particle_list[i].get_pos()[1]
    ax1.scatter(x, y)
plt.show()

fit_var_list, best_pos = train(pso)
print("最优位置:" + str(best_pos))
print("最优解:" + str(fit_var_list[-1]))

test = pso.Particle_list[0].get_pos()

fig2, ax2 = plt.subplots(1, 1, figsize=(7, 7))
for i in range(pso.size):
    x = pso.Particle_list[i].get_pos()[0]
    y = pso.Particle_list[i].get_pos()[1]
    ax2.scatter(x, y)
plt.show()
