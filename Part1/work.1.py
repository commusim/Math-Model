import matplotlib.pyplot as plt
import numpy as np
import math

D_x = np.arange(0, 2, 0.001)
N_m = 10
r = 10
N_0 = 50
y_N = []
for t in D_x:
    N_result = N_m / (1 + (N_m / N_0 - 1 ) * math.exp(-r * t))
    y_N.append(N_result)
fig, ax = plt.subplots(1, 1)
ax.plot(D_x, y_N)
ax.set_xlabel("t", fontstyle='italic')
ax.set_ylabel("N(t)", fontstyle='oblique')
plt.savefig("work(1)")
fig.show()

