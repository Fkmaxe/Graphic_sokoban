import pygame
import sys
from config import *
from draw_text import draw_text
from screen import ecran

# Initialisation de Pygame
pygame.init()

def start_screen():
    username = ""
    input_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if input_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(username)  # Affiche le pseudo dans la console ou procédez au jeu
                        input_active = False  # Désactive l'entrée après la soumission
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode

        ecran.fill(BLACK)
        draw_text('Enter your username:', font, WHITE, ecran, 20, 20)

        # Affiche le pseudo en cours de saisie
        draw_text(username, font, WHITE, ecran, 20, 60)

        if not input_active:
            return username

        pygame.display.flip()
