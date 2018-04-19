import os
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
# from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
# http://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#sphx-glr-auto-examples-svm-plot-rbf-parameters-py
# cross-validation + training test + consider StratifiedShuffleSplit avoid bias y
# https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6

"""
http://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html
As we have seen, every estimator exposes a score method that can judge the quality of the fit (or the prediction) on new data. Bigger is better.

>>>
>>> from sklearn import datasets, svm
>>> digits = datasets.load_digits()
>>> X_digits = digits.data
>>> y_digits = digits.target
>>> svc = svm.SVC(C=1, kernel='linear')
>>> svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
0.97999999999999998

http://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html#grid-search
>>> from sklearn.model_selection import GridSearchCV, cross_val_score
>>> Cs = np.logspace(-6, -1, 10)
>>> clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs),
...                    n_jobs=-1)
>>> clf.fit(X_digits[:1000], y_digits[:1000])
GridSearchCV(cv=None,...
>>> clf.best_score_  # scores on the train set ??
0.925...
>>> clf.best_estimator_.C
0.0077...

>>> # Prediction performance on test set is not as good as on train set
>>> clf.score(X_digits[1000:], y_digits[1000:])
0.943...

By default, the GridSearchCV uses a 3-fold cross-validation. However, if it detects that a classifier is passed, rather than a regressor, it uses a stratified 3-fold.

Nested cross-validation

>>>
>>> cross_val_score(clf, X_digits, y_digits)
...
array([ 0.938...,  0.963...,  0.944...])
"""
testing = 1

fileDir = os.path.join(os.getcwd(), 'MicroMaster', 'AI', 'week7ML', 'input3.csv')
input_data = np.genfromtxt(fileDir, delimiter=',', skip_header=1)
X = input_data[:, :2]
y = input_data[:, 2]
if testing: print(X)

test_size = 0.4
random_state = 0
n_splits = 5
cv = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)

# SVM with Linear Kernel
# https://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel
# https://stats.stackexchange.com/questions/73032/linear-kernel-and-non-linear-kernel-for-support-vector-machine
"""kernel : string, optional (default=’rbf’)

Specifies the kernel type to be used in the algorithm. It must be one of ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or a callable. If none is given, ‘rbf’ will be used. If a callable is given it is used to pre-compute the kernel matrix from data matrices; that matrix should be an array of shape (n_samples, n_samples)."""

kernel = 'linear'
C = [0.1, 0.5, 1, 5, 10, 50, 100]
param_grid = dict(C=C)
grid = GridSearchCV(SVC(kernel=kernel), param_grid=param_grid, cv=cv)

grid.fit(X, y)
test_score = []
for train, test in cv.split(X,y):
    test_score.append(grid.score(X[test], y[test]))
print("The best parameters are %s with a score of %0.2f, with a std test score of %0.2f"
      % (grid.best_params_, grid.best_score_, np.mean(test_score)))
# The best parameters are {'C': 0.1} with a score of 0.59, with a std test score of 0.59

# # SVM with Polynomial Kernel
# kernel = 'poly'
# C = [0.1, 1, 3]
# degree = [4, 5, 6]
# gamma = [0.1, 0.5]
# param_grid = dict(C=C, degree=degree, gamma=gamma)
# grid = GridSearchCV(SVC(kernel=kernel), param_grid=param_grid, cv=cv)

# grid.fit(X, y)
# print("The best parameters are %s with a score of %0.2f, with a std test score of %0.2f"
#       % (grid.best_params_, grid.best_score_, np.mean(test_score)))

# SVM with RBF Kernel
kernel = 'rbf'
C = [0.1, 0.5, 1, 5, 10, 50, 100]
gamma = [0.1, 0.5, 1, 3, 6, 10]
param_grid = dict(C=C, gamma=gamma)
grid = GridSearchCV(SVC(kernel=kernel), param_grid=param_grid, cv=cv)

grid.fit(X, y)
print("The best parameters are %s with a score of %0.2f, with a std test score of %0.2f"
      % (grid.best_params_, grid.best_score_, np.mean(test_score)))
# The best parameters are {'C': 50, 'gamma': 1} with a score of 0.95

# Logistic Regression
C = [0.1, 0.5, 1, 5, 10, 50, 100]
param_grid = dict(C=C)
grid = GridSearchCV(LogisticRegression(), param_grid=param_grid, cv=cv)

grid.fit(X, y)
print("The best parameters are %s with a score of %0.2f, with a std test score of %0.2f"
      % (grid.best_params_, grid.best_score_, np.mean(test_score)))
# The best parameters are {'C': 5} with a score of 0.58

# # k-Nearest Neighbors
# kernel = 'knn'
# n_neighbors =  range(1,51)
# leaf_size = range(5, 65, 5)
# param_grid = dict(n_neighbors=n_neighbors, leaf_size=leaf_size)
# grid = GridSearchCV(SVC(kernel=kernel), param_grid=param_grid, cv=cv)

# grid.fit(X, y)
# print("The best parameters are %s with a score of %0.2f, with a std test score of %0.2f"
#       % (grid.best_params_, grid.best_score_, np.mean(test_score)))

# # Decision Trees
# kernel = 'dt'
# max_depth = range(1,51)
# min_samples_split = range(2, 11)
# param_grid = dict(max_depth=max_depth, min_samples_split=min_samples_split)
# grid = GridSearchCV(SVC(kernel=kernel), param_grid=param_grid, cv=cv)

# grid.fit(X, y)
# print("The best parameters are %s with a score of %0.2f, with a std test score of %0.2f"
#       % (grid.best_params_, grid.best_score_, np.mean(test_score)))

# # Random Forest
# kernel = 'rf'
# max_depth = range(1,51)
# min_samples_split = range(2, 11)
# param_grid = dict(max_depth=max_depth, min_samples_split=min_samples_split)
# grid = GridSearchCV(SVC(kernel=kernel), param_grid=param_grid, cv=cv)

# grid.fit(X, y)
# print("The best parameters are %s with a score of %0.2f, with a std test score of %0.2f"
#       % (grid.best_params_, grid.best_score_, np.mean(test_score)))

try:
    os.remove('output3.csv')
except:
    pass





