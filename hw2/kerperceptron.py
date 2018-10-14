# Input: number of iterations L
# numpy matrix X of features, with n rows (samples), d columns (features)
# X[i,j] is the j-th feature of the i-th sample
# numpy vector y of labels, with n rows (samples), 1 column
# y[i] is the label (+1 or -1) of the i-th sample
# Output: numpy vector alpha of n rows, 1 column
import numpy as np
import math
import K

def run(L,X,y):
	# Your code goes here
	n = len(X)
	d = len(X[0])
	alpha = np.zeros(n)
	
	for iter in range(1,L+1):
		for t in range(n):
			sumval = sumK(alpha, X, y, t, n)
			if(y[t] * sumval <= 0):
				alpha[t] += 1
	return alpha
	
def sumK(alpha, X, y, t, n):
	sumval = 0
	for i in range(n):
		sumval += alpha[i] * y[i] * K.run(X[i],X[t]) 
	return sumval