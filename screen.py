import pygame
from niveaux import liste_niveaux
def taille_ecran(niveaux):
    largeur = 0
    hauteur = 0
    for i, index_niveaux in enumerate(niveaux):
        for j, index_hauteur in enumerate(index_niveaux):
            if j > hauteur:
                hauteur = j
            for k ,index_largeur in enumerate(index_hauteur):
                if k > largeur:
                    largeur = k
    return (largeur+1)*64, (hauteur+1)*64

taille_fenetre = taille_ecran(liste_niveaux)
ecran = pygame.display.set_mode(taille_fenetre)
ecran.fill((0,0,0))
pygame.display.set_caption("Sokoban")