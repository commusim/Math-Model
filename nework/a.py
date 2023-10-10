import torch
import math

def generate_random_points_in_ring(inner_radius, outer_radius, num_points, device):
    # 生成随机极坐标角度
    theta = 2 * math.pi * torch.rand(num_points, device=device)
    # 生成随机半径在内圆和外圆之间
    r = (outer_radius - inner_radius) * torch.rand(num_points, device=device) + inner_radius
    # 将极坐标转换为直角坐标
    x = r * torch.cos(theta)
    y = r * torch.sin(theta)
    # 返回一个包含 x 和 y 张量的元组
    return x, y

# 创建一个GPU张量
device = torch.device("cuda")
inner_radius = 100
outer_radius = 350
num_points = 1

# 生成随机点，并将它们移到GPU上
random_points = generate_random_points_in_ring(inner_radius, outer_radius, num_points, device)
