import pygame

import os


# --------------------------------------------------------
# -- Cette classe permet d'insérer un texte dans        --
# -- une fenêtre avec la taille de police au choix      --
# -- , mais aussi la position donnée par l'utilisateur. -- 
# -- Elle permet aussi d'ajuster cet texte pour qu'il   -- 
# -- soit centrée dans la fenêtre.                      --
# --------------------------------------------------------




class TexteCenter():
    def __init__(self, fenetre, texte : int , taillePolice : int, hauteur : int , largeur, x: int , y : int, couleur ) :

        self.fenetre = fenetre
        self.texte = texte
        self.couleur = couleur
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = x
        self.y = y
                
        self.police = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), taillePolice)
        self.afficherTexte()
        
        
        
    def modifierText(self, texte: str):
        # Effacer zone de texte (dans le cas où y a déjà du texte)
        pygame.draw.rect(self.fenetre, (243,223,36), self.positionSave)   

        self.texte = texte
        self.afficherTexte()
        
    def afficherTexte(self):
        # Affiche le texte dans la fenêtre
        
        
        texteRendu = self.police.render(self.texte, True, self.couleur)
        posTexte = texteRendu.get_rect()
        
        
        margeGauche = (self.largeur - posTexte.width) / 2
        margeHauteur = (self.hauteur - posTexte.height) / 2

        self.fenetre.blit(texteRendu, (self.x + margeGauche, self.y + margeHauteur)) 
        
        self.positionSave = posTexte
        self.positionSave.x = self.x + margeGauche 
        self.positionSave.y = self.y + margeHauteur
        
        pygame.display.update()       
