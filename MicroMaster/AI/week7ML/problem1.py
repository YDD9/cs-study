# https://www.youtube.com/watch?v=oLane_Vh3CU
# https://www.kdnuggets.com/2016/10/beginners-guide-neural-networks-python-scikit-learn.html
# http://www.cse.chalmers.se/~richajo/dit865/files/Perceptron%20example.html
import os
import numpy as np
import sys
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import Perceptron
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt
# from matplotlib import rcParams
# rcParams['figure.figsize'] = 10,5
# %matplotlib inline

testing = 1
# # load iris dataset
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target

fileDir = os.path.join(sys.argv[1])
with open(fileDir, 'r') as f:
    data = f.readlines()
if testing: print(data)

nb_samples = len(data)
X = np.empty((nb_samples, 2))
y = np.empty(nb_samples)
for i in range(nb_samples):
    X[i] = map(int, (data[i].split(','))[: -1])
    y[i] = int((data[i].split(','))[-1])
if testing: print("{}\n{}".format(X, y))

# test_size = 0.3
# random_state = 0

# X_train, X_test, y_train, y_test = train_test_split(X,
#                                                     y,
#                                                     test_size=test_size,
#                                                     random_state=random_state)

# sc = StandardScaler()
# sc.fit(X_train)

# X_train_std = sc.transform(X_train)
# X_test_std = sc.transform(X_test)

# print("Unique label:{}".format(np.unique(y)))

# n_iter = 40
# eta0 = 0.1

# ppn = Perceptron(n_iter=n_iter,
#                  eta0=eta0,
#                  random_state=random_state)

# ppn.fit(X_train_std,
#         y_train)
# print(ppn.get_params)

# y_pred = ppn.predict(X_test_std)

# print("accuracy: {:.2f}%".format(accuracy_score(y_test,y_pred)*100))

def predict(xi, W):
    intermediate = W[0] + np.dot(xi, W[1:])
    if intermediate > 0:
        return 1
    else:
        return -1


def int_perceptron(X, y, n_iter=40, eta=0.1):
    W = np.zeros(1+X.shape[1])
    temp = np.copy(W)
    errors_ = []
    for _ in range(n_iter):
        errors = 0
        for xi, target in zip(X, y):
            update = eta * (target - predict(xi,W))
            W[1:] += update * xi
            W[0] += update
            errors += int(update != 0.0)
        with open(sys.argv[2], 'a') as f:
            f.write("{},{},{}\n".format(W[1],W[2],W[0]))
        errors_.append(errors)
        if np.sum(np.equal(temp,W)) == W.shape[0]:
            break
        else:
            temp = np.copy(W)
    return W, errors_

# X = np.vstack([X_train_std, X_test_std])
# y = np.hstack([y_train, y_test])
try:
    os.remove(sys.argv[2])
except:
    pass
int_perceptron(X, y)




