import random


# creation d'une classe DataTrans
class DataTrans:

    # le contructeur de DataTrans
    def __init__(self):
        pass

    # la fonction qui calcule f(x) = x ** 3 + 3 * (x ** 2) - 5
    def f(self, x):
        return x ** 3 + 3 * (x ** 2) - 5

    # la fonction qui retourne le minimum d'une liste simple (une liste qui ne contient que des éléments simple comme 2, 3, etc)
    def min_array(self, tab):
        min = tab[0]
        for i in range(len(tab)):
            if min > tab[i]:
                min = tab[i]
        return min

    # la fonction qui retourne le maximum d'une liste simple (une liste qui ne contient que des éléments simple comme 2, 3, etc)
    def max_array(self, tab):
        max = tab[0]
        for i in range(len(tab)):
            if max < tab[i]:
                max = tab[i]
        return max

    # la fonction qui génère une liste global (une liste qui contient d'autre liste)
    def multiple_list_generator(self, length_global_array, length_single_array, max_value):
        my_list = []
        for i in range(length_global_array):
            my_list.append([random.randrange(0, max_value) for i in range(length_single_array)])
        return my_list

    # la fonction qui affiche le minimum d'une liste simple (une liste qui ne contient que des éléments simple comme 3, 2, etc)
    def display_min(self, tab):
        print("============Les maximum============")
        for i in range(len(tab)):
            print("Min de ", tab[i], " est ", self.min_array(tab[i]))

    # la fonction qui affiche le maximum d'une liste simple (une liste qui ne contient que des éléments simple comme 3, 2, etc)
    def display_max(self, tab):
        print("============Les minimum============")
        for i in range(len(tab)):
            print("Max de ", tab[i], " est ", self.max_array(tab[i]))

    # la fonction que affiche la valeur du minimum de ma liste global (une liste qui contient d'autre liste)
    def display_min_global(self, min):
        print("============Le minimum============")
        print("Min = ", min)

    # la fonction que affiche la valeur du maximum de ma liste global (une liste qui contient d'autre liste)
    def display_max_global(self, max):
        print("============Le minimum============")
        print("Max = ", max)

    # la fonction qui retourne le minimum de la liste global (la liste qui contient d'autre liste)
    def min_global(self, tab):
        l = []
        for i in range(len(tab)):
            my_list = tab[i]
            l.append(self.min_array(my_list))
        return self.min_array(l)

    # la fonction qui retourne le maximum de la liste global (la liste qui contient d'autre liste)
    def max_global(self, tab):
        l = []
        for i in range(len(tab)):
            my_list = tab[i]
            l.append(self.max_array(my_list))
        return self.max_array(l)

    # la fonction qui calcule D'
    def d_prime(self, D):
        my_list = []
        for j in range(len(D)):
            my_list.append([self.f(D[j][i]) for i in range(len(D[j]))])
        return my_list

    # la fonction qui affiche D' = f(D)
    def display_d_prime(self, my_list):
        print("D' = ", my_list)
