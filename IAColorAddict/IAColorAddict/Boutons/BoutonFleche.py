import pygame

# ------------------------------------------------------------------------------
# -- Cette classe permet de faire un bouton en flèche (utile pour l'acceuil)  --
# ------------------------------------------------------------------------------



class BoutonFleche():
    def __init__(self, fenetre, point1:list[int], point2:list[int], point3:list[int], point4:list[int] ) -> None:
        self.fleche = pygame.draw.polygon(fenetre, (255,255,255), [point1, point2, point3, point4], 0)                                                                     
        pygame.display.update()
        
    def verifier_click_fleche(self, posClick):
        ''' Méthode qui va vérifier si le bouton a été cliqué '''

        if self.fleche.colliderect(posClick):
            return True
        else:
            return False
      