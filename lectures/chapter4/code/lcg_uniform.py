# initialize seed, a, b and m
seed = 0
a=1664525
b=1013904223
m=2**32

# N is the number of random numbers
N = 10000

# initialize list and compute first pseudo-random number from seed
X = [(a*seed + b) % m]

# apply reccurence relation
for i in range(N):
    X.append((a*X[i] + b) % m)

# divide everything by m to get all numbers in the range [0,1]
X = [r/m for r in X]

# compute mean
mu = 0 
for i in range(N):
	mu += X[i]/N
	
# compute variance
sigma2 = 0
for i in range(N):
	sigma2 += (X[i] - mu)**2/N
	
print("mean: ", mu)
print("variance: ", sigma2)
