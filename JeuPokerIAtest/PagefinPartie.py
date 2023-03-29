import pygame
from Bouton import Bouton
from Texte import Texte

from TexteCentrer import TexteCenter

class PagefinPartie():
    def __init__(self, fenetre, background_image) -> None:
        self.fenetre = fenetre
        self.background_image = background_image
        
    def afficherPagefinPartie(self):
        pygame.init()

        #Backgrond
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))

        self.boutonRejouer = Bouton(300,300,400,50,(243,223,36),"Rejouer",self.fenetre,30,True)
        self.boutonAccueil = Bouton(300,400,400,50,(243,223,36),"Retourner à l'accueil",self.fenetre,30,True)

        pygame.display.update()

    def attendreChoix(self):
        choixEffectue = False
        choix = None
        while choixEffectue == False:
            for event in pygame.event.get():
                # On change le pointer de la souris au survol sur un bouton
                if (event.type == pygame.MOUSEMOTION):
                    positionCurseur = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boutonRejouer.verifier_click_bouton(positionCurseur) or self.boutonAccueil.verifier_click_bouton(positionCurseur):
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
                
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boutonRejouer.verifier_click_bouton(positionClick):
                        choix = "Rejouer"
                        choixEffectue = True
                    if self.boutonAccueil.verifier_click_bouton(positionClick):
                        choixEffectue = True
                        choix = "Acceuil"
                        
                elif (event.type == pygame.QUIT):
                    choixEffectue = True
                    
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

        return choix