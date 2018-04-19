import os
import numpy as np
import sys

testing = 1

fileDir = os.path.join(sys.argv[1])
input_data = np.genfromtxt(fileDir, delimiter=',')
def scaling(X):
    return (X-X.mean())/X.std()
X = np.c_[np.ones(input_data.shape[0]), scaling(input_data[:, 0]), scaling(input_data[:,1])]
y = input_data[:, 2]
if testing: print(X)

alpha = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]
n_iter = 100

def lregression(X, y, n_iter=100, alpha=0.01):
    beta = [0, 0, 0]
    for _ in range(n_iter):
        beta -= alpha / X.shape[0] * np.dot((np.dot(beta, X.T)-y) , X)
    with open(sys.argv[2], 'a') as f:
        f.write("{},{},{},{},{}\n".format(alpha,n_iter,beta[0],beta[1],beta[2]))
    return

try:
    os.remove(sys.argv[2])
except:
    pass
for v in alpha:
    lregression(X, y, alpha=v, n_iter=n_iter)
lregression(X, y, alpha=0.03, n_iter=150)




