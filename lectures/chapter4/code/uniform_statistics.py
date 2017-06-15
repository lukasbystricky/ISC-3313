import numpy as np

# define endpoints
b = 0.3
a = 0.2

# compute pdf, this is the same at all x values between a and b
pdf = 1/(b - a)

# create a grid of points using linspace
N = 32
x = np.linspace(0.23, 0.27, N + 1)
h = (0.27 - 0.23)/N

# compute probability using lef Riemann sum
p = 0
for i in range(N):
	p += h*pdf

print("probability:", p)
