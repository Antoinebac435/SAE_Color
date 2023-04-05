from Jeu.Jeu import Jeu
from Jeu.Joueur import Joueur
from Jeu.Carte import Carte  
from os import listdir
from Boutons.BoutonListe import BoutonListe

import pygame

from Boutons.Bouton import Bouton
import os

# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher une fenêtre lorsqu'un joueur a utilisé --
# -- une carte multicolor.                                                 --
# ---------------------------------------------------------------------------


class PopUpMulticolor():
    def __init__(self, background ) : 
        pygame.init() 
        
        # Background 
        self.background = background
        self.fenetre = pygame.display.set_mode((900, 700))
        
        # Police d'écriture
        self.fontJOUEURTitre = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 45)
        self.fontJOUEUR = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 38)
        
        # Autre
        self.listeCouleur = ['jaune','rouge','rose','vert','orange','noir','bleu', 'marron','gris','violet']
        self.typePartie = None


      
      
    def afficherPopUpMulticolor(self):
        pygame.init() 
        self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Theme', self.background, 'fondPageAcceuil.png')),(0, 0))

        self.fenetre.blit(self.fontJOUEURTitre.render("Choisir une couleur", True, (0, 0, 0)), (250, 200))
        
        self.boutonRouge = Bouton(250,300,80,40,(220,20,60),"rouge",self.fenetre,15)
        self.boutonJaune = Bouton(250,350,80,40,(255,215,0),"jaune",self.fenetre,15)
        self.boutonRose = Bouton(350,300,80,40,(255,105,180),"rose",self.fenetre,15)
        self.boutonVert = Bouton(350,350,80,40,(34,139,34),"vert",self.fenetre,15)
        self.boutonOrange = Bouton(450,300,80,40,(255,165,0),"orange",self.fenetre,15)
        self.boutonNoir = Bouton(450,350,80,40,(105,105,105),"noir",self.fenetre,15)   
        self.boutonBleu = Bouton(550,300,80,40,(70,130,180),"bleu",self.fenetre,15)
        self.boutonMarron = Bouton(550,350,80,40,(160,82,45),"marron",self.fenetre,15)
        self.boutonGris = Bouton(650,300,80,40,(211,211,211),"gris",self.fenetre,15)
        self.boutonViolet = Bouton(650,350,80,40,(199,21,133),"violet",self.fenetre,15)

        pygame.display.update()    
                   
        
        return self.fenetre
    
    
    
    
    
    def attendreChoix(self) : 
        ''' Permet d'attendre que le joueur clique sur l'un des boutons pour sélectionner une couleur'''
    
        choixEffectue = False
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    self.afficherPopUpMulticolor()
                    if self.boutonJaune.verifier_click_bouton(positionClick):
                        choixEffectue = "jaune" 
                    if self.boutonRouge.verifier_click_bouton(positionClick):
                        choixEffectue = "rouge" 
                    if self.boutonRose.verifier_click_bouton(positionClick):
                        choixEffectue = "rose" 
                    if self.boutonVert.verifier_click_bouton(positionClick):
                        choixEffectue = "vert" 
                    if self.boutonOrange.verifier_click_bouton(positionClick):
                        choixEffectue = "orange" 
                    if self.boutonNoir.verifier_click_bouton(positionClick):
                        choixEffectue = "noir" 
                    if self.boutonBleu.verifier_click_bouton(positionClick):
                        choixEffectue = "bleu" 
                    if self.boutonMarron.verifier_click_bouton(positionClick):
                        choixEffectue = "marron" 
                    if self.boutonGris.verifier_click_bouton(positionClick):
                            choixEffectue = "gris" 
                    if self.boutonViolet.verifier_click_bouton(positionClick):
                        choixEffectue = "violet" 
                                
                        
                        
        return choixEffectue   

    
      
 
            
            
            
            
            
           
        
    