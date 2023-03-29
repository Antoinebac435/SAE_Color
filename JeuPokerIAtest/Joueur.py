import random
import pygame
from typing import List


from Carte import Carte
from typing import List


class Joueur ():
    def __init__(self, nom : str, gainsDepart: int, cheminImageAvatar: str, bot:str, niveau:str) :
        self.nom: str = nom
        self.piocheJoueur: List[Carte] = []
        self.derniereMise = None
        self.mainJoueur: List[Carte] = []
        self.gains: int = gainsDepart
        self.cheminImageAvatar = cheminImageAvatar
        self.imageAvatar = pygame.image.load(self.cheminImageAvatar)
        self.aPerdu = False
        self.bot : bool = bot
        self.niveau : str = niveau
        
    def viderMainJoueur(self):
        self.mainJoueur = []

    def donnerMainCarteJoueur(self, carte: Carte):
        self.mainJoueur.append(carte)

    def getCheminImageAvatar(self):
        return self.cheminImageAvatar

    def getAPerdu(self):
        return self.aPerdu

    def setAPerdu(self, aPerdu: bool):
       self.aPerdu = aPerdu

    def getImageAvatar(self):
        return self.imageAvatar
    
    def getNom(self):
        return self.nom

    def setGains(self, gains : int):
        self.gains = gains

    def getGains(self):
        return self.gains
        
    def getBot(self):
        return self.bot

    def setBot(self, bot : bool ):
        self.bot = bot

    def getNiveau(self):
        return self.niveau

    def setNiveau(self, niveau : str ):
        self.niveau = niveau
    
    def getMainJoueur(self):
        return self.mainJoueur
    
    def setMainJoueur(self, mainJoueur : List[Carte]):
        self.mainJoueur = mainJoueur
        
    # problème  
    def afficherMain(self) :
        for cartes in self.mainJoueur : 
            print(cartes.AfficheCarte())
        
    def setNom(self, nom : str ):
        self.nom = nom
        
    def __str__(self) -> str:
        
        return "nom :"+self.nom+ "main:"+str(self.mainJoueur) + "typeJoueur"+str(self.bot)
        
