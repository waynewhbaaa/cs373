# Input: number of iterations L
# numpy matrix X of features, with n rows (samples), d columns (features)
# X[i,j] is the j-th feature of the i-th sample
# numpy vector y of labels, with n rows (samples), 1 column
# y[i] is the label (+1 or -1) of the i-th sample
# Output: numpy vector theta of d rows, 1 column
import numpy as np


def run(L,X,y):
    # Your code goes here
    n = len(X)
    d = len(X[0])
    theta = np.zeros((d,1))
    for i in range(1,L+1):
        for t in range(n):
            if (y[t]*(np.dot(X[t], theta))) <= 0:
                for k in range (d):
                    theta[k] = theta[k] + y[t] * X[t][k]
    return theta
