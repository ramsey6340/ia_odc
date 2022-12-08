from tp1_exo2.exo2_obj.data_trans import DataTrans


# la fonction main
def main():
    print("=======================TP1:Exo2-Objet=======================")
    try:
        n = int(input("Combien de liste voulez-vous dans D ? "))
        s = int(input("Quel est la taille de chacune de ces liste ? "))
        max_value = int(input("Quel est la valeur maximal à ne pas depasser ? "))
    except ValueError:
        print("La valeur entrée est incorrecte !")
    else:
        data_tran = DataTrans()
        D = data_tran.multiple_list_generator(length_global_array=n, length_single_array=s, max_value=max_value)
        print("D = ",D)
        data_tran.display_min(D)
        data_tran.display_max(D)
        data_tran.display_min_global(data_tran.min_global(D))
        data_tran.display_max_global(data_tran.max_global(D))


# appele de la fonction main si le fichier courant est le fichier main
if __name__ == "__main__":
    main()
