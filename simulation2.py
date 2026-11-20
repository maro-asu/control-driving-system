import numpy as np
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Noto Sans CJK JP'

def simulate(Kd, Kv=0.8):
    T = 30.0
    dt = 0.01
    time = np.arange(0, T + dt, dt)
    N = len(time)

    d_ref = 30.0

    x_L = np.zeros(N)
    v_L = np.zeros(N)
    x_F = np.zeros(N)
    v_F = np.zeros(N)

    x_L[0] = 30.0
    x_F[0] = 0.0
    v_L[0] = 15.0
    v_F[0] = 15.0

    a_L = np.zeros(N)
    a_L[(time >= 10.0) & (time < 12.0)] = -2.0

    a_F = np.zeros(N)

    for k in range(N - 1):
        d = x_L[k] - x_F[k]
        e_d = d - d_ref
        e_v = v_L[k] - v_F[k]

        a_F[k] = Kd * e_d + Kv * e_v
        a_F[k] = np.clip(a_F[k], -3.0, 2.0)

        v_L[k + 1] = v_L[k] + a_L[k] * dt
        v_F[k + 1] = v_F[k] + a_F[k] * dt

        x_L[k + 1] = x_L[k] + v_L[k] * dt
        x_F[k + 1] = x_F[k] + v_F[k] * dt

    distance = x_L - x_F

    return time, distance, v_L, v_F, a_F


# 比較するゲイン
Kd_values = [0.1, 0.2, 0.4]

# 車間距離を比較
plt.figure(figsize=(9, 5))

for Kd in Kd_values:
    time, distance, v_L, v_F, a_F = simulate(Kd)

    plt.plot(
        time,
        distance,
        label=f"Kd = {Kd}"
    )

plt.axhline(
    30.0,
    linestyle="--",
    color="black",
    label="Desired Distance"
)

plt.xlabel("time [s]")
plt.ylabel("Distance [m]")
plt.title("Compared")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()