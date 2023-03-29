import pygame
from typing import List

class BoutonFleche():
    def __init__(self, fenetre, point1:List[int], point2:List[int], point3:List[int], point4:List[int] ) -> None:
        self.fleche = pygame.draw.polygon(fenetre, (255,255,255), [point1, point2, point3, point4], 0)                                                                     
        pygame.display.update()
        
    def verifier_click_fleche(self, posClick):
        if self.fleche.colliderect(posClick):
            return True
        else:
            return False
        
# pygame.init()
# screen = pygame.display.set_mode((900, 700))
# pygame.display.set_caption("Créer un jeu avec PyGame")
# background_image = "./images/PageAcceuil/fondPageAcceuil.png"
# background = pygame.image.load(background_image).convert()
# screen.blit(background, (0,0))  
# fleche_gauche = BoutonFleche(screen, [0, 65], [40, 90], [35, 65], [40, 40])
# fleche_gauche = BoutonFleche(screen, [400, 900], [350, 650], [400, 900], [700, 100])
# pygame.display.update()

# run = True
# while run:
#     for event in pygame.event.get():
#         if (event.type == pygame.QUIT):
#             run = False  
    