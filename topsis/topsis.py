# A topsis algorithm implementation by tiagofeu

import numpy as np

# reads data.csv and creates weights array
data = np.genfromtxt('../data/cars.csv', delimiter=',')
weights = np.array([0.3, 0.05, 0.6, 0.05])
cars = ['Palio', 'HB20', 'Corola']

# normalizes data matrix
n = data ** 2
n = np.sqrt(n.sum(axis=0))
n_data = data / n

# apply weights to normalized data
w_data = n_data * weights

print(w_data)
