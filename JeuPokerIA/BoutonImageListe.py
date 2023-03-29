import pygame

from BoutonFleche import BoutonFleche
from TexteCentrer import TexteCenter
from typing import List

class BoutonImageListe():
    def __init__(self, titre: str, listChoixImages: List[str], x: int, y: int, largeur: int, hauteur: int, couleur: pygame.Color, fenetre) -> None:
        # fenetre
        self.fenetre = fenetre

        # variable
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur = couleur
        self.x = x
        self.y = y

        # liste
        self.listChoixImages = listChoixImages
        self.index: int = 0

        # Logo
        self.afficherAvatar()
        
        # Titre        
        texte = TexteCenter(self.fenetre, titre, 25,
                            self.hauteur-170, largeur, x, y, (255, 255, 255))

        # fleche
        self.fleche_gauche = BoutonFleche(
            fenetre, [x + 45, y + 20], [x+85, y+self.hauteur-5], [x+80, y+20], [x+85, y])
        self.fleche_droite = BoutonFleche(
            fenetre, [x + 300, y + 20], [x+260, y+self.hauteur-5], [x+265, y+20], [x+260, y])
        pygame.display.update()
        
    def getImageAvatar(self):
        return self.listChoixImages[self.index]

    def changerListeDroite(self):
        self.index = self.index+1
        if self.index > len(self.listChoixImages)-1:
            self.index = 0
        self.afficherAvatar()

    def changerListeGauche(self):

        self.index = self.index-1
        if self.index < 0:
            self.index = len(self.listChoixImages)-1
        self.afficherAvatar()
        
    def afficherAvatar(self):
        imageAvatarPath = "./images/Avatar/" + self.listChoixImages[self.index]
        imageAvatar = pygame.image.load(imageAvatarPath)
        posImageAvatar = imageAvatar.get_rect()
        posImageAvatar.x = (self.largeur - posImageAvatar.width) / 2 + self.x
        posImageAvatar.y = (self.hauteur - posImageAvatar.height) / 2 + self.y
 
        posXcercle = (posImageAvatar.width / 2) + posImageAvatar.x
        posYcercle = (posImageAvatar.width / 2) + posImageAvatar.y     
        
        pygame.draw.circle(self.fenetre, self.couleur, (posXcercle, posYcercle), (posImageAvatar.height / 2) + 15)
        pygame.draw.circle(self.fenetre, (0,0,0), (posXcercle, posYcercle), (posImageAvatar.height / 2) + 15, 3)        
        self.fenetre.blit(imageAvatar,  posImageAvatar)
        pygame.display.update()
        
    def verifierClickDeplacement(self, positionClick):
         if self.fleche_droite.verifier_click_fleche(positionClick) == True:
            self.changerListeDroite()
         elif self.fleche_gauche.verifier_click_fleche(positionClick) == True:
            self.changerListeGauche() 

    def verifierPositionSurBoutonFleche(self, position):
         return self.fleche_droite.verifier_click_fleche(position) or self.fleche_gauche.verifier_click_fleche(position)

# pygame.init()
# screen = pygame.display.set_mode((900, 562))
# pygame.display.set_caption("Créer un jeu avec PyGame")
# background_image = "./images/PageAcceuil/fondPageAcceuil.png"
# background = pygame.image.load(background_image).convert()
# screen.blit(background, (0,0))
# rec = BoutonList("Nombre de joueurs",["4","5","6"],280,80,350,45,(243,223,36),screen)

# pygame.display.update()

# run = True
# while run:
#     for event in pygame.event.get():
#         if (event.type == pygame.MOUSEBUTTONDOWN):
#             positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
#             if rec.fleche_droite.verifier_click_fleche(positionClick) == True:
#                     rec.changerListeDroite()
#             elif rec.fleche_gauche.verifier_click_fleche(positionClick) == True:
#                     rec.changerListeGauche()
#         elif (event.type == pygame.QUIT):
#             run = False
