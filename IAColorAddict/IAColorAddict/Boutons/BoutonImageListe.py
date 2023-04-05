import pygame

from Boutons.BoutonFleche import BoutonFleche
from Autre.TexteCentrer import TexteCenter
import os



# --------------------------------------------------------------------------
# -- Cette classe permet de faire un Bouton, un Composant, qui affiche    --
# -- une image au milieu avec des flèches sur les côtés. Ces flèches      --
# -- permettent lorsque l'on clique dessus, de passer d'une image à une   -- 
# -- autre.                                                               --
# --------------------------------------------------------------------------


class BoutonImageListe():
    
    def __init__(self, titre: str, listChoixImages: list[str], x: int, y: int, largeur: int, hauteur: int, couleur: pygame.Color, fenetre) :
        # Fenêtre
        self.fenetre = fenetre

        # Variable
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur = couleur
        self.x = x
        self.y = y

        # Liste
        self.listChoixImages = listChoixImages
        self.index: int = 0

        # Logo
        self.afficherAvatar()
        
        # Titre        
        texte = TexteCenter(self.fenetre, titre, 25,self.hauteur-170, largeur, x, y, (255, 255, 255))

        # fleche
        self.fleche_gauche = BoutonFleche(
            fenetre, [x + 45, y + 20], [x+85, y+self.hauteur-5], [x+80, y+20], [x+85, y])
        self.fleche_droite = BoutonFleche(
            fenetre, [x + 300, y + 20], [x+260, y+self.hauteur-5], [x+265, y+20], [x+260, y])
        pygame.display.update()
        
        
        
    def getImageAvatar(self):
        ''' Méthode qui permet d'avoir l'avatar sous la forme "avatar.png". 
        Cela correspond à l'avatar choisi par l'utilisateur dans la page PageChoixJouer '''
        return self.listChoixImages[self.index]
    
    

    def changerListeDroite(self):
        ''' Méthode qui va incrémenter la liste. 
            Cette méthode va être utilisée quand on cliquer sur la flèche de droite. ''' 
        
        self.index = self.index+1
        if self.index > len(self.listChoixImages)-1:
            self.index = 0
        self.afficherAvatar()





    def changerListeGauche(self):
        ''' Méthode qui va décrémenter la liste. 
            Cette méthode va être utilisée quand on cliquer sur la flèche de gauche. ''' 

        self.index = self.index-1
        if self.index < 0:
            self.index = len(self.listChoixImages)-1
        self.afficherAvatar()
        
        
        
        
        
    def afficherAvatar(self):
        ''' Méthode qui va afficher l'avatar au milieu'''
        imageAvatarPath = os.path.join('ressources', 'avatar',self.listChoixImages[self.index] )
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
        ''' Méthode qui va vérifier si l'une des flèches a été cliquée et bouger la liste en fonction'''
        
        if self.fleche_droite.verifier_click_fleche(positionClick) == True:
            self.changerListeDroite()
        elif self.fleche_gauche.verifier_click_fleche(positionClick) == True:
            self.changerListeGauche()         

