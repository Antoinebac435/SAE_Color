import pygame
import os


# ------------------------------------------------------- 
# -- Cette classe permet d'insérer un texte dans       --
# -- une fenêtre avec la taille de police au choix     --
# -- , mais aussi la position donnée par l'utilisateur --
# ------------------------------------------------------- 




class Texte():
    def __init__(self, fenetre, texte :str, taillepolice : int, couleur, x : int, y : int) -> None:
        self.fenetre = fenetre
        self.police = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), taillepolice)
        texteRendu = self.police.render(texte, True, couleur)
        self.fenetre.blit(texteRendu, (x, y)) 
        
        