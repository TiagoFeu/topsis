# A topsis algorithm implementation by tiagofeu

from turtle import distance
import numpy as np
import matplotlib.pyplot as plt

# reads data csv and deletes the labels
data = np.genfromtxt('../data/top_ten_stocks.csv', delimiter=',')
data = np.delete(data, 0, 1)
data = np.delete(data, 0, 0)

# sets criteria, weights and labels
criteria = ['Stock Price', 'MarketCap', 'P/L', 'Revenue', 'EPS', 'Beta', 'Dividend']
cost_benefit = ['cost', 'benefit', 'cost', 'benefit', 'benefit', 'cost', 'benefit']
weights = np.array([0.05, 0.2, 0.2, 0.2, 0.2, 0.1, 0.05])
labels = ['Apple', 'Microsoft', 'Alphabet C', 'Alphabet A', 'Amazon', 'Tesla', 'Berkshire', 'Broadcom', 'Meta', 'NVIDIA']

# normalizes data matrix
n = data ** 2
n = np.sqrt(n.sum(axis=0))
n_data = data / n

# apply weights to normalized data
w_data = n_data * weights

# calculates the ideal positive and negative solutions
max_criteria = w_data.max(axis=0)
min_criteria = w_data.min(axis=0)

negative_ideal_solution = np.zeros(max_criteria.size)
positive_ideal_solution = np.zeros(max_criteria.size)

for i in range(len(max_criteria)):
    if cost_benefit[i] == 'cost':
        positive_ideal_solution[i] = min_criteria[i]
        negative_ideal_solution[i] = max_criteria[i]
    else:
        positive_ideal_solution[i] = max_criteria[i]
        negative_ideal_solution[i] = min_criteria[i]

# calculates the euclidean distances from the ideal solutions
distance_positive = w_data - positive_ideal_solution
distance_positive = distance_positive ** 2
distance_positive = np.sqrt(distance_positive.sum(axis=1))

distance_negative = w_data - negative_ideal_solution
distance_negative = distance_negative ** 2
distance_negative = np.sqrt(distance_negative.sum(axis=1))

# calculates the relative proximity of the solutions
relative_proximity = distance_negative / (distance_negative + distance_positive)
print(relative_proximity)

# plots the relative proximity
plt.figure(figsize=(15, 10))
plt.bar(labels, relative_proximity)
plt.title('TOP 10 MARKETCAP STOCKS')
plt.savefig('../results/relative_proximity.png')