import pygame
import sys
from screen import ecran
pygame.init()

font = pygame.font.Font(None, 36)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#ecran fin de jeux
def regame_screen(mouve):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    running = False  # Si l'utilisateur appuie sur 'Y', la boucle s'arrête
                if event.key == pygame.K_n:
                    pygame.quit()  # Si l'utilisateur appuie sur 'N', quittez Pygame
                    sys.exit()

        ecran.fill((0, 0, 0))
        draw_text('mouvement :', font, (255, 255, 255), ecran,150 ,100 )
        draw_text(str(mouve), font, (255, 255, 255), ecran,320 ,100 )
        draw_text('Vous avez finit', font, (255, 255, 255), ecran, 150, 200)
        draw_text('Appuyer pour rejouer? (Y/N)', font, (255, 255, 255), ecran, 150, 300)

        pygame.display.flip()

