from __future__ import annotations
from typing_extensions import Self


# Variables globales : 
# valet : 11 - dame : 12 - roi : 13 - as : 14
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
familles = ['coeur','carreau','trefle','pique']

class Carte() : 
    def __init__(self : Self, valeur : int, famille : str):
        if valeur in valeurs : 
            self.valeur : int = valeur 
        
        if famille in familles :
            self.famille : str  = famille 
            
    def getValeur(self)->int: 
        return self.valeur
    
    def getFamille(self)->str: 
        return self.famille 

    def getCouleur(self)->str:
        couleur = None
        if self.famille == 'coeur' or self.famille == 'pique':
            couleur = 'rouge'
        else:
            couleur = 'noir'

        return couleur

    def AfficheCarte(self) :
        return "Carte " + self.valeur + " de famille " + self.famille
        
if __name__ == "__main__" : 

    print("TEST :")

    carte = Carte(2, "pique") 

    print("Création carte (2 de pique) :")
    print("Sa valeur est" , carte.getValeur())
    print("Sa famille est" ,carte.getFamille())
    print("Sa couleur est" ,carte.getCouleur())

    print("-----------------------------------")
