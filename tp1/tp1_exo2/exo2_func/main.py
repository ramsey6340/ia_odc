from tools import *


# la fonction main qui sera appelé à l'execution du programme
def main():
    try:
        n = int(input("Combien de liste voulez-vous dans D ? "))
        s = int(input("Quel est la taille de chacune de ces liste ? "))
        max_value = int(input("Quel est la valeur maximal à ne pas depasser ? "))
    except ValueError:
        print("La valeur entrée est incorrecte !")
    else:
        D = multiple_list_generator(length_global_array=n, length_single_array=s, max_value=max_value)
        print("D = ",D)
        display_min(D)
        display_max(D)
        display_min_global(min_global(D))
        display_max_global(max_global(D))


# permet d'appeler la fonction main si le fichier en cour d'executio est le fichier main
if __name__ == "__main__":
    main()
