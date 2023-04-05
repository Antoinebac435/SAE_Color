from __future__ import annotations
import random
from typing_extensions import Self




# --------------------------------------------------------------------------
# -- Cette classe permet de créer une carte. Une carte est identifiée     --
# -- par sa couleur et son titre                                          --
# --------------------------------------------------------------------------







# Variables globales : 
couleurs = ['jaune','rouge','rose','vert','orange','noir','bleu', 'marron','gris','violet','multicolor']
titres = ['jaune','rouge','rose','vert','orange','noir','bleu', 'marron','gris','violet']



class Carte() : 
    def __init__(self : Self, couleur : str, titre : str):
        if couleur and titre in couleurs : 
            self.couleur : str = couleur 
            self.titre : str  = titre 
            
    def getCouleur(self) : 
        ''' Méthode qui permet d'avoir la couleur d'une carte'''
        return self.couleur
    
    def getTitre(self) : 
        ''' Méthode qui permet d'avoir le titre d'une carte'''
        return self.titre 
    
    def AfficheCarte(self) :
        return "Carte " + self.couleur + " de type " + self.titre
        
    





if __name__ == "__main__" : 
    c = Carte("rose","vert") 
    print("La couleur de la carte cree est" ,c.getCouleur())
    print("Le titre de la carte cree est" ,c.getTitre())
    # ------- 
    print("\n")
