# Input: numpy vector alpha of n rows, 1 column
# numpy matrix X of features, with n rows (samples), d columns (features)
# X[i,j] is the j-th feature of the i-th sample
# numpy vector y of labels, with n rows (samples), 1 column
# y[i] is the label (+1 or -1) of the i-th sample
# numpy vector z of d rows, 1 column
# Output: label (+1 or -1)

import K

def run(alpha,X,y,z):
	# Your code goes here
	label = 0
	n = len(X)
	sumval = 0
	for i in range(n):
		sumval += alpha[i] * y[i] * K.run(X[i], z)
	if(sumval > 0):
		label = 1
	else:
		label = -1
	return label