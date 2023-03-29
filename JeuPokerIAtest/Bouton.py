import pygame

#button class
class Bouton():
    def __init__(self,  x : int, y : int , largeur : int, hauteur : int, couleur : pygame.Color, texte : str, fenetre, policeTx : int, ombre : bool = False):
        self.fenetre = fenetre
        if ombre == True :
            self.rect = pygame.draw.rect(fenetre, pygame.Color("#384468"), (x, y, largeur+10, hauteur+10),  0, 5)

        self.rect = pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur),  0, 5)
        police = pygame.font.Font("policeEcriture/Grandstander-clean.ttf",policeTx)
        self.texte = police.render(texte, True, pygame.Color("#384468"))
        texteCoordonees = self.texte.get_rect () 
        margeGauche = (largeur - texteCoordonees.width) / 2
        margeHauteur = (hauteur - texteCoordonees.height) / 2

        self.fenetre.blit(self.texte, (x + margeGauche, y + margeHauteur))
        pygame.display.update()

    def verifier_click_bouton(self, posClick):
        if self.rect.colliderect(posClick):
            return True
        else:
            return False

# pygame.init()
# screen = pygame.display.set_mode((900, 562))
          
# pygame.display.set_caption("Créer un jeu avec PyGame")
# rec = Bouton(650,200,200,50,(255,255,255),"lulu juju",screen)
# run = True
# while run:
#     for event in pygame.event.get():
#         if (event.type == pygame.MOUSEBUTTONDOWN):
#             positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
#             if rec.verifier_click_bouton(positionClick):
#                 print ("dkdd")
#         elif (event.type == pygame.QUIT):
#             run = False  
    
 
    
