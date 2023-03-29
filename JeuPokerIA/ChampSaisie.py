import pygame

from TexteCentrer import TexteCenter


class ChampSaisie():
    def __init__(self, x : int, y : int , largeur : int, hauteur : int, couleur : pygame.Color, fenetre) -> None:
        self.fenetre = fenetre
        self.texte = ""
        
        #rectangle
        pygame.draw.rect(self.fenetre, couleur, ( x, y,largeur, hauteur),0, 40)
        pygame.draw.rect(self.fenetre, (0,0,0),( x, y, largeur, hauteur), 4, 45)
        #nom joueur
        self.texteCenter = TexteCenter(fenetre, "Nom", 25 , hauteur, largeur, x , y, (0,0,0))
    
    def getTexte(self):
        return self.texte
    
    def verifierSaisie(self, key):
        touche = pygame.key.name(key)
        if len(self.texte) < 20 and len(touche) == 1 and ("abcdefghijklmnopqrstuvwxyz1234567890".index(touche) >= 0):
            self.texte = self.texte + touche
            self.texteCenter.modifierText(self.texte) 
        elif key == pygame.K_BACKSPACE:
            self.texte = self.texte[:-1]
            self.texteCenter.modifierText(self.texte) 
     