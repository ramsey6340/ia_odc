NUM_CHOICES = range(1, 19)
NUM_CHOICES_COLUMN = range(1, 13)


# fonction pour afficher les differentes operations possible sur le data frame original
def display_choices():
    print("1-Afficher le data frame original")
    print("2-Afficher une colonne spécifiques du data frame original")
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


# fonction pour afficher les differentes operation possible
# lorsque l'utilisateur choisie l'option 2 dans la fonction "display_choices"
def display_choices_num_column(length_df):
    print("1-La colonne \"id\"")
    print("2-La colonne \"actor\"")
    print("3-La colonne \"session_uuid\"")
    print("4-La colonne \"object_id\"")
    print("5-La colonne \"activity_type\"")
    print("6-La colonne \"progression\"")
    print("7-La colonne \"score\"")
    print("8-La colonne \"temps\"")
    print("9-La colonne \"total_ecrans\"")
    print("10-La colonne \"created\"")
    print("11-La colonne \"modified\"")
    print("12-La colonne \"learning_object\"")
    print("13-La colonne \"processed\"")

    choix = 0
    nb_row = 0
    is_success = False
    while not is_success:
        try:
            while choix not in NUM_CHOICES_COLUMN:
                choix = int(input("Quel est votre choix de colonne ? "))
            while nb_row < 1 or nb_row > length_df:
                nb_row = int(input(f"Combien de ligne voulez-vous afficher ?(?/{length_df}) "))
        except ValueError:
            print("La valeur saisie est incorrect")
            # choix = 0
            # nb_row = 0
        else:
            is_success = True

    return choix, nb_row
