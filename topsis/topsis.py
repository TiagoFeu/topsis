from ctypes import sizeof
import numpy as np
import pandas as pd

def normalizing_matrix_d(self):
    """
    This method normalized the matrix_d according to the standard TOPSIS algorithm. You may change if if you want.
    """
    m = self.matrix_d ** 2
    m = np.sqrt(m.sum(axis=0))
    self.matrix_d = self.matrix_d / m

# get data from csv file
data = np.genfromtxt('champions_stats.csv', delimiter=',')

#delete the champion and stats names
data = np.delete(data, 0, axis=0)
data = np.delete(data, 1, axis=1)
# delete the id collumn
data = np.delete(data, 0, axis=1)

# normalize the data
m = data ** 2
m = np.sqrt(m.sum(axis=0))
datan = data / m

#set criteria
criteria = np.ones(18) * (1/18)

#determine wich is the best champion
champs_weighted = datan * criteria

max_per_crit = champs_weighted.max(axis=0)
min_per_crit = champs_weighted.min(axis=0)

print(max_per_crit.shape)

rows, collumns = champs_weighted.shape

positive_d = np.zeros(rows)
negative_d = np.zeros(rows)

# calculate the distance between the champs_weigthed and max_per_crit
for i in range(rows):
    for j in range(collumns):
        positive_d[i] = np.sqrt((champs_weighted[i][j] - max_per_crit[j])**2)
        negative_d[i] = np.sqrt((champs_weighted[i][j] - min_per_crit[j])**2)

TOP = negative_d / (positive_d + negative_d)

print (np.where(TOP == np.amax(TOP)))