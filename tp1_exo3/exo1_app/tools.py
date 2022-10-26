from tp1_exo1.exo1_obj.calculator import Calculator

# la fonction qui fait le traitement en fonction du choix de l'utilisateur
def my_result(n, choice):
    calcul = Calculator(n)
    if choice == 1:
        my_list = calcul.generator_list()
        for x in my_list:
            print("f(", x, ") = ", calcul.f(x))
    elif choice == 2:
        my_list = calcul.generator_list()
        for x in my_list:
            print("g(", x, ") = ", calcul.g(x))
    elif choice == 3:
        my_list = calcul.generator_list()
        print("La valeur de L est: ", my_list)
    elif choice == 4:
        my_list = calcul.generator_list()
        for x in my_list:
            print(f"(f({x})-g({x}))^2 = ", calcul.sub_f_g_sqrt(x))

    else:
        my_list = calcul.generator_list()
        r = calcul.total_sum(my_list)
        print("La valeur de R est: ", r)


# la fonction qui affiche les differents choix possible
def display_choice():
    print("=======================TP1:Exo1=======================")
    print("====Calcule de R = SUM(f(x)-g(x))^2====")
    print("1- calculer f(x)")
    print("2- calculer g(x)")
    print("3- Générer la liste L")
    print("4- calculer (f(x)-g(x))^2")
    print("5- calculer R")