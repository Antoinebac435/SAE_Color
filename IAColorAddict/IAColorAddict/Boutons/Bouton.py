import pygame
import os

# --------------------------------------------------------------------------
# -- Cette classe permet de faire un bouton avec des dimensions choisies, --
# -- un emplacement décidé, une taille de police choisie ...              --
# -- et cela s'affichera sur la fenêtre                                   --
# --------------------------------------------------------------------------




class Bouton():
    def __init__(self,  x : int, y : int , largeur : int, hauteur : int, couleur : pygame.Color, texte : str, fenetre, policeTx : int, ombre : bool = False):
        
        
        
        self.fenetre = fenetre
        if ombre == True :
            self.rect = pygame.draw.rect(fenetre, pygame.Color("#384468"), (x, y, largeur+10, hauteur+10),  0, 5)
            
            
        self.rect = pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur),  0, 5)
        self.police = pygame.font.Font(os.path.join('ressources','policeEcriture', 'Grandstander-clean.ttf'),policeTx)
        
        
        self.texte = self.police.render(texte, True, pygame.Color("#384468"))
        texteCoordonees = self.texte.get_rect () 
        margeGauche = (largeur - texteCoordonees.width) / 2
        margeHauteur = (hauteur - texteCoordonees.height) / 2

        self.fenetre.blit(self.texte, (x + margeGauche, y + margeHauteur))
        pygame.display.update()
        
        
        

    def verifier_click_bouton(self, posClick):
        ''' Méthode qui va vérifier si le bouton a été cliqué '''
        if self.rect.colliderect(posClick):
            return True
        else:
            return False
