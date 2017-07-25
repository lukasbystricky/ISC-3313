from geneticAlgorithm import ga
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 8*x[0]**2 + x[1]**2
N = 1000

err = []

for max_generations in range(20):
    np.random.seed(111)
    (generations,x_opt) = ga(f, -4, 4, -4, 4, N, max_generations)
    
    err.append(f(x_opt))
    
plt.semilogy(err)
plt.xlabel("Generation number")
plt.ylabel("Error in optimal function value")
plt.show()
