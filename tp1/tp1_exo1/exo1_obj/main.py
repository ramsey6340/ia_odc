from tp1_exo1.exo1_obj.calculator import Calculator


# la fonction main qui sera appelé à l'execution du programme
def main():
    print("=======================TP1:Exo1-Objet=======================")
    try:
        n = 0
        while n <= 0:
            n = int(input("Donner la valeur de N: "))
    except ValueError:
        print("La valeur entrée est incorrecte !")
    else:
        calcul = Calculator(n)
        l = calcul.generator_list()
        r = calcul.total_sum(l)
        print("La valeur de R est: ", r)


# permet d'appeler la fonction main si le fichier en cour d'exécution est le fichier main
if __name__ == "__main__":
    main()
