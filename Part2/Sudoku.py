import numpy as np
import matplotlib.pyplot as plt
import time
from function import *

num_map = np.array([[8, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 6, 0, 0, 0, 0, 0],
                    [0, 7, 0, 0, 9, 0, 2, 0, 0],
                    [0, 5, 0, 0, 0, 7, 0, 0, 0],
                    [0, 0, 0, 0, 4, 5, 7, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 3, 0],
                    [0, 0, 1, 0, 0, 0, 0, 6, 8],
                    [0, 0, 8, 0, 0, 0, 0, 1, 0],
                    [0, 9, 0, 0, 0, 0, 4, 0, 0]])
maps = np.zeros((9, 9, 9))
init(num_map, maps)

print(maps)
