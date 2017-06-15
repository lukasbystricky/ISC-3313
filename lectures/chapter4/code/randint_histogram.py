import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# generate N random integers in the range 0 to 10
N = 1000
X = rand.randint(0, 11, N) 

mu = np.average(X)
sigma2 = np.average((X - mu)**2)

print("mean: ", mu)
print("variance:", sigma2)

# histogram with bins 0,1,2,...,10,11
plt.hist(X, np.arange(0,12))
plt.show()
