import pygame
from Boutons.Bouton import Bouton
from Autre.Texte import Texte
import os
from Autre.TexteCentrer import TexteCenter


# ---------------------------------------------------------------------------
# -- Cette page permet d'afficher la liste des joueurs qui se connectent   --
# ---------------------------------------------------------------------------

class PageAttenteJoueurEnLigne():
    def __init__(self, fenetre, background_image) :
        self.fenetre = fenetre
        self.background_image = background_image
        
    def afficherPageJoueurEnAttente(self, infosPartie: dict, listeJoueurs: list[dict]):
        pygame.init()

        #Background
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        TexteCenter(self.fenetre, "Nom de la partie : {0}".format(str(infosPartie["nomPartie"])), 40, 15, 900, 0, 50, (4,32,106))
        TexteCenter(self.fenetre, "{0} / {1} joueurs".format(len(listeJoueurs), str(infosPartie["nbJoueur"])), 30, 15, 900, 0, 100, (4,32,106))
        
        Texte(self.fenetre, "Liste des joueurs :", 25, (0, 0, 0), 50, 200)
        
        positionJoueurY = 250
        for joueur in listeJoueurs:
            imageAvatarPath = os.path.join('ressources', 'avatar', joueur["avatar"] )
            imageAvatar = pygame.image.load(imageAvatarPath)
            self.fenetre.blit(imageAvatar, (100, positionJoueurY)) 
            Texte(self.fenetre, joueur["nomJoueur"], 35, (0, 0, 0), 200, positionJoueurY + 20)
            positionJoueurY = positionJoueurY + 100
   
        pygame.display.update()



    def attendreChoix(self):
        ''' Méthode qui permet d'attendre si le bouton retour a été cliqué ou non'''
        choixEffectue = False
        choix = None
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
 
                elif (event.type == pygame.QUIT):
                    choixEffectue = True   

