import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
from func import lamprey
from config import T, y0, params, t

lamprey_solution = solve_ivp(lamprey, (0, T), y0, args=(params,), t_eval=t)

t = lamprey_solution.t
y = lamprey_solution.y.T

print("Value of variables at the last t:")
labels = ['C', 'Fast', 'Slow', 'F', 'M', 'O', 'E']
for label, value in zip(labels, y[-1]):
    print(f"{label}: {value}")

plt.plot(t, y[:, 0], 'b', label='C')
plt.plot(t, y[:, 1], 'r', label='Fast')
plt.plot(t, y[:, 2], 'g', label='Slow')
plt.plot(t, y[:, 3], 'y', label='F')
plt.plot(t, y[:, 4], 'c', label='M')
plt.plot(t, y[:, 5], 'm', label='O')
plt.plot(t, y[:, 6], 'k', label='E')
plt.legend()
plt.show()