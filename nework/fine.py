import numpy as np
from math import *

D = [-59, -28, 0, 31, 61, 92, 122, 153, 184, 214, 245, 275]
times = [9, 10.5, 12, 13.5, 15]


def DNI(month, time):
    a, b, c = 0.34981, 0.5783875, 0.275745
    sin_rou = sin((2 * pi * D[month - 1]) / 365) * sin((2 * pi * 23.45) / 360)
    omiga = (pi / 12) * (time - 12)
    sin_as = sqrt(1 - sin_rou ** 2) * cos((39.4 / 180) * pi) * cos(omiga) + sin_rou * sin((39.4 / 180) * pi)
    result = 1.366 * (a + b * exp(-c / sin_as))
    return result




def eta(x, y, z, month, time):
    z=84-z
    sin_rou = sin((2 * pi * D[month - 1]) / 365) * sin((2 * pi * 23.45) / 360)
    omiga = (pi / 12) * (time - 12)
    sin_as = sqrt(1 - sin_rou ** 2) * cos((39.4 / 180) * pi) * cos(omiga) + sin_rou * sin((39.4 / 180) * pi)
    as_ = asin(sin_as)
    phi = 39.4 * pi / 180
    cos_gamma = (sin_rou - sin_as * sin(phi)) / abs(cos(as_) * cos(phi))
    gamma_ = acos(cos_gamma)
    eta_sb = 0.98 + np.random.rand() / 50 - 0.01
    eta_trunc = 0.85 + np.random.rand() / 50 - 0.01
    eta_ref = 0.72

    vecor_i = [-cos(as_) * sin(gamma_), -cos(as_) * cos(gamma_), -sin(as_)]

    x1,y1,z1= -x/sqrt(x**2+y**2+z**2)-vecor_i[0],-y/sqrt(x**2+y**2+z**2)-vecor_i[1],-z/sqrt(x**2+y**2+z**2)-vecor_i[2]

    vecor_n = [x1/sqrt(x1**2+y1**2+z1**2),y1/sqrt(x1**2+y1**2+z1**2),z1/sqrt(x1**2+y1**2+z1**2)]
    eta_cos = (vecor_n[0]*vecor_i[0]+vecor_n[1]*vecor_i[1]+vecor_n[2]*vecor_i[2])
    eta_at = 0.99321 - 0.001176*sqrt(x**2+y**2+z**2) + 1.97E-8*(x**2+y**2+z**2)
    return eta_sb,eta_trunc,eta_at,eta_cos,eta_ref


A = eta(107.25,11.664,8,1,9)
print(A)