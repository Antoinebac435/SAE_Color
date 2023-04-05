import pygame


# --------------------------------------------------------------------------
# -- Cette classe permet de faire un bouton en forme de cercle (utile     --
# -- pour le logo quitter/croix.                                          --
# -- Elle a le même fonctionnement qu'un bouton normal                    --
# --------------------------------------------------------------------------




class Boutonc():
   def __init__(self, largeur : int, hauteur : int, couleur : pygame.Color, fenetre, radius:int):
      # fenetre = pygame.display.set_mode((900,700))

      self.fenetre = fenetre
      self.largeur = largeur
      self.hauteur = hauteur
      self.radius = radius

      self.cercle = pygame.draw.circle(fenetre,couleur,(largeur,hauteur),radius,1) # DRAW CIRCLE
 
      pygame.display.update()

   def verifier_click_bouton(self, posClick):
      ''' Méthode qui va vérifier si le bouton a été cliqué '''
      if self.cercle.colliderect(posClick):
         return True
      else:
         return False
