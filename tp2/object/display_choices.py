NUM_CHOICES = range(1, 19)


def display_choices():
    print("1-Afficher le data frame original")
    print("2-Afficher une ou des colonnes spécifiques")
    print("3-Afficher l'effectif des apprenants pour chaque module")
    print("4-Afficher le nombre total de session pour chaque module")
    print("5-Afficher le score maximal obtenue dans chaque module")
    print("6-Afficher le score minimal obtenue dans chaque module")
    print("7-Afficher le taux de reussite pour les apprenants qui ont un score>=50")
    print("8-Afficher le data frame contenant les points 3-7")
    print("9-Afficher le top 10 des modules")
    print("10-Convertir le top 10 en tableau numpy")
    print("11-Afficher le taux maximal")
    print("12-Afficher le taux minimal")
    print("13-Afficher le data frame avec les données resumé de chaque apprenant")
    print("14-Tracer les courbes des 10 top module")
    print("15-Diagramme de baton des 10 top module")
    print("16-Tracer les courbes des 3 top module")
    print("17-Nuage de point pour tous les modules")
    print("18-Diagramme de Camembert des modules regroupé par catégorie A, B, C et D")

    # global choix
    choix = 0
    while choix not in NUM_CHOICES:
        try:
            choix = int(input("Quel est votre choix ? "))
        except ValueError:
            print("La valeur saisie est incorrect")
            choix = 0
        else:
            return choix
