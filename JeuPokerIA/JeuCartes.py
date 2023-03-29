from __future__ import annotations
import random
from typing_extensions import Self

from Carte import Carte
from Carte import valeurs, familles

class JeuCartes() : 
    def __init__(self, nbCartes: int = 52): 
        self.nbCartes : int = nbCartes
        self.jeu : list[Carte] = []
        self.creerJeu() 
                
    def creerJeu(self) :
        '''On crée le paquet de Carte du Jeu, qui va nous servir à distribuer les cartes'''
        for valeur in valeurs :  #Couleur de la carte
            for famille in familles : 
                self.jeu.append(Carte(valeur,famille))
                
    def getJeu(self) : 
        '''Renvoi la liste des cartes du Jeu'''
        return self.jeu 
        
    def melanger(self) : 
        ''' Méthode qui mélange le paquet de carte du début '''
        return random.shuffle(self.jeu)
    
    # distribue 1 carte à 1 joueur
    def distribuerCarte(self) : 
        ''' Méthode qui permet de distribuer une carte à un joueur '''        
        return self.jeu.pop()

if __name__ == "__main__" : 
    print("-----------------------------------")    
    print("TEST :")
    jeu = JeuCartes()      
    cartes = jeu.getJeu()

    for carte in jeu.getJeu():
        print ("Famille : {0} - couleur : {1} - Valeur carte : {2}".format(carte.getFamille(), carte.getCouleur(), carte.getValeur()))

    print("Jeu de {0} cartes".format(len(cartes)))

    print("-----------------------------------")    