import numpy as np

# define mean and variance
mu = 0.25
sigma2 = 0.0001

# create grid between 0.23 and 0.27 with N points
N = 128
x = np.linspace(0.23, 0.27, N + 1)
h = (0.27 - 0.23)/N

# compute left Riemann sum
p = h*np.sum(1/np.sqrt(2*np.pi*sigma2)*np.exp(-(x[:-1] - mu)**2/(2*sigma2)))

print("probability: ", p)
