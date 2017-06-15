import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

# N is the number of trials
N = 10000
M = 0

# create an empty list to store the number of heads for each 10 throw trial
heads = []

# loop over trials
for i in range(N):
	
	# set number of heads in this trial to 0
	num_heads = 0
	
	# do ten coin flips
	for i in range(10):
		
		r = rand.rand()
		
		# if r > 0.5, we'll say this is a head
		if r > 0.5:
			num_heads += 1
	
	# append result for this trial to heads list
	heads.append(num_heads)

	# if the number heads is exactly 8, the trial is a success
	if num_heads == 8:
		M += 1

# print results, display histogram
print("Probability of exactly 8 heads in 10 tosses: ", M/N)

plt.hist(heads)
plt.show()
