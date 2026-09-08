import matplotlib
matplotlib.use('Agg')  # Chuyển backend sang chế độ không GUI để chạy mượt trên WSL/Linux

import numpy as np
import matplotlib.pyplot as plt

# 1. Khởi tạo tham số thời gian và tần số
t = np.linspace(0, 10, 1000)
gamma = 0.5            # Hệ số dập tắt
omega = 2 * np.pi * 1.0 # Tần số góc

# 2. Công thức dao động dập tắt: x(t) = e^(-gamma * t) * cos(omega * t)
x = np.exp(-gamma * t) * np.cos(omega * t)

# 3. Vẽ đồ thị
plt.figure(figsize=(10, 6))
plt.plot(t, x, label=r'$x(t) = e^{-\gamma t} \cos(\omega t)$', color='blue', linewidth=2)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title('Mo phong Dao dong Dap tat (Damped Harmonic Oscillation)', fontsize=14)
plt.xlabel('Thoi gian t (s)', fontsize=12)
plt.ylabel('Li do x(t)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=12)

# 4. Xuất đồ thị ra file ảnh .png
plt.savefig('damped_oscillation_plot.png', dpi=300)
print("Đã thực thi thành công và xuất file ảnh damped_oscillation_plot.png!")