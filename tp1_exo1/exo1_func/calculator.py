# importation du module atan
from math import atan


# la fonction f(x)
def f(x):
    return x / (x ** 2 + 1)


# la fonction g(x)
def g(x):
    return atan(x)


# la fonction qui determine la liste L
def generator_list(n):
    l = []
    for i in range(-n, n + 1):
        l.append(i)
    return l


# la fonction pour calculer (f(x)-g(x))^2
def sub_f_g_sqrt(x):
    return (f(x) - g(x)) ** 2


# la fonction pour calculer R
def total_sum(l):
    sum = 0
    for i in l:
        sum += sub_f_g_sqrt(i)
    return sum
