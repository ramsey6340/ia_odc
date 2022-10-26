import random


class DataTrans:
    def __init__(self):
        pass

    def f(self, x):
        return x ** 3 + 3 * (x ** 2) - 5

    def min_array(self, tab):
        min = tab[0]
        for i in range(len(tab)):
            if min > tab[i]:
                min = tab[i]
        return min

    def max_array(self, tab):
        max = tab[0]
        for i in range(len(tab)):
            if max < tab[i]:
                max = tab[i]
        return max

    def multiple_list_generator(self, length_global_array, length_single_array, max_value):
        my_list = []
        for i in range(length_global_array):
            my_list.append([random.randrange(0, max_value) for i in range(length_single_array)])
        return my_list

    def display_min(self, tab):
        print("============Les maximum============")
        for i in range(len(tab)):
            print("Min de ", tab[i], " est ", self.min_array(tab[i]))

    def display_max(self, tab):
        print("============Les minimum============")
        for i in range(len(tab)):
            print("Max de ", tab[i], " est ", self.max_array(tab[i]))

    def display_min_global(self, min):
        print("============Le minimum============")
        print("Min = ", min)

    def display_max_global(self, max):
        print("============Le minimum============")
        print("Max = ", max)

    def min_global(self, tab):
        l = []
        for i in range(len(tab)):
            my_list = tab[i]
            l.append(self.min_array(my_list))
        return self.min_array(l)

    def max_global(self, tab):
        l = []
        for i in range(len(tab)):
            my_list = tab[i]
            l.append(self.max_array(my_list))
        return self.max_array(l)

    def d_prime(self, D):
        my_list = []
        for j in range(len(D)):
            my_list.append([self.f(D[j][i]) for i in range(len(D[j]))])
        return my_list

    def display_d_prime(self, my_list):
        print("D' = ", my_list)
