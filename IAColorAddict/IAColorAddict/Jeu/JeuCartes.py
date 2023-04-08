from __future__ import annotations
import random
from typing_extensions import Self

from Jeu.Carte import Carte




# --------------------------------------------------------------------------
# -- Cette classe permet de créer un jeu de cartes. Le jeu de carte       --
# -- est mélangé et distribué aux participants.                           --
# --------------------------------------------------------------------------



# Variables globales : 
couleurs = ['jaune','rouge','rose','vert','orange','noir','bleu', 'marron','gris','violet','multicolor']
titres = ['jaune','rouge','rose','vert','orange','noir','bleu', 'marron','gris','violet']





class JeuCartes() : 
    def __init__(self, nbCartes: int = 110): 
        self.nbCartes : int = nbCartes
        self.jeu : list[Carte] = []
        self.creerJeu() 
        
        self.carteMilieu : Carte = Carte("New","Carte")
        self.tab_CartesJoueurs : list[list[Carte]] = []
        
        
        
        
    def creerJeu(self) :
        '''On crée le paquet de Carte du Jeu, qui va nous servir à distribuer les cartes'''
        for couleur in couleurs :  #Couleur de la carte
            for titre in titres : 
                self.jeu.append(Carte(couleur,titre))
                
                
                
                
                
    def getJeu(self) : 
        '''Renvoi la liste des cartes du Jeu'''
        return self.jeu 





           
    def melanger(self) : 
        ''' Méthode qui mélange le paquet de carte du début '''
        return random.shuffle(self.jeu)
    
    
    
    
    
    
    def distribuerCarte(self) : 
        ''' Méthode qui permet de distribuer une carte à un joueur '''            
        dernierecarte = (self.jeu[-1])
        self.jeu.pop()
        return dernierecarte






    def distribuerJeu(self, nbJoueurs) : 
        ''' Méthode qui distribue les cartes du jeu pour chaque joueur '''
        
        self.carteMilieu : Carte = self.jeu.pop() 

        valeur = int(len(self.jeu) / nbJoueurs)

        for i in range(nbJoueurs) :
            self.tab_CartesJoueurs.append([])

            for j in range(valeur) :                
                carte = self.distribuerCarte()
                self.tab_CartesJoueurs[i].append(carte) 
                
                
        return self.carteMilieu, self.tab_CartesJoueurs 

        




                    

if __name__ == "__main__" : 

    JC = JeuCartes(110)
    print(len(JC.jeu))

    