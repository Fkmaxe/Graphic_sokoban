import pygame
pygame.init()

#skin des éléments de jeux
image_mur = pygame.image.load("sprite/block_04.png")
image_caisse = pygame.image.load("sprite/crate_01.png")
image_cible = pygame.image.load("sprite/environment_09.png")
image_joueur = pygame.image.load("sprite/player_01.png")
image_caisse_cible = pygame.image.load("sprite/crate_45.png")
image_sol = pygame.image.load("sprite/ground_01.png")

#variable de graphisme et de jeu
taille_case = 64
niveau_actuel_index = 0
font = pygame.font.Font(None, 36)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)