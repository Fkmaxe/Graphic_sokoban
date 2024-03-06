def jeu_gagne():
    for y in range(hauteur_niveau):
        for x in range(largeur_niveau):
            if niveau_original[y][x] == "T" and niveau[y][x] not in ["CT", "C"]:
                return False
    # Si toutes les cibles sont couvertes par des caisses, le jeu est gagné
    global niveau_actuel_index
    niveau_actuel_index += 1  # Incrémente l'index pour passer au niveau suivant
    if niveau_actuel_index < len(niveaux):
        charger_niveau(niveau_actuel_index)  # Charge le niveau suivant
        return False  # Pour éviter de quitter le jeu
    else:
        print("Félicitations, vous avez terminé tous les niveaux !")
        return True  # Aucun niveau restant