# import pygame

# #button class
# class Boutonc():
#     def __init__(self,  x : int, y : int , largeur : int, hauteur : int, couleur : pygame.Color, texte : str, fenetre, radius:int):
#         window = pygame.display.set_mode((500,500))
        
#         radius = 10
        
#         self.fenetre = fenetre
#         self.radius = 10
#         self.largeur = 100
#         self.hauteur = 100
#         self.cercle = pygame.draw.circle(fenetre, pygame.Color("#384468"), ( largeur, hauteur),radius)
#         self.cercle = pygame.draw.circle(fenetre, couleur, (largeur, hauteur), radius)
#         # police = pygame.font.Font("./policeEcriture/Grandstander-clean.ttf",30)
#         # self.texte = police.render(texte, True, pygame.Color("#384468"))
#         # texteCoordonees = self.texte.get_circle () 
#         # margeGauche = (largeur - texteCoordonees.width) / 2
#         # margeHauteur = (hauteur - texteCoordonees.height) / 2
        
        

#         # self.fenetre.blit(self.texte, (x + margeGauche, y + margeHauteur))
#         pygame.display.update()

#     def verifier_click_bouton(self, posClick):
#         if self.rect.colliderect(posClick):
#             return True
#         else:
#             return False


import pygame
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
      if self.cercle.colliderect(posClick):
         return True
      else:
         return False
