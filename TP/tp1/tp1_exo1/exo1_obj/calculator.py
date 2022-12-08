# importation du module atan
from math import atan


class Calculator:

    def __init__(self, n):
        self.n = n

    # la fonction qui calcule f(x) = x / (x ** 2 + 1)
    def f(self, x):
        return x / (x ** 2 + 1)

    # la fonction qui calcule g(x) = arctan(x)
    def g(self, x):
        return atan(x)

    # la fonction qui determine la liste L (une liste simple d'entier negative et positive)
    def generator_list(self):
        l = []
        for i in range(-self.n, self.n + 1):
            l.append(i)
        return l

    # la fonction pour calculer (f(x)-g(x))^2
    def sub_f_g_sqrt(self, x):
        return (self.f(x) - self.g(x)) ** 2

    # la fonction pour calculer R = sum((f(x)-g(x))^2) pour un intervale donnée
    def total_sum(self, l):
        sum = 0
        for i in l:
            sum += self.sub_f_g_sqrt(i)
        return sum
