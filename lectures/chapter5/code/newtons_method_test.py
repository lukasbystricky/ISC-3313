import numpy as np

def newton_step(x0, f, df):
    return x0 - f(x0)/df(x0)
    
def newtons_method(x0, f, df, tol=1e-5, max_it=20):

    # intitialize iteration counter to 0
    icount = 0

    # intitialize diff to be some number bigger than TOL
    diff = 2*tol

    # loop
    while (f(x0) > tol or diff > tol) and icount < max_it:
        
        # call newton_step defined earlier
        x1 = newton_step(x0, f, df)
    
        diff = abs(x0 - x1)
        x0 = x1
        icount = icount + 1
        
    return (x1, icount)
    
## test of x - cos(x) = 0

f = lambda x : x - np.cos(x)
df = lambda x: 1 + np.sin(x)

(x,k) = newtons_method(0, f, df)

print("x=", x,"after",k,"iterations")
