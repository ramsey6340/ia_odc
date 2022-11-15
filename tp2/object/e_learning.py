import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class Elearning:
    def __init__(self, dataset_csv):
        self.data_frame = pd.read_csv(dataset_csv, delimiter=';')

    # ==========================Parti 1==========================
    def get_effectif_apprenant(self):
        # calcule de l'effectif des apprenants pour chaque module,
        #  en faisant attention parce que les apprenants peuvent se répeter

        return self.data_frame.groupby("object_id").actor.nunique()

    def get_nombre_total_session(self):
        # calcule du nombre total de session pour chaque module
        return self.data_frame.groupby("object_id").session_uuid.count()

    def get_score_max_par_module(self):
        # calcule du score maximal pour chaque module
        return self.data_frame.groupby("object_id").score.max()

    def get_score_min_par_module(self):
        # calcule du score minimal pour chaque module
        return self.data_frame.groupby("object_id").score.min()

    def get_nombre_apprenant_admis(self):
        # calcule du nombre d'apprenant pour chaque module dont le score est >=50
        # taux de ressite = (nombre_eleve_plus_de_50 x 100) / effective_apprenant
        return self.data_frame.loc[self.data_frame.score >= 50].groupby("object_id").actor.nunique()

    def get_df_groupby_module(self):
        # creation du data frame regroupé par module et contenant les champs suivant:
        # effectif des apprenants par module
        # nombre total de session
        # score maximal obtenue dans le module
        # score minimal obtenue dans le module
        # taux de reussite du module

        my_dict = {"effectif": self.get_effectif_apprenant(),
                   "nombre_total_session": self.get_nombre_total_session(),
                   "score_max": self.get_score_max_par_module(),
                   "score_min": self.get_score_min_par_module(),
                   "taux_de_reussite": (self.get_nombre_apprenant_admis() * 100) / self.get_effectif_apprenant()
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
    def get_max_taux_de_reussite(self):
        # obtenir le taux maximal dans le top 10 des modules
        return max(self.get_top_10_modules().taux_de_reussite)

    def get_min_taux_de_reussite(self):
        # obtenir le taux minimal dans le top 10 des modules
        return min(self.get_top_10_modules().taux_de_reussite)

    def get_name_top_module(self):
        # obtenir le nom du premier module dans le top 10 des modules
        taux_max = self.get_max_taux_de_reussite()
        top_module = self.get_top_10_modules().loc[self.get_top_10_modules().taux_de_reussite == taux_max]
        return top_module.index[0]

    def get_name_last_module(self):
        # obtenir le nom du dernier module dans le top 10 des modules
        taux_min = self.get_min_taux_de_reussite()
        last_module = self.get_top_10_modules().loc[self.get_top_10_modules().taux_de_reussite == taux_min]
        return last_module.index[0]

    def get_a_module_df(self, name_module):
        # le data frame dont le nom de module correspond au nom du top module trié par un nombre précis de champ voulue
        return self.data_frame.loc[
            self.data_frame.object_id == name_module,
            ["actor", "session_uuid", "object_id", "score", "temps"]
        ]

    def get_total_session_par_apprenant_du_module(self, data_frame):
        # calcul du nombre total de session pour le top module regrouper par apprenant
        return data_frame.groupby("actor").session_uuid.nunique()

    def get_total_temps_par_apprenant_du_module(self, data_frame):
        # calcul du nombre total de temps pour le top module régroupé par apprenant
        return data_frame.groupby("actor").temps.sum()

    def get_score_max_par_apprenant_du_module(self, data_frame):
        # calcul du score maximal pour le top modul régroupé par apprenant
        return data_frame.groupby("actor").score.max()

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
        return self.get_score_max_par_apprenant_du_module(data_frame=data_frame).map(
            lambda x: Elearning.get_a_bit(x))  # la fonction joue sur les Series

    def get_final_top_module_df(self, data_frame):
        # creation du data frame final à partir des données precedemment calculer
        top_module_dict = {
            "nbre_total_session": self.get_total_session_par_apprenant_du_module(data_frame=data_frame),
            "nbre_total_temps": self.get_total_temps_par_apprenant_du_module(data_frame=data_frame),
            "score": self.get_score_max_par_apprenant_du_module(data_frame=data_frame),
            "resultat": self.get_colonne_pour_admission(data_frame=data_frame)
        }
        return pd.DataFrame(top_module_dict)

    # ==========================Fin du partie 2==========================

    # ==========================Parti 3==========================
    
    # ==========================Fin du partie 3==========================
