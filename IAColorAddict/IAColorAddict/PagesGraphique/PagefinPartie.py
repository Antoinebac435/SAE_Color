import pygame
from Boutons.Bouton import Bouton
from Autre.Texte import Texte
import os

from Autre.TexteCentrer import TexteCenter

# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher une fenêtre de fin de partie.          --
# -- on peut y rejouer, ou aller à lacceuil                                --
# ---------------------------------------------------------------------------




class PagefinPartie():
    def __init__(self, fenetre, background_image, nom : str | None):
        self.fenetre = fenetre
        self.background_image = background_image
        self.nom = nom
        
        self.fontJOUEURTitre = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 45)

        
        
        
        
    def afficherPagefinPartie(self):
        pygame.init()

        #Background
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        self.fenetre.blit(self.fontJOUEURTitre.render("Le joueur " + str(self.nom) + " a gagné", True, (0, 0, 0)), (250, 200))


        # Boutons
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