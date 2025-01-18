import numpy as np

# Initial condition
y0 = [10, 10, 10, 10, 10, 4000, 1000]

# Parameters
params = {
    'T_HP': 275,
    'T_MP': 90,

    'K_upstream': 5000,
    'K_downstream': 5000,

    'p_E_to_E': 1 - 1/30,
    'p_E_to_C': 1/30 - 0.01,

    'p_C_to_C': 0.999,
    'p_C_to_Fast': 0.0004,
    'p_C_to_Slow': 0.0005,

    'p_Fast_to_Fast': 0.99,
    'p_Slow_to_Slow': 0.99,

    'p_Fast_to_F': 0.009,
    'p_Slow_to_M': 0.009,

    'p_F_to_D': 0.1,
    'p_M_to_D': 0.1,

    'r_O': 0.001,

    'alpha': 0.00001,
    'mu': 1000,
    'beta': 1,
    'gamma': 0.002,
}

# Compute trajectory
dt = 0.01
T = 40000
num_time_pts = int(T / dt)
t = np.linspace(0, T, num_time_pts)