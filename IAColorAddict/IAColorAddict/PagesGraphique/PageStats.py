import pygame
from Boutons.Bouton import Bouton
from Autre.Texte import Texte
import os
from Autre.TexteCentrer import TexteCenter

class PageStats():
    def __init__(self, fenetre, background_image) -> None:
        self.fenetre = fenetre
        self.background_image = background_image
        
    def afficherPageStats(self):
        pygame.init()

        #Backgrond
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        
        texteRegles = TexteCenter(self.fenetre, "Statistique des Parties", 30, 400, 75, 400, -160, (255, 255, 255))
        
        
        
        retour = os.path.join('ressources','Outils', 'retour.png')
        background = pygame.image.load(retour)
        self.boxRetour = background.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(background, self.boxRetour)
        
    
    
        pygame.display.update()
        
    
    def attendreChoix(self):
        choixEffectue = False
        choix = None
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEMOTION):
                    positionCurseur = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    # on affiche un pointer de souris au survol sur le bouton retour
                    if self.boxRetour.colliderect(positionCurseur):
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))  

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
                        
                elif (event.type == pygame.QUIT):
                    choixEffectue = True