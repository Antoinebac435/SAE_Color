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


class PopUpIA():
    def __init__(self, avatar, background, temps, reponse, multicolor) : 
        pygame.init() 
    
        self.background = background
        self.avatar = avatar
        #La carte a jouer
        self.reponse = reponse
        #Si != None : on affiche la réponse de l'IA, la choisir qu'il a choisit
        self.multicolor = multicolor
        
        #Temps restant de l'affichage de la fenêtre
        self.temps = temps
        self.fenetre = pygame.display.set_mode((900, 700))
        self.fontJOUEURTitre = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 45)
        self.fontJOUEUR = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 38)


      
      
    def afficherPopUp(self, temps):
        pygame.init() 
        # Background 
        self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Theme', self.background,  'fondPageAcceuil.png')),(0, 0))
        # Texte
        if self.reponse == None : 
            self.fenetre.blit(self.fontJOUEUR.render("L IA est en train de jouer", True, (0, 0, 0)), (190, 260))
            self.fenetre.blit(self.fontJOUEURTitre.render(str(temps), True, (0, 0, 0)), (430,530))
            ## Ajout de l'avatar du joueur
            DEFAULT_IMAGE_SIZE = (100, 100)
            image = pygame.transform.scale(pygame.image.load(os.path.join('ressources', 'Avatar', self.avatar)), DEFAULT_IMAGE_SIZE)
            self.fenetre.blit(image,(400, 360))
        else : 
            if self.reponse == 'pioche' : 
                self.fenetre.blit(self.fontJOUEUR.render("L'IA a pioché", True, (0, 0, 0)), (230, 260))
            # elif self.reponse == 'multicolor' : 
            #     self.fenetre.blit(self.fontJOUEUR.render("L'IA a joué une carte multicolor", True, (0, 0, 0)), (190, 260))
     
            else :
                if self.multicolor != None : 
                    self.fenetre.blit(self.fontJOUEUR.render("L'IA a joué une carte multicolor", True, (0, 0, 0)), (190, 260))
                    self.fenetre.blit(self.fontJOUEUR.render("Il a choisi la couleur :"+ str(self.reponse.getTitre()),  True, (0, 0, 0)), (300, 400))
                else :

                    self.fenetre.blit(self.fontJOUEUR.render("L'IA a joué :", True, (0, 0, 0)), (190, 260))
                    self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.reponse.getCouleur() + "_" + self.reponse.getTitre() + ".svg").convert_alpha(), (400, 400))  

     
        pygame.display.update()    
        
        return self.fenetre
    
    
      
 
            
            
            
            
            
           
        
        
    
        
# if __name__ == "__main__" : 
#     pygame.init()
#     fenetre2 = pygame.display.set_mode((900, 700))
#     p = PopUp()
#     p.afficherFenetre()

          
       
    