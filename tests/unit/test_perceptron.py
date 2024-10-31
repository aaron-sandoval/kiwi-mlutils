import numpy as np

from kiwi_mlutils.perceptron import perceptron

x = np.array([[1,1], [-1,-1], [2,1]])
y = np.array([1, -1, -1])

print(perceptron(x, y))