import pygame

from Bouton import Bouton
from Boutoncercle import Boutonc
class PageAcceuil():
    def __init__(self, fenetre, background_image) -> None:
        pygame.init()
        
        #Fenetre
        self.fenetre = fenetre
        self.background_image = background_image

    def getBoutonJouer(self):
        return self.boutonJouer
    
    def afficherPageAcceuil(self):
        pygame.display.set_caption("Jeu : Poker")
        
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        #Croix pour quitter
        self.croixQuitter = "./images/Outils/signe-de-la-croix-removebg-preview.png"
        background = pygame.image.load(self.croixQuitter)
        
        # self.cercleQuitter = pygame.draw.circle(self.fenetre50)
        self.fenetre.blit(background,(10, 10))
        
        #Logo
        if self.background_image == "./images/Theme/Noel/fondPageAcceuil.png":
            logo = "./images/Theme/Noel/logoAcceuil.png"
            background = pygame.image.load(logo)
            self.fenetre.blit(background,(330, 5))

        elif self.background_image == "./images/Theme/Haloween/fondPageAcceuil.png":
            logo = "./images/Theme/Haloween/logoAcceuil.png"
            background = pygame.image.load(logo)
            self.fenetre.blit(background,(310, 5))

        elif self.background_image == "./images/Theme/Paques/fondPageAcceuil.png":
            logo = "./images/Theme/Paques/logoAcceuil.png"
            background = pygame.image.load(logo)
            self.fenetre.blit(background,(310, 5))

        else :
            logo = "./images/Theme/Defaut/logoAcceuil.png"
            background = pygame.image.load(logo)
            self.fenetre.blit(background,(335, 15))
        
        # Boutons (Jouer, Option, Règle)
        self.boutonJouer = Bouton(300,300,300,50,(243,223,36),"Jouer",self.fenetre,30,True)
        self.boutonOption = Bouton(300,400,300,50,(243,223,36),"Option",self.fenetre,30,True)
        self.boutonRegle = Bouton(300,500,300,50,(243,223,36),"Règle",self.fenetre,30,True)
        self.boutonCroix = Boutonc(30,25,(0,0,0),self.fenetre,15)

        pygame.display.update()
        
    def attendreChoix(self)->str:
        choixEffectue = False
        choix = ""
        while choixEffectue == False:
            for event in pygame.event.get():
                # On change le pointer de la souris au survol sur un bouton
                if (event.type == pygame.MOUSEMOTION):
                    positionCurseur = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boutonJouer.verifier_click_bouton(positionCurseur) or self.boutonOption.verifier_click_bouton(positionCurseur) or self.boutonRegle.verifier_click_bouton(positionCurseur) or self.boutonCroix.verifier_click_bouton(positionCurseur):
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
                
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)

                    # Pour commencer à jouer, choix des joueurs
                    if self.boutonJouer.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Jouer"

                    # Pour les options
                    elif self.boutonOption.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Option"

                    # Pour les règles
                    elif self.boutonRegle.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Regles"

                    # Pour quitter
                    elif self.boutonCroix.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Fermer"

                elif (event.type == pygame.QUIT):
                    choixEffectue = True
                    
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
        
        return choix       
    
                    
    # def verifier_boutonQuitter(self,clickPos):
        
    #     if self.cercleQuitter.
    #         return True
    #     else:
    #         return False


# p = PageAcceuil()
