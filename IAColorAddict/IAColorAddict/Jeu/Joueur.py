import random

from Jeu.Carte import Carte



# -----------------------------------------------------------------------------------------------
# -- Cette classe permet de créer n joueur. Un joueur est identifiable par rapport à son nom.  --
# -- Il possède une main (3 cartes visibles) et une pioche (cartes non visibles).              --
# -----------------------------------------------------------------------------------------------



class Joueur ():
    def __init__(self, nom : str, typeJoueur : str, niveau_ia : str) :
        self.nom: str = nom
        self.piocheJoueur: list[Carte] = []
        self.mainJoueur: list[Carte] = []
        self.typeJoueur = typeJoueur
        self.niveau_ia = niveau_ia

    def estIA(self) : 
        if self.typeJoueur[0:2] == "IA" : 
            return True 
        else : 
            return False
        
    def getNiveauIa(self) : 
        return self.niveau_ia

    def getPiocheJoueur(self):
        '''Méthode qui permet d'avoir la pioche d'un joueur'''
        return self.piocheJoueur
    
    def getNom(self):
        ''' Méthode qui permet d'avoir le nom d'un joueur'''

        return self.nom
    
    def getMainJoueur(self):
        ''' Méthode qui permet d'avoir la main d'un joueur (3 cartes +-)'''

        return self.mainJoueur
    
    def setMainJoueur(self, mainJoueur : list[Carte]):
        ''' Méthode qui permet de modifier la main d'un joueur'''

        self.mainJoueur = mainJoueur
        
    def setPiocheJoueur(self, piocheJoueur : list[Carte]):
        ''' Méthode qui permet de modifier la pioche d'un joueur'''

        self.piocheJoueur = piocheJoueur
        
        
    def afficherMain(self) :
        ''' Méthode qui permet d'afficher la main d'un joueur (3 cartes +-)'''

        for cartes in self.mainJoueur : 
            return (cartes.AfficheCarte())
        
    def setNom(self, nom : str ):
        ''' Méthode qui permet de modifier le nom d'un joueur'''

        self.nom = nom
        
    def piochePossible(self) : 
        if( (len(self.piocheJoueur) > 0) or (len(self.mainJoueur) < 4)):
            return True 
        else : 
            return False
    
        

    def piocherCarteSiPossible(self):
        ''' Méthode qui va piocher une carte dans la pioche du Joueur SEULEMENT si cela est possible '''
        if( (len(self.piocheJoueur) > 0) and (len(self.mainJoueur) < 6)):
           self.piocherCarte()
           
    def piocherCarte(self):
        ''' Méthode qui va piocher une carte dans la pioche du Joueur '''
        cartePiocher = random.choice(self.piocheJoueur)
        self.mainJoueur.append(cartePiocher)
        self.piocheJoueur.remove(cartePiocher)
        
        
    def __str__(self):
        
        return "nom :"+self.nom+ "main:"+str(self.mainJoueur)+"pioche:"+str(self.piocheJoueur)
        
