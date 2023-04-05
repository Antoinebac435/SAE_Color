from Jeu.Jeu import Jeu
from Jeu.Joueur import Joueur
from Jeu.Carte import Carte  
from os import listdir
from Autre.TexteCentrer import TexteCenter
import pygame
import random

from Boutons.Bouton import Bouton
import os

# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher une fenêtre qui indique le changement  --
# -- de joueurs.                                                           --
# ---------------------------------------------------------------------------


class PopUp():
    def __init__(self , joueur, background, avatar) : 
        pygame.init() 
    
        self.background = background
        self.joueur = joueur
        self.avatar = avatar
        self.fenetre = pygame.display.set_mode((900, 700))
        self.fontJOUEURTitre = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 45)
        self.fontJOUEUR = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 38)


      
      
    def afficherPopUp(self):
        pygame.init() 
        # Background 
        self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Theme', self.background,  'fondPageAcceuil.png')),(0, 0))
        
        # Texte
        self.fenetre.blit(self.fontJOUEURTitre.render("C'est au tour de : ", True, (0, 0, 0)), (250, 200))
                
                
        ## Centrer le texte du nom du Joueur
        texteRendu = self.fontJOUEUR.render(self.joueur, True, (60,60,60))
        posTexte = texteRendu.get_rect()
        margeGauche = (900 - posTexte.width) / 2
        margeHauteur = (66 - posTexte.height) / 2
        self.fenetre.blit(texteRendu, (0 + margeGauche, 280 + margeHauteur)) 


        ## Ajout de l'avatar du joueur
        DEFAULT_IMAGE_SIZE = (100, 100)
        image = pygame.transform.scale(pygame.image.load(os.path.join('ressources', 'Avatar', self.avatar)), DEFAULT_IMAGE_SIZE)
        self.fenetre.blit(image,(400, 360))
     
        pygame.display.update()    
        
        return self.fenetre
    
    
      
 
            
            
            
            
            
           
        
        
    
        
# if __name__ == "__main__" : 
#     pygame.init()
#     fenetre2 = pygame.display.set_mode((900, 700))
#     p = PopUp()
#     p.afficherFenetre()

          
       
    