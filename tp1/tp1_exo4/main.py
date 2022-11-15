from tp1_exo4.tools import *


def main():
    print("=======================TP1:Exo4=======================")
    try:
        max_value = int(input("Quel est la valeur maximal à ne pas depasser? "))
    except ValueError:
        print("La valeur entrée est incorrecte !")
    else:
        l = random_value_list(max_value)
        print("Taille du tableau: ", len(l))
        print("Valeurs: ", l)
        print("La moyenne vaut: ", average(l))
        print("La mediane vaut: ", median(l))
        print("La variance vaut: ", variance(l))
        print("L\'ecart type vaut: ", standard_deviation(l))


if __name__ == "__main__":
    main()
