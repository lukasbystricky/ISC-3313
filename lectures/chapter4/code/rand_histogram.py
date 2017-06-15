import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# generate N uniformly distributed random points on [0,1]
N = 1000
X = rand.rand(N)

mu = np.average(X)
sigma2 = np.average((X - mu)**2)

print("mean: ", mu)
print("variance:", sigma2)

plt.hist(X)
plt.show()
