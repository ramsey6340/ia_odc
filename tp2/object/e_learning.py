import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Elearning:
    def __init__(self, dataset_csv):
        is_success = False
        delimiter_list = [',', ';', '/', ':']
        i = 0
        while i < len(delimiter_list) and not is_success:
            try:
                self.data_frame = pd.read_csv(dataset_csv, delimiter=delimiter_list[i])
            except pd.errors.ParserError:
                i += 1
            except FileNotFoundError:
                print(f"Le chemin d'accès '{dataset_csv}' est introuvable !")
                exit()
            else:
                is_success = True
        if not is_success:
            print("Erreur: Le data frame ne peut pas etre ouvert !")
        else:
            print("Succes: Le data frame a bien été lu !")

    # ==========================Parti 1==========================

    def display_df_global(self):
        return self.data_frame

    def get_effectif_learners(self):
        # calcule de l'effectif des apprenants pour chaque module,
        #  en faisant attention parce que les apprenants peuvent se répeter

        return self.data_frame.groupby("object_id").actor.nunique()

    def get_total_number_of_session(self):
        # calcule du nombre total de session pour chaque module
        return self.data_frame.groupby("object_id").session_uuid.count()

    def get_score_max_by_module_in_global_df(self):
        # determination du score maximal pour chaque module
        return self.data_frame.groupby("object_id").score.max()

    def get_score_min_by_module_in_global_df(self):
        # calcule du score minimal pour chaque module
        return self.data_frame.groupby("object_id").score.min()

    def get_number_of_learners_admitted(self):
        # calcule du nombre d'apprenant pour chaque module dont le score est >=50
        # taux de ressite = (nombre_eleve_plus_de_50 x 100) / effective_apprenant
        return self.data_frame.loc[self.data_frame.score >= 50].groupby("object_id").actor.nunique()

    def get_success_rate(self):
        success_rate_column = (self.get_number_of_learners_admitted() * 100) / self.get_effectif_learners()
        success_rate_column.replace(np.nan, 0, inplace=True)
        return success_rate_column

    def get_df_groupby_module(self):
        # creation du data frame regroupé par module et contenant les champs suivant:
        # effectif des apprenants par module
        # nombre total de session
        # score maximal obtenue dans le module
        # score minimal obtenue dans le module
        # taux de reussite du module

        my_dict = {"effectif": self.get_effectif_learners(),
                   "nombre_total_session": self.get_total_number_of_session(),
                   "score_max": self.get_score_max_by_module_in_global_df(),
                   "score_min": self.get_score_min_by_module_in_global_df(),
                   "taux_de_reussite": self.get_success_rate()
                   }
        df_tp2 = pd.DataFrame(my_dict)
        # df_tp2.dropna(axis=0, inplace = True) # supprime les NaN dans le data frame
        df_tp2.replace(np.nan, 0, inplace=True)
        return df_tp2

    def get_top_10_modules(self):
        # le data frame contenat les top 10 des modules classé en fonction de leur taux de reussite
        return self.get_df_groupby_module().sort_values(by='taux_de_reussite', ascending=False).head(10)

    def get_df_to_array(self):
        # conversion du data frame en tableau numpy
        return np.array(self.get_top_10_module())

    # ==========================Fin du partie 1==========================

    # ==========================Parti 2==========================

    # ***********Pour le top module***********
    def get_max_success_rate(self):
        # obtenir le taux maximal dans le top 10 des modules
        return max(self.get_top_10_modules().taux_de_reussite)

    def get_min_success_rate(self):
        # obtenir le taux minimal dans le top 10 des modules
        return min(self.get_top_10_modules().taux_de_reussite)

    def get_name_top_module(self):
        # obtenir le nom du premier module dans le top 10 des modules
        taux_max = self.get_max_success_rate()
        top_module = self.get_top_10_modules().loc[self.get_top_10_modules().taux_de_reussite == taux_max]
        return top_module.index[0]

    def get_name_last_module(self):
        # obtenir le nom du dernier module dans le top 10 des modules
        taux_min = self.get_min_success_rate()
        last_module = self.get_top_10_modules().loc[self.get_top_10_modules().taux_de_reussite == taux_min]
        return last_module.index[0]

    def get_a_module_df(self, name_module):
        # le data frame dont le nom de module correspond au nom du top module trié par un nombre précis de champ voulue
        return self.data_frame.loc[
            self.data_frame.object_id == name_module,
            ["actor", "session_uuid", "object_id", "score", "temps"]
        ]

    def get_total_session_by_learner_of_module(self, data_frame_of_one_module):
        # calcul du nombre total de session pour un module precis regrouper par apprenant
        return data_frame_of_one_module.groupby("actor").session_uuid.nunique()

    def get_total_time_by_learner_of_module(self, data_frame_of_one_module):
        # calcul du nombre total de temps pour un module precis régroupé par apprenant
        return data_frame_of_one_module.groupby("actor").temps.sum()

    def get_score_max_by_learner_of_module(self, data_frame_of_one_module):
        # calcul du score maximal pour un module precis régroupé par apprenant
        return data_frame_of_one_module.groupby("actor").score.max()

    @classmethod
    def get_a_bit(cls, value):
        # fonction permettant de retourner 0 ou 1 en fonction de la valeur donnée comme paramettre
        """
           retourne 0 ou 1 en fonction de la valeur donnée en paramettre
           param: entier
           retour: 0 ou 1
        """
        if value >= 50:
            return 1
        else:
            return 0

    def get_colonne_pour_admission(self, data_frame):
        # calcul de la colonne pour le résultat final (1 si score>= et 0 sinon)
        return self.get_score_max_by_learner_of_module(data_frame_of_one_module=data_frame).map(
            lambda x: Elearning.get_a_bit(x))  # la fonction joue sur les Series

    def get_summarize_data_of_each_learners(self, data_frame_of_one_module):
        # creation du data frame contenant les données résumer de chaque apprenant
        top_module_dict = {
            "nbre_total_session": self.get_total_session_by_learner_of_module(
                data_frame_of_one_module=data_frame_of_one_module
            ),
            "nbre_total_temps": self.get_total_time_by_learner_of_module(
                data_frame_of_one_module=data_frame_of_one_module
            ),
            "score": self.get_score_max_by_learner_of_module(data_frame_of_one_module=data_frame_of_one_module),
            "resultat": self.get_colonne_pour_admission(data_frame=data_frame_of_one_module)
        }
        return pd.DataFrame(top_module_dict)

    # ==========================Fin du partie 2==========================

    # ==========================Parti 3: Matplotlib==========================
    def get_module_name_in_top_10_module(self, index):
        # fonction pour obtenir le nom d'un module precis du top 10 des module
        return self.get_top_10_modules().index[index]

    def get_module_name_in_global_df(self, index):
        # fonction pour obtenir le nom d'un module precis du data frame global
        return self.data_frame.object_id[index]

    def get_list_learner_names(self, module_name):
        # fonction pour obtenir la liste des noms des apprenants d'un module precis
        learners_from_module = self.data_frame.loc[
            self.data_frame.object_id == module_name,
            ["object_id", "actor"]
        ]
        learner_names = learners_from_module.groupby("object_id").actor.unique().values
        return learner_names

    def get_df_learner_for_a_module(self, learner_name, module_name):
        # obtention d'un data frame contenant la liste des score
        # et leur temps pour un apprenant precis dans un module precis
        return self.data_frame[["actor", "object_id", "score", "temps"]].where(
            (self.data_frame.actor == learner_name) & (self.data_frame.object_id == module_name)
        ).dropna(axis=0)

    @classmethod
    def get_score_max_for_a_module(cls, df_learner):
        # fonction pour obtenit le score maximal pour un apprenant dans un module precis
        return df_learner["score"].max()

    @classmethod
    def get_df_score_max(cls, df_learner, score_max):
        # fonction pour obtenir le data frame contenant uniquement le score maximal avec les differents temps
        return df_learner.loc[df_learner.score == score_max]

    @classmethod
    def get_min_time_for_max_score(cls, df_score_max):
        # fonction pour obtenir le temps minimal, pour un score maximal donnée, convertie en minute
        # NB: par défaut le temps est en minute
        time_series = df_score_max.groupby("score").temps.min()
        return time_series.values[0] / 60

    def get_total_time_for_learners_groupby_module(self):
        # fonction pour obtenir le total des temps de tous les apprenants dans les modules
        return self.data_frame.groupby("object_id").temps.sum()

    def get_score_max_for_learner_groupby_module(self):
        # fonction pour avoir le score maximal obtenue dans les modules
        return self.data_frame.groupby("object_id").score.max()

    @classmethod
    def get_total_time_for_learner_for_a_module(cls, df_learner):
        # fonction pour obtenir le total des temps d'un apprenant dans un module
        return df_learner["temps"].sum()

    def get_df_score_max_time_for_learner_in_a_module(self, index, total_time=False):
        score_list = []
        time_list = []
        time = 0
        # obtention du  nom du module
        module_name = self.get_module_name_in_top_10_module(index=index)
        # obtention de la liste des apprenants d'un module precis
        learner_names = self.get_list_learner_names(module_name=module_name)
        # obtention du score et du temps pour un apprenant precis d'un module precis
        for i in range(len(learner_names[0])):
            df_learner = self.get_df_learner_for_a_module(learner_name=learner_names[0][i], module_name=module_name)
            score_max = Elearning.get_score_max_for_a_module(df_learner=df_learner)
            if not total_time:
                df_score_max = Elearning.get_df_score_max(df_learner=df_learner, score_max=score_max)
                time = Elearning.get_min_time_for_max_score(df_score_max=df_score_max)
            else:
                time = Elearning.get_total_time_for_learner_for_a_module(df_learner=df_learner)

            # ajout des données dans la liste
            score_list.append(score_max)
            time_list.append(time)

        # creation et renvoie de notre data frame
        df_final = pd.DataFrame({"score_max": score_list, "temps": time_list})
        df_final.sort_values(by=["score_max", "temps"], ascending=[False, True], inplace=True)
        df_final["rang"] = [i + 1 for i in range(len(df_final))]
        return df_final

    def display_curve_of_10_module(self):
        # methode pour dessiner les courbes des 10 top module
        fig, ax = plt.subplots()
        for i in range(10):
            ax.plot(
                self.get_df_score_max_time_for_learner_in_a_module(i)["temps"],
                self.get_df_score_max_time_for_learner_in_a_module(i)["score_max"],
                label='top {}'.format(i)
            )

        ax.set_xlabel("Abscisses (temps)")
        ax.set_ylabel("Ordonnées (scores)")
        ax.legend()
        plt.show()

    def display_diagram_bar(self):
        # methode pour dessiner le diagramme en batton
        # le positionnement par rapport à l'axe des abscisses
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # le positionnement par rapport à l'axe des ordonnées
        height = self.get_top_10_modules()["taux_de_reussite"]
        # la largeur de chaque bar
        width = 0.05

        # reglage sur les bars
        plt.bar(x, height, width, color=(0.65098041296005249, 0.80784314870834351, 0.89019608497619629, 1))
        # le reglage des point noir sur le bout des bars
        plt.scatter(x, height, color='k', s=40)

        # xlim determine la valeur maximal de la graduation. Si c'est 0.11 allors la valeur maximal est 11
        plt.xlim(0, 11)
        # ylim determine la valeur maximal de la graduation. Si c'est 0.14 allors la valeur maximal est 14
        plt.ylim(1)
        plt.title('Diagramme en Batons')

        plt.show()

    def display_n_fig_in_10_top_module(self, nb_fig=3):
        fig, ax = plt.subplots(nb_fig, 1)
        fig.subplots_adjust(hspace=0)
        for i in range(nb_fig):
            ax[i].plot(
                self.get_df_score_max_time_for_learner_in_a_module(index=i)["rang"],
                self.get_df_score_max_time_for_learner_in_a_module(index=i)["score_max"]
            )

            ax[i].set_xlabel("Rang")
            ax[i].set_ylabel("Score Max")

            ax[i].set_title(self.get_top_10_modules().index[i]);
        plt.show()

    def get_df_scatter(self):
        df_scatter = pd.DataFrame(
            {
                "score_max": self.get_score_max_for_learner_groupby_module(),
                "temps_total": self.get_total_time_for_learners_groupby_module() / 60
            }
        )
        df_scatter.sort_values(by=["score_max", "temps_total"], ascending=[False, True], inplace=True)
        df_scatter["rang"] = [i + 1 for i in range(len(df_scatter))]
        return df_scatter

    def display_scatter_fig(self):
        data = {
            'x': self.get_df_scatter()["rang"],
            'c': np.random.randint(0, 50, len(self.get_df_scatter())),
            'd': np.random.randn(len(self.get_df_scatter())),
            'y': self.get_df_scatter()["temps_total"]
        }
        data['d'] = np.abs(data['d']) * 100
        fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
        # creation du nuage de point
        ax.scatter('x', 'y', c='c', s='d', data=data)
        plt.title('Nuage de points')
        plt.xlabel('x (Rang)')
        plt.ylabel('y (Temps global)');
        plt.show()

    def get_df_category_for_pie_fig(self):
        df_pie = self.get_df_groupby_module().copy()
        df_pie["classe"] = "A"

        df_pie.loc[(df_pie["taux_de_reussite"] >= 80), 'classe'] = 'A'
        df_pie.loc[(df_pie["taux_de_reussite"] < 80) & (df_pie["taux_de_reussite"] >= 60), 'classe'] = 'B'
        df_pie.loc[(df_pie["taux_de_reussite"] < 60) & (df_pie["taux_de_reussite"] >= 50), 'classe'] = 'C'
        df_pie.loc[(df_pie["taux_de_reussite"] < 50), 'classe'] = 'D'

        return df_pie

    def display_pie_fig(self):
        data_pie = self.get_df_category_for_pie_fig().groupby("classe").classe.count()
        plt.pie(data_pie, autopct='%1.2f%%');
        plt.show()

# ==========================Fin du partie 3==========================
