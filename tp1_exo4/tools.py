import random
import numpy as np


ARRAY_LENGTH = 100

# la moyenne
def average(my_list):
    return np.mean(my_list)


# la mediane
def median(my_list):
    return np.median(my_list)


# la variance
def variance(my_list):
    return np.var(my_list)


# l'ecart type
def standard_deviation(my_list):
    return np.std(my_list)


# la fonction générateur de liste
def random_value_list(max_value):
    my_list = []
    for i in range(ARRAY_LENGTH):
        my_list.append(np.round(random.uniform(0, max_value), 2))
    return my_list
