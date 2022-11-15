from tp1_exo3.exo1_app.tools import *


def main():
    print("=======================TP1:Exo3-exo1=======================")
    n = 0
    again = 'o'
    choice = 0
    while again == 'o':
        display_choice()
        try:
            while choice < 1 or choice > 5:
                choice = int(input("Quel operation voulez-vous faire ? "))

            while n <= 0:
                n = int(input("Donner la valeur de N: "))
        except ValueError:
            print("La valeur entrée est incorrecte !")
        else:
            my_result(n=n, choice=choice)
        finally:
            choice = 0
            n = 0
            again = 'a'
            while again not in ['o', 'n']:
                again = str(input("Voulez-vous continuer avec l'exo3 ?(o/n) "))
                again = again.lower()


if __name__ == "__main__":
    main()
