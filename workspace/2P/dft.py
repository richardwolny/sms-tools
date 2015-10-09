import matplotlib.pyplot as plt
import numpy as np


N = 64
k0 = 7.5
# complex input signal,
# x = np.exp(1j * 2 * np.pi * k0 / N * np.arange(N))
# real signal,
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

nv = np.arange(-N/2, N/2)
kv = np.arange(-N/2, N/2)

X = np.array([])
for k in kv:
  s = np.exp(1j * 2 * np.pi * k / N * nv)
  X = np.append(X, sum(x * np.conjugate(s)))

y = np.array([])
for n in nv:
  s = np.exp(1j * 2 * np.pi * n / N * kv)
  y = np.append(y, 1.0 / N * sum(X*s))

plt.plot(kv, abs(X))
plt.axis([-N/2, N/2, 0, N])
plt.show()

plt.plot(nv, y)
plt.axis([-N/2, N/2-1, -1, 1])
plt.show()

