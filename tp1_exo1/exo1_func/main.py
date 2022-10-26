from calculator import *

# la fonction main
def main():
    print("=======================TP1:Exo1=======================")
    try:
        n = 0
        while n <= 0:
            n = int(input("Donner la valeur de N: "))
    except ValueError:
        print("La valeur entrée est incorrecte !")
    else:
        l = generator_list(n)
        r = total_sum(l)
        print("La valeur de R est: ", r)


# permet d'appeler la fonction main si le fichier en cour d'exécution est le fichier main
if __name__ == "__main__":
    main()
