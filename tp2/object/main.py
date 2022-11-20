import os
from e_learning import Elearning
from display_choices import *


def main():
    print("=====================TP2: Numpy, Pandas, Matplotlib=====================")
    path_df = input("Veuillez renseigner le chemin du Data Frame: ")
    elearning = Elearning(dataset_csv=path_df)
    again = 'o'
    while again == 'o':
        choice = display_choices()

        # os.system("cls")

        if choice == 1:
            print("================Data frame original================")
            print(elearning.display_df_global())
        elif choice == 2:
            print("================Afficher une colonne spécifiques du data frame original================")
            nb_col, nb_row = display_choices_num_column(length_df=len(elearning.data_frame))
            elearning.display_any_column(nb_col=nb_col, nb_row=nb_row)
        elif choice == 3:
            print("================Afficher l'effectif des apprenants pour chaque module================")
            print(elearning.get_effectif_learners())
        elif choice == 4:
            print("================Afficher le nombre total de session pour chaque module================")
            print(elearning.get_total_number_of_session())
        elif choice == 5:
            print("================Afficher le score maximal obtenue dans chaque module================")
            print(elearning.get_score_max_by_module_in_global_df())
        elif choice == 6:
            print("================Afficher le score minimal obtenue dans chaque module================")
            print(elearning.get_score_min_by_module_in_global_df())
        elif choice == 7:
            print("================Afficher le taux de reussite pour les apprenants"
                  " qui ont un score>=50================")
            print(elearning.get_success_rate())
        elif choice == 8:
            print("================Afficher le data frame contenant les points 3-7================")
            print(elearning.get_df_groupby_module())
        elif choice == 9:
            print("================Afficher le top 10 des modules================")
            print(elearning.get_top_10_modules())
        elif choice == 10:
            print("================Convertir le top 10 en tableau numpy================")
            print(elearning.get_df_to_array())
        elif choice == 11:
            print("================Afficher le taux maximal================")
            print(elearning.get_max_success_rate())
        elif choice == 12:
            print("================Afficher le taux minimal================")
            print(elearning.get_max_success_rate())
        elif choice == 13:
            print("================Afficher le data frame avec les données resumé de chaque apprenant pour le top "
                  "module================")
            name_module = elearning.get_name_top_module()
            data_frame_of_one_module = elearning.get_a_module_df(name_module=name_module)
            print(elearning.get_summarize_data_of_each_learners(data_frame_of_one_module=data_frame_of_one_module))
        elif choice == 14:
            print("================Tracer les courbes des 10 top module================")
            print("Cela peut prendre environs 30 secondes, merci de patientez")
            elearning.display_curve_of_10_module()
        elif choice == 15:
            print("================Diagramme de baton des 10 top module================")
            elearning.display_diagram_bar()
        elif choice == 16:
            print("================Tracer les courbes des 3 top module================")
            print("Cela peut prendre environs 15 secondes, merci de patientez")
            elearning.display_n_fig_in_10_top_module()
        elif choice == 17:
            print("================Nuage de point pour tous les modules================")
            elearning.display_scatter_fig()
        else:
            print("================Diagramme de Camembert des modules regroupé par catégorie A, B, "
                  "C et D================")
            elearning.display_pie_fig()

        again = 'a'
        while again not in ['o', 'n']:
            again = input("Voulez-vous continuer ?(o/n)")
            again = again.lower()


if __name__ == "__main__":
    main()
