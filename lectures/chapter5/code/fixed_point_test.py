import numpy as np

def fixed_point(x0, f, max_it = 100, tol = 1e-8):

	x1 = np.cos(x0)
	k = 0 # iteration number

	while abs(x0 - x1) > tol and k < max_it:
		
		# set x0 to x1 (x0 is x_k)
		x0 = x1
		
		# compute x_{k+1} from x_k, store in x1
		x1 = np.cos(x0)
		
		# increment counter 
		k += 1

	return (x1, k)
	
	
f = lambda x: np.cos(x)
(x,k) = fixed_point(0, f)

print("x=",x,"after",k,"iterations")
