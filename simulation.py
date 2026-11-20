import numpy as np
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Noto Sans CJK JP'

# シミュレーション条件
T = 30.0
dt = 0.01
time = np.arange(0, T + dt, dt)
N = len(time)

d_ref = 30.0

# 初期状態
x_L = np.zeros(N)
v_L = np.zeros(N)

x_F = np.zeros(N)
v_F = np.zeros(N)

x_L[0] = 30.0
x_F[0] = 0.0

v_L[0] = 15.0
v_F[0] = 15.0

# 先行車の加速度
a_L = np.zeros(N)

# 10秒後から12秒後まで減速
a_L[(time >= 10.0) & (time < 12.0)] = -2.0

# 追従車の加速度
a_F = np.zeros(N)

# 制御ゲイン
Kd = 0.2
Kv = 0.8

for k in range(N - 1):

    # 車間距離と誤差
    d = x_L[k] - x_F[k]
    e_d = d - d_ref

    # 速度差
    e_v = v_L[k] - v_F[k]

    # フィードバック制御
    a_F[k] = Kd * e_d + Kv * e_v

    # 加速度制限
    a_F[k] = np.clip(a_F[k], -3.0, 2.0)

    # 速度の更新
    v_L[k + 1] = v_L[k] + a_L[k] * dt
    v_F[k + 1] = v_F[k] + a_F[k] * dt

    # 位置の更新
    x_L[k + 1] = x_L[k] + v_L[k] * dt
    x_F[k + 1] = x_F[k] + v_F[k] * dt

# 車間距離
d = x_L - x_F

# グラフ1：車間距離
plt.figure()
plt.plot(time, d, label="Actual Distance")
plt.axhline(d_ref, linestyle="--", label="Desired Distance")
plt.xlabel("time [s]")
plt.ylabel("distance [m]")
plt.title("Change in Distance")
plt.grid()
plt.legend()
plt.show()

# グラフ2：速度
plt.figure()
plt.plot(time, v_L, label="Lead Velocity")
plt.plot(time, v_F, label="Following Velocity")
plt.xlabel("time [s]")
plt.ylabel("Velocity [m/s]")
plt.title("Change in Velocity")
plt.grid()
plt.legend()
plt.show()

# グラフ3：追従車の加速度
plt.figure()
plt.plot(time[:-1], a_F[:-1])
plt.xlabel("time [s]")
plt.ylabel("Following Acceleration [m/s^2]")
plt.title("Change in Acceleration")
plt.grid()
plt.show()
