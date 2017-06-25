import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# generate data
x = []
y = []

x.append(0.1)
y.append(0.05)

h = 0.1
N = 10000
for i in range(1,N+1):
	x.append(x[i-1] - h*np.sin(y[i-1] + np.tan(3*y[i-1])))
	y.append(y[i-1] - h*np.sin(x[i-1] + np.tan(3*x[i-1])))

# initialize plot
fig, ax = plt.subplots()
ax.set_xlim((min(x) - 0.1, max(x) + 0.1))
ax.set_ylim((min(y) - 0.1, max(y) + 0.1))

data_line, = ax.plot(x[0],y[0])
ax.set_title("t = %4d" % 0)

# define update function
def update_frame(i):
	data_line.set_data(x[:i], y[:i])
	ax.set_title("t = %4d" % i)
	
anim = FuncAnimation(fig, update_frame, frames = np.arange(0,N,10))
anim.save("orbit_fractal.gif", writer="imagemagick", fps=30)
