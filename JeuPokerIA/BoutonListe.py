import pygame

from BoutonFleche import BoutonFleche
from TexteCentrer import TexteCenter
from typing import List

class BoutonListe():
    def __init__(self, titre : str , taillePolice : int, listChoix : List[str], x : int, y : int , largeur : int, hauteur : int, couleur : pygame.Color, fenetre) -> None:
        #fenetre
        self.fenetre = fenetre
        
        # variable
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur = couleur
        self.taille = taillePolice
        self.x = x
        self.y = y
        
       # rectangle
        #self.s = pygame.draw.rect(fenetre, couleur, ( x, y,largeur, self.hauteur),0, 40)
        #rectContour = pygame.draw.rect(fenetre, (0,0,0),( x, y,largeur, self.hauteur), 4, 45)
        
        #Titre
        texte = TexteCenter(self.fenetre,titre, 25, self.hauteur-100, largeur, x , y , (255,255,255))

        # fleche
        self.fleche_gauche = BoutonFleche(fenetre, [x -80, y +20], [x-40, y+self.hauteur-5], [x-45, y+20], [x-40, y])
        self.fleche_droite = BoutonFleche(fenetre, [x + 400, y +20], [x+360, y+self.hauteur-5], [x+365, y+20], [x+360, y])
        
        #liste
        self.listChoix = listChoix
        self.index : int = 0
        self.afficherTexte()

        pygame.display.update()
        
    def getChoix(self):
        return self.listChoix[self.index]   
         
    def changerListeDroite(self):
        self.index = self.index+1
        if self.index > len(self.listChoix)-1:
            self.index = 0
        self.afficherTexte()

    def changerListeGauche(self):
        self.index = self.index-1
        if self.index < 0:
            self.index = len(self.listChoix)-1
        self.afficherTexte()

    def afficherTexte(self):
        rect = pygame.draw.rect(self.fenetre, self.couleur, ( self.x, self.y,self.largeur, self.hauteur),0, 40)
        rectContour = pygame.draw.rect(self.fenetre, (0,0,0),( self.x, self.y, self.largeur, self.hauteur), 4, 45)
        texte = TexteCenter(self.fenetre,self.listChoix[self.index], self.taille , self.hauteur, self.largeur, self.x , self.y, (0,0,0) )

    def verifierClickDeplacement(self, positionClick):
         if self.fleche_droite.verifier_click_fleche(positionClick) == True:
            self.changerListeDroite()
            return True
         elif self.fleche_gauche.verifier_click_fleche(positionClick) == True:
            self.changerListeGauche()       
            return True 

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
