import sys
from config import *
from niveaux import liste_niveaux
from screen import ecran
import time
from end_screen import regame_screen
from start_screen import start_screen
from score_update import update_top_scores




mouve = 0
pygame.init()

niveau = []  # La grille du niveau actuel
niveau_original = []  # Copie originale du niveau pour vérification



def charger_niveau(index):
    global niveau, niveau_original, hauteur_niveau, largeur_niveau
    niveau = [ligne[:] for ligne in liste_niveaux[index]]
    niveau_original = [ligne[:] for ligne in niveau]
    hauteur_niveau = len(niveau)
    largeur_niveau = len(niveau[0]) if niveau else 0

charger_niveau(niveau_actuel_index)
def dessiner_jeu():
    ecran.fill((0, 0, 0))  # Blanc
    for y in range(hauteur_niveau):
        for x in range(largeur_niveau):
            element = niveau[y][x]
            rect = pygame.Rect(x * taille_case, y * taille_case, taille_case, taille_case)
            if element == "#":
                ecran.blit(image_mur, rect.topleft)
            elif element == "C":  # Gère la caisse seule et sur cible
                ecran.blit(image_caisse, rect.topleft)
            if element == "T" :  # Gère la cible vide et avec caisse
                ecran.blit(image_cible, rect.topleft)
            if element == "CT":
                ecran.blit(image_caisse_cible, rect.topleft)
            if element == "J":  # Gère le joueur seul et sur cible
                ecran.blit(image_sol, rect.topleft)
                ecran.blit(image_joueur, rect.topleft)
            if element == "JT":
                ecran.blit(image_cible, rect.topleft)
                ecran.blit(image_joueur, rect)
            if element == " ":
                ecran.blit(image_sol, rect.topleft)
    pygame.display.flip()




def trouver_joueur():
    for y in range(hauteur_niveau):
        for x in range(largeur_niveau):
            if niveau[y][x] in ["J", "JT"]:  # "J" pour joueur seul, "JT" pour joueur sur cible
                return x, y
    return None


def deplacer_joueur(dx, dy):
    x, y = trouver_joueur()
    cible_x, cible_y = x + dx, y + dy

    # Vérifie les limites du niveau pour éviter les erreurs d'index
    if not (0 <= cible_x < largeur_niveau and 0 <= cible_y < hauteur_niveau):
        return

    destination = niveau[cible_y][cible_x]
    est_sur_cible = niveau[y][x] in ["JT", "CT"]  # Le joueur ou la caisse est-il/elle actuellement sur une cible ?

    # Déplacement sur une case vide ou sur une cible
    if destination in [" ", "T"]:
        if est_sur_cible:
            niveau[y][x] = "T"  # Laisse une cible derrière si le joueur était sur une cible
        else:
            niveau[y][x] = " "  # Sinon, laisse une case vide

        niveau[cible_y][cible_x] = "JT" if destination == "T" else "J"  # Marque le joueur sur une cible ou une case vide

    # Déplacement d'une caisse
    elif destination == "C":
        cible_prochaine_x, cible_prochaine_y = cible_x + dx, cible_y + dy
        # Vérifie les limites du niveau pour éviter les erreurs d'index
        if not (0 <= cible_prochaine_x < largeur_niveau and 0 <= cible_prochaine_y < hauteur_niveau):
            return

        destination_prochaine = niveau[cible_prochaine_y][cible_prochaine_x]
        # Peut pousser la caisse sur une case vide ou une cible
        if destination_prochaine in [" ", "T"]:
            niveau[cible_prochaine_y][cible_prochaine_x] = "CT" if destination_prochaine == "T" else "C"  # Marque la caisse sur une cible ou une case vide
            niveau[cible_y][cible_x] = "JT" if destination == "T" else "J"  # Marque le joueur sur une cible ou une case vide
            if est_sur_cible:
                niveau[y][x] = "T"  # Laisse une cible derrière si le joueur était sur une cible
            else:
                niveau[y][x] = " "  # Sinon, laisse une case vide



def jeu_gagne():
    for y in range(hauteur_niveau):
        for x in range(largeur_niveau):
            if niveau_original[y][x] == "T" and niveau[y][x] not in ["CT", "C"]:
                return False
    # Si toutes les cibles sont couvertes par des caisses, le jeu est gagné
    global niveau_actuel_index
    niveau_actuel_index += 1  # Incrémente l'index pour passer au niveau suivant
    if niveau_actuel_index < len(liste_niveaux):
        charger_niveau(niveau_actuel_index)  # Charge le niveau suivant
        return False  # Pour éviter de quitter le jeu
    else:
        end_time = time.time()

        print("Félicitations, vous avez terminé tous les niveaux !")
        return True  # Aucun niveau restant


# Boucle de jeu
start_time = time.time()
username = start_screen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                deplacer_joueur(-1, 0)
                mouve = mouve + 1
            elif event.key == pygame.K_RIGHT:
                deplacer_joueur(1, 0)
                mouve = mouve + 1
            elif event.key == pygame.K_UP:
                deplacer_joueur(0, -1)
                mouve = mouve + 1
            elif event.key == pygame.K_DOWN:
                deplacer_joueur(0, 1)
                mouve = mouve + 1

    dessiner_jeu()

    if jeu_gagne():
        update_top_scores(username, mouve)
        regame_screen(mouve)
        mouve = 0
        niveau_actuel_index = -1


    pygame.time.Clock().tick(60)
