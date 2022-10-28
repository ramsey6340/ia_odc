import random

from tp1_exo2.exo2_obj.data_trans import DataTrans


# la fonction f(x) = x**3 + 3*(x**2) - 5
def f(x):
    return x ** 3 + 3 * (x ** 2) - 5


# la fonction qui retourne le minimun
def min_array(tab):
    min = tab[0]
    for i in range(len(tab)):
        if min > tab[i]:
            min = tab[i]
    return min


# la fonction qui retoune le maximun
def max_array(tab):
    max = tab[0]
    for i in range(len(tab)):
        if max < tab[i]:
            max = tab[i]
    return max


# la fonction qui génère une liste qui contient d'autre liste
def multiple_list_generator(length_global_array, length_single_array, max_value):
    my_list = []
    for i in range(length_global_array):
        my_list.append([random.randrange(0, max_value) for i in range(length_single_array)])
    return my_list


# la fonction qui affiche le minimun d'une
def display_min(tab):
    print("============Les minimum============")
    for i in range(len(tab)):
        print("Min de ", tab[i], " est ", min_array(tab[i]))


# la fonction qui affiche le maximum d'une liste simple
def display_max(tab):
    print("============Les maximum============")
    for i in range(len(tab)):
        print("Max de ", tab[i], " est ", max_array(tab[i]))


# la fonction qui affiche le minimun de notre liste global (la liste qui contient d'autre liste)
def display_min_global(min):
    print("============Le minimum global============")
    print("Min = ", min)


# la fonction qui affiche le maximum de notre liste global (la liste qui contient d'autre liste)
def display_max_global(max):
    print("============Le maximum global============")
    print("Max = ", max)


# la fontion qui affiche le minimun de la liste global
def min_global(tab):
    l = []
    for i in range(len(tab)):
        my_list = tab[i]
        l.append(min_array(my_list))
    return min_array(l)


# la fontion qui affiche le maximum de la liste global
def max_global(tab):
    l = []
    for i in range(len(tab)):
        my_list = tab[i]
        l.append(max_array(my_list))
    return max_array(l)


# la fonction qui calcule et retourne D' = f(D)
def d_prime(D):
    my_list = []
    for j in range(len(D)):
        my_list.append([f(D[j][i]) for i in range(len(D[j]))])
    return my_list


# la fonction affiche D'
def display_d_prime(my_list):
    print('==========Valeur de D\'==========')
    print("D' = ", my_list)


# la fonction qui affiche les different choix possible
def display_choice():
    print("=======================TP1:Exo2=======================")
    print("====Calcule de f(x) = x^3 + 3x^2 – 5====")
    print("1- calculer f(x)")
    print("2- crée une liste global avec des valeurs aleatoire")
    print("3- determiner le min et le max de chacune des liste composant la liste global")
    print("4- trouver le min global et le max global")
    print("5- calculer D'")


# la fonction qui affiche les resultats en fonction du choix fait par l'utilisateur
def my_result(choice, length_global_array, length_single_array, max_value):
    data_trans = DataTrans()
    D = data_trans.multiple_list_generator(length_global_array=length_global_array, length_single_array=length_single_array, max_value=max_value)
    if choice == 1:
        my_list = data_trans.d_prime(D)
        print(D)
        for j in range(len(my_list)):
            for i in range(len(my_list[j])):
                print(f"f({D[j][i]}) = ",my_list[j][i])
    elif choice == 2:
        print("D = ", D)
    elif choice == 3:
       data_trans.display_min(D)
       data_trans.display_max(D)
    elif choice == 4:

        min = data_trans.min_global(D)
        display_min_global(min)

        max = data_trans.max_global(D)
        display_max_global(max)

    else:
        my_list = data_trans.d_prime(D)
        display_d_prime(my_list)


