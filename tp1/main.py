import tp1_exo1.exo1_func.main as exo1func
import tp1_exo1.exo1_obj.main as exo1obj
import tp1_exo2.exo2_func.main as exo2func
import tp1_exo2.exo2_obj.main as exo2obj
import tp1_exo3.exo1_app.main as exo3exo1app
import tp1_exo3.exo2_app.main as exo3exo2app
import tp1_exo4.main as exo4

NB_EXO = range(1, 8)


def main():
    num_exo = 0
    again = 'o'
    while again == 'o':

        print("==================TP1==================")
        print("1-Exo1: sous forme de fonction")
        print("2-Exo1: sous forme d'objet")
        print("3-Exo2: sous forme de fonction")
        print("4-Exo2: sous forme d'objet")
        print("5-Exo3: exo1 sous forme d'application console")
        print("6-Exo3: exo2 sous forme d'application console")
        print("7-Exo4: sous forme de fonction")

        try:
            while num_exo not in NB_EXO:
                num_exo = int(input("Quel exercice voulez-vous exécuter ? "))

        except ValueError:
            print("La valeur entrée est incorrecte !")

        if num_exo == 1:
            exo1func.main()
        elif num_exo == 2:
            exo1obj.main()
        elif num_exo == 3:
            exo2func.main()
        elif num_exo == 4:
            exo2obj.main()
        elif num_exo == 5:
            exo3exo1app.main()
        elif num_exo == 6:
            exo3exo2app.main()
        else:
            exo4.main()
        again = 'a'
        while again not in ['o', 'n']:
            again = input("Voulez-vous continuer ?(o/n)")
            again = again.lower()
            num_exo  = 0
    else:
        print("Au revoir !")


if __name__ == "__main__":
    main()
