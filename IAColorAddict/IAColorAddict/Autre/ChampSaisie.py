import pygame
from Autre.TexteCentrer import TexteCenter





# ----------------------------------------------------------
# -- Cette classe permet d'avoir un espace de champ       --
# -- de saisie. L'utilisateur pourra taper dans ce champ  --
# -- et cela s'affichera sur la fenêtre                   --
# ----------------------------------------------------------



class ChampSaisie():
    def __init__(self, x : int, y : int , largeur : int, hauteur : int, couleur : pygame.Color, fenetre) :
        # Fenêtre et texte
        self.fenetre = fenetre
        self.texte = ""
        
        #Rectangle
        pygame.draw.rect(self.fenetre, couleur, ( x, y,largeur, hauteur),0, 40)
        pygame.draw.rect(self.fenetre, (0,0,0),( x, y, largeur, hauteur), 4, 45)
        
        #Nom joueur
        self.texteCenter = TexteCenter(fenetre, "Nom", 25 , hauteur, largeur, x , y, (0,0,0))
    
    
    
    
    
    def getTexte(self):
        '''Getter qui renvoi le texte'''
        return self.texte
    
    
    
    
    def verifierSaisie(self, key):
        ''' Méthode qui va vérifier si la lettre entrée est une lettre valide : 
            si elle correspond à une lettre de l'alphabet minuscule. 
            Si la lettre est valide ; on l'ajoute au mot à composer '''
            
        touche = pygame.key.name(key)
        
        if len(self.texte) < 20 and len(touche) == 1 and ("abcdefghijklmnopqrstuvwxyz1234567890".index(touche) >= 0):
            self.texte = self.texte + touche
            self.texteCenter.modifierText(self.texte) 
            
        elif key == pygame.K_BACKSPACE:
            self.texte = self.texte[:-1]
            self.texteCenter.modifierText(self.texte) 
     