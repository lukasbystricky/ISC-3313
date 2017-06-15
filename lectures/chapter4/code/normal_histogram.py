import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# generate N samples from normal distribution with mean 4 and 
# standard deviation 2
N = 1000
X = rand.normal(4, 2, N) 

mu = np.average(X)
sigma2 = np.average((X - mu)**2)

print("mean: ", mu)
print("variance:", sigma2)

plt.hist(X)
plt.show()
