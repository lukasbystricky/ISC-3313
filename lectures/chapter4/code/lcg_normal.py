import numpy as np

# initialize seed, a, b and m
seed_x = 0
seed_y = 1
a=1664525
b=1013904223
m=2**32

# N is the number of random numbers
N = 10000

# initialize lists and compute first pseudo-random number from seed

X = [(a*seed_x + b) % m]
Y = [(a*seed_y + b) % m]

# apply reccurence relation
for i in range(N):
    X.append((a*X[i] + b) % m)
    Y.append((a*Y[i] + b) % m)

# divide everything by m to get all numbers in the range [0,1]
X = [r/m for r in X]
Y = [r/m for r in Y]

# create normal distribution
Z = []
for i in range(N):
    Z.append(np.sqrt(-2*np.log(X[i]))*np.cos(2*np.pi*Y[i]))
    Z.append(np.sqrt(-2*np.log(X[i]))*np.sin(2*np.pi*Y[i]))

# compute mean
mu = 0
for i in range(2*N): # we've created 2N normaly distributed points
	mu += Z[i]/(2*N)
	
# compute variance
sigma2 = 0
for i in range(2*N):
	sigma2 += (Z[i] - mu)**2/(2*N)
	
print("mean: ", mu)
print("variance: ", sigma2)
