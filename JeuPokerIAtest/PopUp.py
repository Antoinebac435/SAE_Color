import random
from Joueur import Joueur
from Carte import Carte  
from os import listdir
import pygame
from Bouton import Bouton
import os
import time

from TexteCentrer import TexteCenter

class PopUp():
    def __init__(self, backgroundImage: pygame.Surface ) : 
        pygame.init() 
        self.backgroundImage = backgroundImage
        self.fenetre = pygame.display.set_mode((900, 700))
        self.fontJOUEURTitre = pygame.font.Font(os.path.join('policeEcriture', 'Grandstander-clean.ttf'), 45)
        self.fontJOUEUR = pygame.font.Font(os.path.join('policeEcriture', 'Grandstander-clean.ttf'), 38)
     
    def afficherPopUp(self, tour: int, joueur: Joueur, indiceJoueur: int, plusGrosseMise: int):
        pygame.init() 
        self.fenetre.blit(self.backgroundImage,(0, 0))  
        TexteCenter(self.fenetre, "Tour : {0}".format(tour), 50, 15, 900, 0, 50, (24,32,106))     
        self.fenetre.blit(self.fontJOUEURTitre.render("C'est au tour de : ", True, (0, 0, 0)), (250, 100))
        TexteCenter(self.fenetre, "{0}  (joueur {1} du tour)".format(joueur.getNom(), indiceJoueur + 1), 40, 15, 900, 0, 200, (255,255,255))
        TexteCenter(self.fenetre, "Vous devez miser : {0}".format(plusGrosseMise), 40, 15, 900, 0, 500, (255,255,255))    
        
        DEFAULT_IMAGE_SIZE = (100, 100)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)  
        pygame.draw.circle(self.fenetre, (r,g,b), (380+70, 330), 55)
        pygame.draw.circle(self.fenetre, (0,0,0), (380+70, 330), 55,3)

        image = pygame.transform.scale(joueur.getImageAvatar(), DEFAULT_IMAGE_SIZE)
        self.fenetre.blit(image,(400, 290))

        TexteCenter(self.fenetre, "Appuyer sur une touche pour continuer", 30, 15, 900, 0, 600, (4,32,106))    

        pygame.display.update()    
        
        sortir = False
        while sortir == False:
            for event in pygame.event.get():
                if  (event.type == pygame.KEYDOWN):
                    sortir = True
                elif (event.type == pygame.QUIT):
                    pygame.quit() 