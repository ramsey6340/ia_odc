from tp1_exo2.exo2_func.tools import *


# La fonction main
def main():
    print("=======================TP1:Exo3-exo2=======================")
    again = 'o'
    choice = 0
    while again == 'o':
        display_choice()
        try:
            while choice < 1 or choice > 5:
                choice = int(input("Quel operation voulez-vous faire ? "))
            n = int(input("Combien de liste voulez-vous dans D ? "))
            s = int(input("Quel est la taille de chacune de ces liste ? "))
            max_value = int(input("Quel est la valeur maximal à ne pas depasser ? "))
        except ValueError:
            print("La valeur entrée est incorrecte !")
        else:
            my_result(choice=choice, length_global_array=n, length_single_array=s, max_value=max_value)
        finally:
            choice = 0
            again = 'a'
            while again not in ['o', 'n']:
                again = str(input("Voulez-vous continuer avec l'exo3 ?(o/n) "))
                again = again.lower()


# appele de la fonction main si le fichier courant est le fichier main
if __name__ == "__main__":
    main()
