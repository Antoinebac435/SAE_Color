import pygame

from Boutons.BoutonFleche import BoutonFleche
from Autre.TexteCentrer import TexteCenter





# --------------------------------------------------------------------------
# -- Cette classe permet de faire un Bouton, un Composant, qui affiche    --
# -- un texte. Ce texte va changer quand on va cliquer sur les flèches    --
# -- de droites ou de gauches, c'est un carrousel avec 2 mots.            -- 
# --------------------------------------------------------------------------







class BoutonListe():
    def __init__(self, titre : str , taillePolice : int, listChoix : list[str], x : int, y : int , largeur : int, hauteur : int, couleur : pygame.Color, fenetre) : 
        #fenetre
        self.fenetre = fenetre
        
        # variable
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur = couleur
        self.taille = taillePolice
        self.x = x
        self.y = y
        

    
        # fleche
        self.fleche_gauche = BoutonFleche(fenetre, [x -80, y +20], [x-40, y+self.hauteur-5], [x-45, y+20], [x-40, y])
        self.fleche_droite = BoutonFleche(fenetre, [x + 400, y +20], [x+360, y+self.hauteur-5], [x+365, y+20], [x+360, y])
        
        texte = TexteCenter(self.fenetre,titre, 25, self.hauteur-100, largeur, x , y , (255,255,255))

        #liste
        self.listChoix = listChoix
        self.index : int = 0
        self.afficherTexte()

        pygame.display.update()
        
        
        
        
    def getChoix(self): 
        ''' Méthode qui permet d'avoir le choix de l'utilisateur dans la page PageChoixJouer. 
        Elle permet d'avoir si le joueur a choisi un ordre ; Aléatoire ou Dans l'ordre '''
        return self.listChoix[self.index]   
         
         
         
    def changerListeDroite(self):
        ''' Méthode qui va incrémenter la liste. 
            Cette méthode va être utilisée quand on cliquer sur la flèche de droite. ''' 
        
        self.index = self.index+1
        if self.index > len(self.listChoix)-1:
            self.index = 0
        self.afficherTexte()





    def changerListeGauche(self):
        ''' Méthode qui va décrémenter la liste. 
            Cette méthode va être utilisée quand on cliquer sur la flèche de gauche. ''' 
        
        self.index = self.index-1
        if self.index < 0:
            self.index = len(self.listChoix)-1
        self.afficherTexte()
        
        
        
        

    def afficherTexte(self):
        ''' Méthode qui permet d'afficher le texte. '''
        rect = pygame.draw.rect(self.fenetre, self.couleur, ( self.x, self.y,self.largeur, self.hauteur),0, 40)
        rectContour = pygame.draw.rect(self.fenetre, (0,0,0),( self.x, self.y, self.largeur, self.hauteur), 4, 45)
        texte = TexteCenter(self.fenetre,self.listChoix[self.index], self.taille , self.hauteur, self.largeur, self.x , self.y, (0,0,0) )




    def verifierClickDeplacement(self, positionClick):
        ''' Méthode qui va vérifier si l'une des flèches a été cliquée et bouger la liste en fonction'''
        if self.fleche_droite.verifier_click_fleche(positionClick) == True:
            self.changerListeDroite()
            return True
        elif self.fleche_gauche.verifier_click_fleche(positionClick) == True:
            self.changerListeGauche()       
            return True 
        
        
