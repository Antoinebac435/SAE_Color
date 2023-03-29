import random
import time

import pygame
from Carte import Carte
from ChampSaisieMise import ChampSaisieMise
from JeuCartes import JeuCartes
from Joueur import Joueur
from Bouton import Bouton
from PopUp import PopUp
from Texte import Texte
from TexteCentrer import TexteCenter
from typing import List
import random 
from PageChoixJouer import PageChoixJouer

class PageJeu():
    
    def __init__(self, listeJoueurs : List[Joueur], fenetre, background_image: str) :         
        self.listeJoueurs : List[Joueur] = listeJoueurs     # Liste des joueurs qui peuvent encore jouer
        self.listeJoueursPerdus : List[Joueur] = []         # Liste des joueurs qui ont perdu définitivement
        self.listeIndicesJoueursManche : List[int]  = []    # Liste des indices des joueurs de la manche qui ne sont pas couché
        self.listeJoueursCouchesTour: List[Joueur] = []       # Liste des joueurs qui se sont couchés dans le tour
        self.listeIndicesJoueursSansGains : List[int]  = [] # Liste des indices des joueurs qui ne peuvent plus miser        
        self.listeMisesJoueursTour: List[int] = []          # Liste des mises des joueurs sur le tour
        self.listeMisesJoueursManche: List[int] = []        # Liste des mises des joueurs sur la manche
        self.misesJoueursCouches: int = 0                   # Mises de tous les joueurs qui se sont couchés
        self.indiceJoueurCourant : int = 0 # Indice du joueur en cours
        self.options : str
        self.manche = 0
        self.tour = 0
        self.plusGrosseMise = None
        self.listeTabCartesMilieu: List[Carte] = [] # Cartes au milieu
 
        self.fenetre = fenetre
        self.background_image = background_image        
        self.dosDeCartes = pygame.image.load("./Images/Cartes/dosDeCartes.png")
                    
        self.background = pygame.image.load(self.background_image).convert()                
                
        # Créer une page pour le passage au joueur suivant
        self.popUpJoueurSuivant = PopUp(self.background)

    # Affichage d'un message de démarage de la manche pendant 2s
    def afficherMessageDemarrageManche(self):
        self.fenetre.blit(self.background,(0, 0))    
        
        joueur: Joueur = self.getJoueurCourant()
        TexteCenter(self.fenetre, "C'est au tour de {0}".format(joueur.getNom()), 40, 15, 900, 0, 100, (4,32,106))
        imageAvatar = pygame.transform.scale(joueur.getImageAvatar(), (100, 100))
        self.fenetre.blit(imageAvatar,(400, 150))

        TexteCenter(self.fenetre, "Premier tour de la manche", 45, 15, 900, 0, 370, (255,255,255)) 
        TexteCenter(self.fenetre, str(self.manche), 55, 15, 900, 0, 470, (4,32,106))

        TexteCenter(self.fenetre, "Appuyer sur une touche pour continuer", 25, 15, 900, 0, 600, (4,32,106))

        pygame.display.update()    
        self.attendreAppuiTouche()

    # Démarrage d'une nouvelle manche
    def demarrerNouvelleManche(self)->str:
       
        self.jeuCartes : JeuCartes = JeuCartes()    # Création d'un jeu de cartes   

        # On mélange et distributer deux cartes à chacun des joueurs    
        self.jeuCartes.melanger()

         # on initalise les mises de la manche et du tour
        self.listeIndicesJoueursManche = []
        self.listeMisesJoueursTour = []
        self.listeMisesJoueursManche = []
        self.listeTabCartesMilieu = []
        self.listeJoueursCouchesTour = []
        self.misesJoueursCouches = 0
                
        nouvelleListeJoueurs = []

        indiceJoueur = 0
        for joueur in self.listeJoueurs:
            # On prend que les joueurs qui sont encore dans la course
            if (joueur.getAPerdu() == False):
                nouvelleListeJoueurs.append(joueur)
                
                self.listeIndicesJoueursManche.append(indiceJoueur)   # Indice des joueurs de la manche
                self.listeMisesJoueursTour.append(0)
                self.listeMisesJoueursManche.append(0)
                indiceJoueur = indiceJoueur + 1
            else:
                # on stocker la liste des joueurs qui peuvent plus jouer
                if (joueur not in self.listeJoueursPerdus):
                    self.listeJoueursPerdus.append(joueur)

        self.manche = self.manche + 1   # Nouvelle manche

        # On va changer l'ordre des joueurs si on est pas sur la première manche                
        if (self.manche > 1):
            nouvelleListeJoueursTriees = nouvelleListeJoueurs.copy()
            # on décale l'ordre des joueurs
            for indiceJoueur in range(0, len(nouvelleListeJoueurs)):
                if (indiceJoueur < len(nouvelleListeJoueurs) - 1):
                    nouvelleListeJoueursTriees[indiceJoueur + 1] = nouvelleListeJoueurs[indiceJoueur]
                else:
                   nouvelleListeJoueursTriees[0] = nouvelleListeJoueurs[indiceJoueur]      # le dernier passera en premier dans la liste
            nouvelleListeJoueurs = nouvelleListeJoueursTriees
            print("nouvelleListeJoueurs", nouvelleListeJoueurs)
        self.listeJoueurs = nouvelleListeJoueurs

        # chaque joueurs prend deux cartes
        for joueur in self.listeJoueurs:
            joueur.viderMainJoueur()
            for i in range (0,2):
                joueur.donnerMainCarteJoueur(self.jeuCartes.distribuerCarte())

        # au départ on prend 5 cartes dans le jeu 
        for i in range (0, 5):
                self.listeTabCartesMilieu.append(self.jeuCartes.jeu[i])                
                self.jeuCartes.jeu.remove(self.jeuCartes.jeu[i])
                
        # On définit la mise de départ qui sera de 50
        self.plusGrosseMise = 50

        self.tour = 1   # premier tour
        self.indiceJoueurCourant = 0    # premier joueur qui va commencer

        self.afficherMessageDemarrageManche()   # affichage du message de démarrage de la manche
        return self.afficherJeuJoueur()         # on affiche le plateau pour le joueur

    # on affiche les joueurs sur le plateau
    def afficherJoueurs(self):
        positionXCarte = 100
        
        
        for indiceJoueur in range (0,len(self.listeJoueurs)):
            joueur = self.listeJoueurs[indiceJoueur]
            if (joueur.getAPerdu() == False):
                nom = joueur.getNom()

                if (joueur in self.listeJoueursCouchesTour):
                    # Si le joueur s'est couché, on affiche directement ses gains comme on a déjà retiré sa mise sur ses gains
                    gain = str(joueur.getGains())
                else:
                    gain = str(joueur.getGains() - self.listeMisesJoueursManche[indiceJoueur])

                imageAvatar = pygame.image.load(joueur.getCheminImageAvatar())

                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)  
                if (indiceJoueur == self.indiceJoueurCourant):                 
                    pygame.draw.circle(self.fenetre, (r,g,b), (660, 560), 50)
                    pygame.draw.circle(self.fenetre, (0,0,0), (660, 560), 50,3)
                    TexteCenter(self.fenetre,nom, 15, 15, 75, 625, 620, (255,255,255))
                    TexteCenter(self.fenetre,gain, 15, 15, 75, 625, 490, (255,255,255))
                    self.fenetre.blit(imageAvatar, (620, 520))      
                
                else:
                    pygame.draw.circle(self.fenetre, (r,g,b), (positionXCarte+36, 120), 50)
                    pygame.draw.circle(self.fenetre, (0,0,0), (positionXCarte+36, 120), 50,3)
                
                    TexteCenter(self.fenetre,nom, 15, 15, 75, positionXCarte, 180, (255,255,255))
                    TexteCenter(self.fenetre,gain, 15, 15, 75, positionXCarte, 50, (255,255,255))

                    # On va vérifier si le joueur est encore dans la manche
                    alpha = 255
                    couleur = (0, 0, 0)
                    # si le joueur n'est plus dans la manche il apparaitra plus clair
                    if (indiceJoueur not in self.listeIndicesJoueursManche):
                        alpha = 50
                        couleur = (255, 255, 255)

                    imageAvatar.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
                    pygame.draw.circle(self.fenetre, couleur, (positionXCarte+36, 120), 50,3)

                    self.fenetre.blit(imageAvatar, (positionXCarte-1, 80))      
                    self.fenetre.blit(self.dosDeCartes, (positionXCarte + 100, 50))            
                    positionXCarte = positionXCarte + 250
            
        # On affiche la liste des joueurs qui ont perdus et qui sont plus dans le jeu
        positionY = 250
        for joueur in self.listeJoueursPerdus:
            imageAvatar = pygame.image.load(joueur.getCheminImageAvatar())
            self.fenetre.blit(imageAvatar, (30, positionY))         
            pygame.draw.circle(self.fenetre, (50,50,50), (70, positionY + 40), 50)
            TexteCenter(self.fenetre, joueur.getNom(), 15, 15, 75, 35, positionY + 95, (255,255,255))
            imageAvatar.fill((255, 255, 255, 100), None, pygame.BLEND_RGB_MULT)
            self.fenetre.blit(imageAvatar, (35, positionY))    
            positionY = positionY + 150

    def TourBotFacile(self): 
        choix = random.randint(0, 100)
        print("choix:",choix)

        if choix > 0 and choix <= 5 :
            print ("coucher")
            self.listeIndicesJoueursManche.remove(self.indiceJoueurCourant)
            mise = self.listeMisesJoueursManche[self.indiceJoueurCourant]
            # Si jamais misé et le joueur se couche
            if (self.tour == 1 and self.listeMisesJoueursManche[self.indiceJoueurCourant] == 0):
                # Le premier joueur perdra 50 de ses gains
                if (self.indiceJoueurCourant == 0):
                    mise = 50      
                # Le deuxième joueur perdra 25 de ses gains
                elif (self.indiceJoueurCourant == 1):
                    mise = 25               
            self.appliquerMiseGainJoueur(mise)
            self.listeJoueursCouchesTour.append(self.getJoueurCourant())               
            self.listeMisesJoueursTour[self.indiceJoueurCourant] = 0
            self.listeMisesJoueursManche[self.indiceJoueurCourant] = 0
                       
        if choix > 5 and choix <= 25:
            print ("miser")
            if self.listeJoueurs[self.indiceJoueurCourant].getGains() > self.plusGrosseMise :
                miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                self.renseignerMiseJoueurTour(miseSaisie)
                self.plusGrosseMise = miseSaisie
            else :
                self.renseignerMiseJoueurTour(self.plusGrosseMise)
                
        if choix > 25 and choix <= 100:
            print ("suivre")
            self.renseignerMiseJoueurTour(self.plusGrosseMise)

    def conditionverificationtour2(self):
        print("robot au 2 tour")
        if self.jeuAvecPair(self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur()) :#>= 6:
            print("robot a pair >6")
            choix = random.randint(0, 100)
            print(choix)
            if (choix >0 and choix <75):
                self.renseignerMiseJoueurTour(self.plusGrosseMise)
            if (choix > 75 and choix <95):
                miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                self.renseignerMiseJoueurTour(miseSaisie)
                self.plusGrosseMise = miseSaisie
            else:
                self.listeIndicesJoueursManche.remove(self.indiceJoueurCourant)
                mise = self.listeMisesJoueursManche[self.indiceJoueurCourant]
                # Si jamais misé et le joueur se couche
                if (self.tour == 1 and self.listeMisesJoueursManche[self.indiceJoueurCourant] == 0):
                        # Le premier joueur perdra 50 de ses gains
                    if (self.indiceJoueurCourant == 0):
                        mise = 50      
                    # Le deuxième joueur perdra 25 de ses gains
                    elif (self.indiceJoueurCourant == 1):
                        mise = 25               
                self.appliquerMiseGainJoueur(mise)
                self.listeJoueursCouchesTour.append(self.getJoueurCourant())               
                self.listeMisesJoueursTour[self.indiceJoueurCourant] = 0
                self.listeMisesJoueursManche[self.indiceJoueurCourant] = 0

        if self.jeuAvecBrelan(self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur()): #>= 4:
            print("brelan")
            choix = random.randint(0, 100)
            print(choix)
            if (choix >0 and choix <75):
                self.renseignerMiseJoueurTour(self.plusGrosseMise)
            if (choix > 75 and choix <95):
                miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                self.renseignerMiseJoueurTour(miseSaisie)
                self.plusGrosseMise = miseSaisie
            else:
                self.listeIndicesJoueursManche.remove(self.indiceJoueurCourant)
                mise = self.listeMisesJoueursManche[self.indiceJoueurCourant]
                # Si jamais misé et le joueur se couche
                if (self.tour == 1 and self.listeMisesJoueursManche[self.indiceJoueurCourant] == 0):
                    # Le premier joueur perdra 50 de ses gains
                    if (self.indiceJoueurCourant == 0):
                        mise = 50      
                    # Le deuxième joueur perdra 25 de ses gains
                    elif (self.indiceJoueurCourant == 1):
                        mise = 25               
                self.appliquerMiseGainJoueur(mise)
                self.listeJoueursCouchesTour.append(self.getJoueurCourant())               
                self.listeMisesJoueursTour[self.indiceJoueurCourant] = 0
                self.listeMisesJoueursManche[self.indiceJoueurCourant] = 0
        else:
            choix = random.randint(0, 100)
            print(choix)
            if (choix >0 and choix <75):
                self.renseignerMiseJoueurTour(self.plusGrosseMise)
            else:
                self.listeIndicesJoueursManche.remove(self.indiceJoueurCourant)
                mise = self.listeMisesJoueursManche[self.indiceJoueurCourant]
                # Si jamais misé et le joueur se couche
                if (self.tour == 1 and self.listeMisesJoueursManche[self.indiceJoueurCourant] == 0):
                    # Le premier joueur perdra 50 de ses gains
                    if (self.indiceJoueurCourant == 0):
                        mise = 50      
                    # Le deuxième joueur perdra 25 de ses gains
                    elif (self.indiceJoueurCourant == 1):
                        mise = 25               
                self.appliquerMiseGainJoueur(mise)
                self.listeJoueursCouchesTour.append(self.getJoueurCourant())               
                self.listeMisesJoueursTour[self.indiceJoueurCourant] = 0
                self.listeMisesJoueursManche[self.indiceJoueurCourant] = 0

    def TourBotDifficile(self):
        
        print("main du robot",self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur())
        if (self.tour == 1):

            if (self.listeJoueurs[self.indiceJoueurCourant].mainJoueur[1].getValeur() >=7 and self.listeJoueurs[self.indiceJoueurCourant].mainJoueur[0].getValeur() == self.listeJoueurs[self.indiceJoueurCourant].mainJoueur[1].getValeur()):
                print("pair des le départ")
                choix = random.randint(0, 100)
                print("le choix est ",choix)
                if (choix >0 and choix <70):
                    self.renseignerMiseJoueurTour(self.plusGrosseMise)
                if (choix > 70 and choix <85):
                    miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                    self.renseignerMiseJoueurTour(miseSaisie)
                    self.plusGrosseMise = miseSaisie
                else:
                    self.listeIndicesJoueursManche.remove(self.indiceJoueurCourant)
                    mise = self.listeMisesJoueursManche[self.indiceJoueurCourant]
                    # Si jamais misé et le joueur se couche
                    if (self.tour == 1 and self.listeMisesJoueursManche[self.indiceJoueurCourant] == 0):
                        # Le premier joueur perdra 50 de ses gains
                        if (self.indiceJoueurCourant == 0):
                            mise = 50      
                        # Le deuxième joueur perdra 25 de ses gains
                        elif (self.indiceJoueurCourant == 1):
                            mise = 25               
                    self.appliquerMiseGainJoueur(mise)
                    self.listeJoueursCouchesTour.append(self.getJoueurCourant())               
                    self.listeMisesJoueursTour[self.indiceJoueurCourant] = 0
                    self.listeMisesJoueursManche[self.indiceJoueurCourant] = 0
           

            if self.listeJoueurs[self.indiceJoueurCourant].mainJoueur[0].getValeur() >= 7 or self.listeJoueurs[self.indiceJoueurCourant].mainJoueur[1].getValeur() >= 7:
                print("la main du robot a> 7 ")
                print("la valeur de la carte est ",self.listeJoueurs[self.indiceJoueurCourant].mainJoueur[0].getValeur())
                choix = random.randint(0, 100)
                print("le choix est ",choix)

                if (choix >0 and choix <=70):
                        print("robot mise")
                        self.renseignerMiseJoueurTour(self.plusGrosseMise)
                else:
                    print("abandonne")
                    self.listeIndicesJoueursManche.remove(self.indiceJoueurCourant)
                    mise = self.listeMisesJoueursManche[self.indiceJoueurCourant]
                    # Si jamais misé et le joueur se couche
                    if (self.tour == 1 and self.listeMisesJoueursManche[self.indiceJoueurCourant] == 0):
                        # Le premier joueur perdra 50 de ses gains
                        if (self.indiceJoueurCourant == 0):
                            mise = 50      
                        # Le deuxième joueur perdra 25 de ses gains
                        elif (self.indiceJoueurCourant == 1):
                            mise = 25               
                    self.appliquerMiseGainJoueur(mise)
                    self.listeJoueursCouchesTour.append(self.getJoueurCourant())               
                    self.listeMisesJoueursTour[self.indiceJoueurCourant] = 0
                    self.listeMisesJoueursManche[self.indiceJoueurCourant] = 0

            else:
                choix = random.randint(0, 100)
                print("le choix est ",choix)
                if (choix >0 and choix <30):
                        self.renseignerMiseJoueurTour(self.plusGrosseMise)
                else:
                    self.listeIndicesJoueursManche.remove(self.indiceJoueurCourant)
                    mise = self.listeMisesJoueursManche[self.indiceJoueurCourant]
                    # Si jamais misé et le joueur se couche
                    if (self.tour == 1 and self.listeMisesJoueursManche[self.indiceJoueurCourant] == 0):
                        # Le premier joueur perdra 50 de ses gains
                        if (self.indiceJoueurCourant == 0):
                            mise = 50      
                        # Le deuxième joueur perdra 25 de ses gains
                        elif (self.indiceJoueurCourant == 1):
                            mise = 25               
                    self.appliquerMiseGainJoueur(mise)
                    self.listeJoueursCouchesTour.append(self.getJoueurCourant())               
                    self.listeMisesJoueursTour[self.indiceJoueurCourant] = 0
                    self.listeMisesJoueursManche[self.indiceJoueurCourant] = 0

         

        if (self.tour == 2 ):
            print("main du robot",self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur())
            self.conditionverificationtour2()

        if (self.tour == 3):
            self.conditionverificationtour2()
            if self.jeuAvecCarre(self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur()):
                choix = random.randint(0, 100)
                if (choix >0 and choix <70):
                    self.renseignerMiseJoueurTour(self.plusGrosseMise)
                if (choix > 70 and choix <=100):
                    miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                    self.renseignerMiseJoueurTour(miseSaisie)
                    self.plusGrosseMise = miseSaisie
                
            if self.jeuAvecSuite(self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur()):
                choix = random.randint(0, 100)
                if (choix >0 and choix <70):
                    self.renseignerMiseJoueurTour(self.plusGrosseMise)
                if (choix > 70 and choix <=100):
                    miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                    self.renseignerMiseJoueurTour(miseSaisie)
                    self.plusGrosseMise = miseSaisie
            if self.jeuAvecFull(self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur()):
                choix = random.randint(0, 100)
                if (choix >0 and choix <70):
                    self.renseignerMiseJoueurTour(self.plusGrosseMise)
                if (choix > 70 and choix <=100):
                    miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                    self.renseignerMiseJoueurTour(miseSaisie)
                    self.plusGrosseMise = miseSaisie
            if self.jeuAvecQuinteFlush(self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur()):
                choix = random.randint(0, 100)
                if (choix >0 and choix <70):
                    self.renseignerMiseJoueurTour(self.plusGrosseMise)
                if (choix > 70 and choix <=100):
                    miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                    self.renseignerMiseJoueurTour(miseSaisie)
                    self.plusGrosseMise = miseSaisie
            if self.jeuAvecQuinteFlushRoyale(self.listeJoueurs[self.indiceJoueurCourant].getMainJoueur()):
                choix = random.randint(0, 100)
                if (choix >0 and choix <70):
                    self.renseignerMiseJoueurTour(self.plusGrosseMise)
                if (choix > 70 and choix <=100):
                    miseSaisie = random.randint(self.plusGrosseMise,self.listeJoueurs[self.indiceJoueurCourant].getGains())
                    self.renseignerMiseJoueurTour(miseSaisie)
                    self.plusGrosseMise = miseSaisie
            
            


            

    # On affiche le plateau pour le joueur et on gére la partie
    def afficherJeuJoueur(self, background_image = None)->str:
        pygame.init()

        # Cas ou on revient sur la partie
        if (background_image != None):
            self.background_image = background_image
            self.background = pygame.image.load(self.background_image).convert()

        # Affichage du background
        self.fenetre.blit(self.background,(0, 0))

        # # bouton retour
        cheminImageretour = "./images/Outils/retour.png"
        imageRetour = pygame.image.load(cheminImageretour)
        self.boxRetour = imageRetour.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(imageRetour, self.boxRetour)        
        
        # afficher cartes du joueur courrant
        jcourant = self.listeJoueurs[self.indiceJoueurCourant]
        mainJoueurCourant = jcourant.getMainJoueur()
        
        #afficher les cartes du Joueur courant
        i = 0
        for carte in mainJoueurCourant:
            cheminCarte = "./Images/Cartes/{0}{1}.png".format(carte.getValeur(), carte.getFamille())
            carteImage = pygame.image.load(cheminCarte)
            self.fenetre.blit(carteImage,(340 + i * 120, 500))
            i = i + 1
            
        #Boutons
        if (jcourant.getGains() >= self.plusGrosseMise):
            nombresBoutons = 3
        else:
            nombresBoutons = 2
         
        self.boutonSuivre = Bouton(150,500,140,40,(243,223,36),"Suivre",self.fenetre,20,False)

        # On doit pas faire apparaître le bouton miser si le joueur n'a pas assez de gains
        positionY = 550
        self.boutonMiser = None
        if (nombresBoutons == 3):
            self.boutonMiser = Bouton(150, positionY,140,40,(243,223,36),"Miser",self.fenetre,20,False)
            positionY = positionY + 50
        self.boutonCoucher = Bouton(150,positionY,140,40,(243,223,36),"Se coucher",self.fenetre,20,False)
        nb = 0
        for i in range (0, nombresBoutons):
            boutonContoure = pygame.draw.rect(self.fenetre, (0,0,0), (150,500+nb,140,40), 3, 5)
            nb = nb + 50

        #afficher paquet de carte
        self.fenetre.blit(self.dosDeCartes,(750, 250))

        self.afficherJoueurs()              # on affiche les autres joueur
        self.afficherCarteMillieuPlateau()  # on affiche les cartes qui peuvent être au milieu
     
        # afficher carte plateau
        pygame.display.update()

        # on gère le tour (choix du joueur, changement de joueur, résultat, changement de manche...)
        retour = self.gererTourJoueur()

        # Si on revient sur l'accueil, on continue pas
        if retour != None:
            return retour
        else:
            # on réaffiche le jeu du joueur courant (sera le joueur suivant)
            return self.afficherJeuJoueur()

    # on gère le tour du joueur        
    def gererTourJoueur(self)->str:
        self.afficherMiseDemandee()             # affichage de la mise demandée au joueur
            
        retour = self.attendreChoixJoueur()     # on attend le choix du joueur

        # Cas où on a cliqué sur le retour, il faudra alors sortir du jeu pour revenir sur l'accueil
        if retour != None:
            return retour
        
        # On vérifie si la manche est terminée si il reste plus qu'un joueur qui peut jouer, par exemple plus d'argent pour les autres joueurs mais qui se sont pas couchés
        # la manche sera terminée, on affichera le gagnant
        nombreJoueursRestantManche = len(self.listeIndicesJoueursManche)
        if (nombreJoueursRestantManche > 1 and (nombreJoueursRestantManche - len(self.listeIndicesJoueursSansGains) == 1)):
            # on affiche le résultat de la manche
            retour = self.afficherResulatFinManche()
            if retour != None:
                return retour
        # Il reste plus qu'un joueur sur la manche il a gagné, tout le monde s'est couché, on affiche directement le gagnant
        elif (nombreJoueursRestantManche == 1):
            # le joueur restant a gagné
            joueurGagnant = self.listeJoueurs[self.listeIndicesJoueursManche[0]]
            self.afficherGagnant(joueurGagnant)
            # Si tout le monde a perdu n'a plus d'argent la partie sera terminée, on vérifie le nombre de joueur qui peuvent encore jouer
            nombreJoueurNonPerdu = 0
            for joueur in self.listeJoueurs:
                if (joueur.getAPerdu() == False):
                    nombreJoueurNonPerdu = nombreJoueurNonPerdu + 1

            # Si tout le monde a perdu, on peut pas faire une nouvelle manche
            if (nombreJoueurNonPerdu == 1):
                self.afficherFinPartie(joueurGagnant)
                # on arrête la partie, on retourne la fin de partie pour pouvoir retourner sur MainGraphique
                return 'finPartie'
            else:
                # On démarre une nouvelle manche
                return self.demarrerNouvelleManche()
        
        # On passe au joueur suivant
        self.passerJoueurSuivant()

        # On va vérifier si on doit changer de tour ou non
        self.gererChangementTour()

        # Les 4 tours sont terminés, à voir qui a gagné, on affiche le résultat de la manche
        if (self.tour == 5):
            retour = self.afficherResulatFinManche()
            if retour != None:
                return retour            

        # affichage d'un message pour savoir qui doit jouer
        self.popUpJoueurSuivant.afficherPopUp(self.tour, self.getJoueurCourant(), self.indiceJoueurCourant, self.plusGrosseMise)
        return None

    # Passage au joueur suivant
    def passerJoueurSuivant(self):
        # On vérifie si le joueur courant est encore dans la manche et a encore de l'argent
        listeJoueursPouvantEncoreJouer = []
        for indiceJoueur in self.listeIndicesJoueursManche:
            # le joueur a encoire de l'argent il peut encore jouer
            if indiceJoueur not in self.listeIndicesJoueursSansGains:
                listeJoueursPouvantEncoreJouer.append(indiceJoueur)
        
        indiceJoueurSuivant = None
        if self.indiceJoueurCourant in listeJoueursPouvantEncoreJouer:
            indiceListe = listeJoueursPouvantEncoreJouer.index(self.indiceJoueurCourant)
            if indiceListe + 1 > len(listeJoueursPouvantEncoreJouer) - 1:
                indiceJoueurSuivant = listeJoueursPouvantEncoreJouer[0]
            else:
                indiceJoueurSuivant = listeJoueursPouvantEncoreJouer[indiceListe + 1]
        else:
            # Le joueur avait été supprimé
            indiceJoueurSuivanteTrouve = False
            indice = 0
            while (indiceJoueurSuivanteTrouve == False and indice < len(listeJoueursPouvantEncoreJouer)):
                if listeJoueursPouvantEncoreJouer[indice] > self.indiceJoueurCourant:
                    indiceJoueurSuivant = listeJoueursPouvantEncoreJouer[indice]
                    indiceJoueurSuivanteTrouve = True
                else:
                    indice = indice + 1
                    
            if (indiceJoueurSuivant == None):
                indiceJoueurSuivant = listeJoueursPouvantEncoreJouer[0]
      
        self.indiceJoueurCourant = indiceJoueurSuivant

    # affichage de la mise demandée
    def afficherMiseDemandee(self):
        miseJoueur = self.listeMisesJoueursManche[self.indiceJoueurCourant]
        Texte(self.fenetre, "Votre mise : {0} - Mise demandée : {1}".format(miseJoueur, self.plusGrosseMise), 15, (255,255,255), 310, 450)
        pygame.display.update()
        
    # on attend le choix du joueur
    def attendreChoixJoueur(self)->str:
        choixEffectue = False      # sert à savoir que le joueur a fait son choix
        retour = None              # sert pour savoir que le joueur a cliqué sur le bouton retour
        champsMise = None


        while choixEffectue == False:
            # print(self.getJoueurCourant())
            # print("Liste Joueur : " + List[Joueur])
            # print('valeur',self.getJoueurCourant().getBot())
            if (self.getJoueurCourant().getBot() == "Humain"): 
                for event in pygame.event.get():
                
                    # On change le pointer de la souris au survol sur un bouton
                    if (event.type == pygame.MOUSEMOTION):
                        positionCurseur = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                        if self.boxRetour.colliderect(positionCurseur) or self.boutonSuivre.verifier_click_bouton(positionCurseur) or (self.boutonMiser and self.boutonMiser.verifier_click_bouton(positionCurseur)) or self.boutonCoucher.verifier_click_bouton(positionCurseur):
                            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                        else:
                            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

                    # Si clique sur un des boutons
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                        
                        # Si on revient sur l'accueil
                        if self.boxRetour.colliderect(positionClick):
                            choixEffectue = True
                            retour = 'accueil'

                        # Si on suit
                        if self.boutonSuivre.verifier_click_bouton(positionClick):
                            self.renseignerMiseJoueurTour(self.plusGrosseMise)
                            choixEffectue = True
                            
                        # Si on mise    
                        elif self.boutonMiser and self.boutonMiser.verifier_click_bouton(positionClick): 
                            champsMise = ChampSaisieMise(self.getJoueurCourant().getGains(), self.plusGrosseMise, self.fenetre)
                            miseSaisie = champsMise.attendreSaisieMise()
                            self.renseignerMiseJoueurTour(miseSaisie)
                            self.plusGrosseMise = miseSaisie
                            choixEffectue = True
                            
                        # Si on se couche
                        elif self.boutonCoucher.verifier_click_bouton(positionClick):
                            self.listeIndicesJoueursManche.remove(self.indiceJoueurCourant)
                            mise = self.listeMisesJoueursManche[self.indiceJoueurCourant]
                            # Si jamais misé et le joueur se couche
                            if (self.tour == 1 and self.listeMisesJoueursManche[self.indiceJoueurCourant] == 0):
                                # Le premier joueur perdra 50 de ses gains
                                if (self.indiceJoueurCourant == 0):
                                    mise = 50      
                                # Le deuxième joueur perdra 25 de ses gains
                                elif (self.indiceJoueurCourant == 1):
                                    mise = 25
                                                
                            self.appliquerMiseGainJoueur(mise)
                            self.listeJoueursCouchesTour.append(self.getJoueurCourant())               
                            self.listeMisesJoueursTour[self.indiceJoueurCourant] = 0
                            self.listeMisesJoueursManche[self.indiceJoueurCourant] = 0
                            choixEffectue = True
                    elif event.type == pygame.QUIT:
                        pygame.quit()    
                   
            if (self.getJoueurCourant().getBot() == "Robot"):
                if (self.getJoueurCourant().getNiveau() == "facile"):
                    self.TourBotDifficile()
                    choixEffectue = True
                else:
                    self.TourBotDifficile()
                    choixEffectue = True

                                    
                        
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
        return retour

    # Afficher le gagnant, cas ou il restait plus qu'un joueur (tout le monde couché)
    def afficherGagnant(self, joueur: Joueur):
        # Affichage du background
        self.fenetre.blit(self.background,(0, 0))
        TexteCenter(self.fenetre, "Bravo le joueur {0} a gagné !!".format(joueur.getNom()), 25, 15, 900, 0, 200, (255,255,255))

        # On affiche la main du joueur gagnant
        positionX = 300
        for carte in joueur.getMainJoueur():
            cheminCarte = "./Images/Cartes/{0}{1}.png".format(carte.getValeur(), carte.getFamille())
            imageCarte = pygame.image.load(cheminCarte)
            self.fenetre.blit(imageCarte,(positionX, 300))
            positionX = positionX + 200

        # On récupère la mise de ceux qui se sont couchés
        gainTotalJoueurAvecMise = joueur.getGains() + self.misesJoueursCouches
        joueur.setGains(gainTotalJoueurAvecMise)

        pygame.display.update()  
        
        TexteCenter(self.fenetre, "Appuyer sur une touche pour continuer", 25, 15, 900, 0, 600, (4,32,106))

        pygame.display.update()    
        self.attendreAppuiTouche()

    # on va vérifier si on peut changer de tour
    def gererChangementTour(self):
        # Pour le changement de tour, on change de tour si tous les joueurs non couchés ont la même mise
        listeMise = []
        for indiceJoueur in self.listeIndicesJoueursManche:
            # On doit exclure les joueurs qui sont encore dans la manche mais qui n'ont pas pu miser la mise max
            if (indiceJoueur not in self.listeIndicesJoueursSansGains):
                listeMise.append(self.listeMisesJoueursTour[indiceJoueur])
            
        if listeMise.count(self.plusGrosseMise) == len(self.listeIndicesJoueursManche) - len(self.listeIndicesJoueursSansGains):
            self.tour = self.tour + 1
            print("tour :", self.tour)
            for indiceJoueur in range (0, len(self.listeMisesJoueursTour)):
                self.listeMisesJoueursTour[indiceJoueur] = 0

    # permet de récupérer une liste de dictionnaire contenant le résultat de chaque joueurs de la manche
    # dict du résultat d'un joueur : {"jeuTrouve": regle, "texte": texte, "valeurJeu": valeurJeu, "valeurCarte": valeurCarte}
    def recupererResultatJoueurs(self)->List[dict]:
       # Cette liste contiendra le résultat des jeux des joueurs
        listeResultatJeuxJoueurs: List[dict] = []

        for indiceJoueurManche in self.listeIndicesJoueursManche:
            joueur = self.listeJoueurs[indiceJoueurManche]
            # On récupère le résultat du jeu joueur
            listCartes = joueur.getMainJoueur().copy()
            listCartes.extend(self.listeTabCartesMilieu) 
            # On prend les cartes du joueur pour les rajouter aux cartes du milieu
            resultatJeuJoueur = self.determinerJeuJoueur(listCartes, indiceJoueurManche)
            listeResultatJeuxJoueurs.append(resultatJeuJoueur)

        return listeResultatJeuxJoueurs

    # Permet de trouver le ou les joueurs gaganants à partir de la liste de résultat
    # Retourne une liste du ou des indices des joueurs gagnantss
    def trouverGagnantsEAffichageGagants(self, listeResultatJeuxJoueurs: List[dict])->List[int]:
        # On va déterminer le gagnant en regardant qui a le jeu le plus fort
        plusGrosJeu: int = 0
        nomCombinaisonJeuGagnant:str = ""       # Nom de la combinaison qui a gagné (flush ou carré ou couleur ou suite...)
        # Liste des indices des joueurs qui ont gagné, c'est une liste car il peut y avoir plusieurs gagnants (par exemple deux paires, avec la même paire la plus grosse)
        listeindicesJoueursGagnants: list[int] = []
        valeurCarteMax = 0
        print("On boucle sur la liste de dictionnaire des résultats des joueurs")
        # On boucle sur la liste de dictionnaire des résultats des joueurs
        for resultatJeuJoueur in listeResultatJeuxJoueurs:
            indiceJoueur = resultatJeuJoueur["indiceJoueur"]
            print ("boucle : {0}".format(indiceJoueur))
            # Un joueur a le plus grosse valeur de jeu, on considère pour l'instant que ça sera lui le gaganant
            if (resultatJeuJoueur["valeurJeu"] > plusGrosJeu):
                listeindicesJoueursGagnants
                plusGrosJeu = resultatJeuJoueur["valeurJeu"]
                nomCombinaisonJeuGagnant = resultatJeuJoueur["texte"]
                listeindicesJoueursGagnants = [indiceJoueur]
                valeurCarteMax = resultatJeuJoueur["valeurCarte"]
            # Un autre joueur a le même, on va le départager avec sa plus grosse carte avec la carte des joueurs
            elif (resultatJeuJoueur["valeurJeu"] == plusGrosJeu):
                joueurARajouter: bool = False
                nouveauJoueurGagnant = bool = False
                # On boucle sur tous les joueurs qui ont le même jeu pour les départager
                for indiceTableau in range(0, len(listeindicesJoueursGagnants)):
                    # Le joueur a une carte plus importante que les autres
                    if (resultatJeuJoueur["valeurCarte"] > listeResultatJeuxJoueurs[indiceTableau]["valeurCarte"]):
                        # Le joueur a la plus grosse carte, ça sera lui le gagnant
                        nouveauJoueurGagnant = True
                        valeurCarteMax = resultatJeuJoueur["valeurCarte"]
                        print ("boucle : break")
                        break
                    # Le joueur a la même carte, il sera gagnant aussi, il y aura plusieurs gagnants
                    elif (resultatJeuJoueur["valeurCarte"] == listeResultatJeuxJoueurs[indiceTableau]["valeurCarte"]):
                        # On le rajoute dans la liste des joueurs gagnants
                        joueurARajouter = True

                if (joueurARajouter):
                    listeindicesJoueursGagnants.append(indiceJoueur)
                elif (nouveauJoueurGagnant):
                    listeindicesJoueursGagnants = [indiceJoueur]

        # Après avoir trouvé le ou les gagants on affiche le ou les joueurs qui on gagné
        if (len(listeindicesJoueursGagnants) > 0):
            self.afficherJoueursGagnants(listeindicesJoueursGagnants, valeurCarteMax, nomCombinaisonJeuGagnant)
        else:
            TexteCenter(self.fenetre,  "Pas de gagnant !", 20, 15, 900, 0, 490, (4,32,106))

        return listeindicesJoueursGagnants

    # Sert à afficher les joueurs gagnants sur la fin de la manche
    def afficherJoueursGagnants(self, listeindicesJoueursGagnants: List[dict], valeurCarteMax: int, nomCombinaisonJeuGagnant: str):
        print("On affiche le ou les joueurs qui on gagné")        
        # On affiche le ou les joueurs qui on gagné
        listeNomsJoueursGagants: List[str] = []
        # On va récupérer dans une liste le ou les noms des joueurs gagnants
        for indiceJoueurGagant in listeindicesJoueursGagnants:
            joueur = self.listeJoueurs[indiceJoueurGagant]
            listeNomsJoueursGagants.append(joueur.getNom())

        # On séparera si plusieurs gagnants avec une ","
        nomsJoueursGagant = ", ".join(listeNomsJoueursGagants)
        if valeurCarteMax != None:
            # On détermine le nom de la carte max
            nomCarte = "de {0}".format(str(valeurCarteMax))
            if (valeurCarteMax == 11):
                nomCarte = "de valet"
            elif (valeurCarteMax == 12):
                nomCarte = "de dame"
            elif (valeurCarteMax == 13):
                nomCarte = "de roi"
            elif (valeurCarteMax == 14):
                nomCarte = "d'as"         
  
            TexteCenter(self.fenetre,  "Gagnant(s): {0} avec {1} {2}".format(nomsJoueursGagant, nomCombinaisonJeuGagnant.lower(), nomCarte), 20, 15, 900, 0, 490, (4,32,106))
        else:
            # Sera le cas pour la Quinte flush royal, il n'y a pas de valeurCarteMax 
            TexteCenter(self.fenetre,  "Gagnant(s): {0} avec {1}".format(nomsJoueursGagant, nomCombinaisonJeuGagnant), 20, 15, 900, 0, 490, (4,32,106))

    # Permet de modifier les gains des joueurs de la manche si gagné ou perdu
    def ajouterEtRetirerGainsJoueursFinManche(self, listeindicesJoueursGagnants: List[int]):
        print("On retire les gains ou on rajoute")    
        # Le ou les joueurs qui ont gagné vont récupérer les gains, ceux qui ont perdu et n'ont plus de gains auront perdus (aPerdu = True)
        indiceJoueur = 0
        # On boucle sur tous les joueurs de la manche, on aura pas les joueurs couchés car ils sont sortis de la manche et leurs gains ont déjà été retiré
        for indiceJoueurManche in self.listeIndicesJoueursManche:
            joueur: Joueur = self.listeJoueurs[indiceJoueurManche]
            gainsJoueur = joueur.getGains()
            # Si le joueur a encore de l'argent, on retire sa mise joué
            miseJoue = self.listeMisesJoueursManche[indiceJoueurManche]
            gainsJoueur = gainsJoueur - miseJoue
            joueur.setGains(gainsJoueur)
            # Si plus d'argent pour le joueur qui a  perdu, on indique qu'il a perdu
            if (gainsJoueur == 0 and indiceJoueur not in listeindicesJoueursGagnants):
                    joueur.setAPerdu(True)

            indiceJoueur = indiceJoueur + 1
 
        # Total des mises, on divise la mise total entre le ou les joueurs qui ont gagné pour se partager les gains
        print("Joueurs qui ont gagné")
        print("sum() : {0}".format(sum(self.listeMisesJoueursManche) + self.misesJoueursCouches))
        print("listeindicesJoueursGagnants", listeindicesJoueursGagnants)

        nombreJoueursGagnants = len(listeindicesJoueursGagnants)
        # Si pas de gagnants les mises sont redistribuées
        if nombreJoueursGagnants == 0:
            nombreJoueursGagnants = len(self.listeMisesJoueursManche)
        totalMisesJoueur = int(sum(self.listeMisesJoueursManche) + self.misesJoueursCouches) // nombreJoueursGagnants
        
        for indiceJoueurGagnant in listeindicesJoueursGagnants:
            joueur = self.listeJoueurs[indiceJoueurGagnant]
            gainsJoueur = joueur.getGains() + totalMisesJoueur
            joueur.setGains(gainsJoueur)
        
    # Affichage du résultat de fin de la manche
    def afficherResulatFinManche(self):
        self.fenetre.fill(0)
        # Affichage du background
        self.fenetre.blit(self.background,(0, 0))
        
        # On va afficher tous les joueurs avec leurs cartes retournées
        positionX = 100        

        # Cette liste va chercher et contiendra le résultat des jeux des joueurs de la manche
        listeResultatJeuxJoueurs: List[dict] = self.recupererResultatJoueurs()

        # On va déterminer le gagnant en regardant qui a le jeu le plus fort
        # Liste des indices des joueurs qui ont gagné, c'est une liste car il peut y avoir plusieurs gagnants (par exemple deux paires, avec la même paire la plus grosse)
        listeindicesJoueursGagnants: list[int] = self.trouverGagnantsEAffichageGagants(listeResultatJeuxJoueurs)
        
        print("On retire les gains ou on rajoute")    
        # Le ou les joueurs qui ont gagané vont récupérer les gains, ceux qui ont perdu et n'ont plus de gains auront perdus (aPerdu = True)
        self.ajouterEtRetirerGainsJoueursFinManche(listeindicesJoueursGagnants)
    
        # on affiche chaque joueur de la manche avec le résultat de sa main
        print("on affiche chaque joueur de la manche avec le résultat de sa main")
        indiceTab = 0
        for indiceJoueur in self.listeIndicesJoueursManche:
            # afficher cartes du joueur
            joueur = self.listeJoueurs[indiceJoueur]
            resultatJeuJoueur = listeResultatJeuxJoueurs[indiceTab]  # Résultat du joueur
            
            # On affiche l'avatar du joueur
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)  

            pygame.draw.circle(self.fenetre, (r,g,b), (positionX+36, 80), 50)
            pygame.draw.circle(self.fenetre, (0,0,0), (positionX+36, 80), 50,3)
                
            TexteCenter(self.fenetre, joueur.getNom(), 15, 15, 75, positionX, 140, (255,255,255))
            TexteCenter(self.fenetre, str(joueur.getGains()), 15, 15, 75, positionX, 10, (255,255,255))
            pygame.draw.circle(self.fenetre, (0, 0, 0), (positionX+36, 80), 50,3)
            
            imageAvatar = pygame.image.load(joueur.getCheminImageAvatar())

            # Si le joueur a perdu on l'affiche sur un ton sombre
            if (joueur.getAPerdu()):
                imageAvatar.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)

            self.fenetre.blit(imageAvatar, (positionX-1, 40)) 
            # Si le joueur a perdu on l'affiche sur un ton sombre
            if (joueur.getAPerdu()):
                Texte(self.fenetre, "PERDU", 35, (255,255,255), positionX - 15, 65)   

            # Affichage des cartes du joueur
            mainJoueur = joueur.getMainJoueur()
       
            positionY = 165
            # on affiche les cartes du joueur
            for carte in mainJoueur:
                carte = "./Images/Cartes/{0}{1}.png".format(carte.getValeur(), carte.getFamille())
                carteJoueur = pygame.image.load(carte)
                self.fenetre.blit(carteJoueur,(positionX, positionY))
                positionY = positionY + 150
            
            # On affiche le résultat du jeu du joueur
            Texte(self.fenetre, resultatJeuJoueur["texte"], 15, (255,255,255), positionX, positionY + 2)     

            positionX = positionX + 200
            indiceTab = indiceTab + 1

        print("Affichage les 5 cartes du mileu")    
        # Affichage les 5 cartes du mileu
        positionX = 100
        for carte in self.listeTabCartesMilieu:
            cheminCarte = "./Images/Cartes/{0}{1}.png".format(carte.getValeur(), carte.getFamille())
            carteImage = pygame.image.load(cheminCarte)
            self.fenetre.blit(carteImage, (positionX, 520))
            positionX = positionX + 150
                        
        TexteCenter(self.fenetre, "Appuyer sur une touche pour continuer", 20, 15, 900, 0, 680, (4,32,106))

        pygame.display.update()    
        self.attendreAppuiTouche()
        
        print("On va regarder si y a encore des joueurs")        
        # On va regarder si y a encore des joueurs
        nombreJoueurJeu = 0
        joueurGagnant = None
        for joueur in self.listeJoueurs:
            if (joueur.getAPerdu() == False):
                joueurGagnant = joueur
                nombreJoueurJeu = nombreJoueurJeu + 1
         
        if (nombreJoueurJeu == 1):
            # La partie est terminée, on affiche la fin de la partie avec le gagnant
            self.afficherFinPartie(joueurGagnant)
            return 'finPartie'   
        else:
            return self.demarrerNouvelleManche()   # On démarre une nouvelle manche
    
    # Affiche de la fin de partie et du joueur gagnant
    def afficherFinPartie(self, joueurGagnant: Joueur):
        # Affichage du background
        self.fenetre.blit(self.background,(0, 0)) 
        TexteCenter(self.fenetre, "Le joueur {0} a gagné la partie !".format(joueurGagnant.getNom()), 30, 15, 900, 0, 300, (4,32,106))       
        TexteCenter(self.fenetre, "Appuyer sur une touche pour continuer", 25, 15, 900, 0, 600, (4,32,106))                             
        pygame.display.update()
        self.attendreAppuiTouche()
        self.listeJoueursPerdus = []

    # retourne le joueur courant
    def getJoueurCourant(self) -> Joueur:
        return self.listeJoueurs[self.indiceJoueurCourant]
    
    # on conserve la mise du joueur qui a misé sur le tour
    def renseignerMiseJoueurTour(self, mise):
        miseJoueur = mise
        
        # On vérifie si le joueur peut miser
        gains = self.getJoueurCourant().getGains()
        gainsRestantJoueur = gains - mise

        if gainsRestantJoueur < 0:
           miseJoueur = gains
           self.listeIndicesJoueursSansGains.append(self.indiceJoueurCourant)
        
        self.listeMisesJoueursTour[self.indiceJoueurCourant] = miseJoueur
        self.listeMisesJoueursManche[self.indiceJoueurCourant] = miseJoueur

    # on applique la mise sur les gains du joueurs, cas du joueur qui s'est couché
    def appliquerMiseGainJoueur(self, mise: int):
        # On va retirer direct la mise de ses gains, on vérifie avant si le joueur a assez d'argent
        joueurCourant = self.getJoueurCourant()
        gains = joueurCourant.getGains()
        gainsRestantJoueur = gains - mise

        if gainsRestantJoueur <= 0:
           gainsRestantJoueur = gains
           self.misesJoueursCouches = self.misesJoueursCouches + gains
           # Le joueur a plus d'argent, la partie est finie pour lui
           joueurCourant.setAPerdu(True)
           self.listeJoueursPerdus.append(joueurCourant)
        else:
           self.misesJoueursCouches = self.misesJoueursCouches + mise 
                   
        joueurCourant.setGains(gainsRestantJoueur)
        
    # affichage des cartes au mileu en fonction du tour joué
    # à partir du tour 2 : 3 cates retournés
    # à partir du tour 3 : 4 cartes retournés
    # à partir du tour 4 : 5 cartes retournés
    def afficherCarteMillieuPlateau(self):
        if self.tour != 1 :
            for i in range(0, self.tour + 1):
                carte = self.listeTabCartesMilieu[i]
                cheminImageCarte = "./Images/Cartes/{0}{1}.png".format(carte.getValeur(), carte.getFamille())
                carteImage = pygame.image.load(cheminImageCarte)
                self.fenetre.blit(carteImage, (600-i*110, 250))

    # attente de l'appui sur une touche
    def attendreAppuiTouche(self): 
        sortir = False
        while sortir == False:
            for event in pygame.event.get():
                if  (event.type == pygame.KEYDOWN):
                    sortir = True
                elif (event.type == pygame.QUIT):
                    pygame.quit() 

    # détermine la plus grosse combinaison pour le jeu du joueur : "quinte-flush-royal", "quinte-royal", "carre", "full", "couleur", "suite", "brelan", "double-paire", "paire", "hauteur"
    def determinerJeuJoueur(self, listeCartes: List[Carte], indiceJoueurManche: int):
        # Liste des combinaisaons par ordre à vérifier
        listeOrdresRegles = ["quinte-flush-royal", "quinte-royal", "carre", "full", "couleur", "suite",
            "brelan", "double-paire", "paire", "hauteur"]

        # ça sera pour déterminer un nombre de point par règle la plus important
        # ça servira pour trouver le gagnant en cherchant celui qui a les points les plus important
        valeurCarte: int = None
        regleTrouve = False
        valeurJeu: int = 0    # Servira à déterminer qui a gagné en fonction de celui qui a cette valeur maximum

        # on boucle sur toutes les règles jusqu'à trouver la règle qui correspond au jeu du joueur :
        # 1 : Quinte Flush Royale (toutes les cartes de la même couleur, séquence as - roi - renne - valet - 10)
        # 2 : Quinte Flush (toute séquence de cartes de même couleur, par exemple 9-8-7-6-5)
        # 3 : Carré (quatre cartes de même valeur, par exemple A-A-A-A)
        # 4 : Full House (trois cartes du même type et une paire)
        # 5 : Couleur (toutes les cartes de la même couleur)
        # 6 : Quinte (ou Suite) (une séquence de base comme 6-5-4-3-2)
        # 7 : Brelan (trois cartes de même valeur, par exemple 5-5-5)
        # 8 : Double Paire (Deux paires, comme 9-9 ET 5-5)
        # 9 : Paire (toute paire, qu'il s'agisse de A-A ou de 2-2). La paire d’As étant la plus forte et gagne contre une autre paire.
        # 10 : Hauteur (quelle que soit votre plus haute carte)
        indiceRegle = 0
        while (regleTrouve == False and indiceRegle < len(listeOrdresRegles)):
            regle = listeOrdresRegles[indiceRegle]

            texte: str = ""
            if regle == "quinte-flush-royal":
                regleTrouve = self.jeuAvecQuinteFlushRoyale(listeCartes)
                valeurJeu = 100
                valeurCarte = None
                texte = "Quinte flush royal"                
              
            elif regle == "quinte-royal":
                valeurCarte = self.jeuAvecQuinteFlush(listeCartes)
                regleTrouve = valeurCarte != None
                valeurJeu = 90
                texte = "Quinte royal"

            elif regle == "carre":
                valeurCarte = self.jeuAvecCarre(listeCartes)
                regleTrouve = valeurCarte != None
                valeurJeu = 80
                texte = "Carré"

            elif regle == "full":
                valeurCarte = self.jeuAvecFull(listeCartes)
                regleTrouve = valeurCarte != None
                valeurJeu = 70
                texte = "Full"

            elif regle == "couleur":
                valeurCarte = self.jeuAvecCouleurIdentique(listeCartes)
                regleTrouve = valeurCarte != None
                valeurJeu = 60
                texte = "Couleur"
                
            elif regle == "suite":
                valeurCarte = self.jeuAvecSuite(listeCartes)          
                regleTrouve = valeurCarte != None
                valeurJeu = 40
                texte = "Suite"

            elif regle == "brelan":
                valeurCarte = self.jeuAvecBrelan(listeCartes)
                regleTrouve = valeurCarte != None
                valeurJeu = 30
                texte = "Brelan"

            elif regle == "double-paire":
                valeurCarte = self.jeuAvecDoublepairs(listeCartes)
                regleTrouve = valeurCarte != None
                valeurJeu = 20
                texte = "Double paire"

            elif regle == "paire":
                valeurCarte = self.jeuAvecPair(listeCartes)
                regleTrouve = valeurCarte != None
                valeurJeu = 10
                texte = "Paire"

            elif regle == "hauteur":
                valeurCarte = self.recupererCarteLaPusGrosse(listeCartes)
                regleTrouve = valeurCarte != None
                valeurJeu = 0
                texte = "Hauteur"

            if regleTrouve == False:
                indiceRegle = indiceRegle + 1

        return {"indiceJoueur": indiceJoueurManche, "jeuTrouve": regle, "texte": texte, "valeurJeu": valeurJeu, "valeurCarte": valeurCarte}

    # on récupère les valeurs de toutes les cartes et on retourne une liste avec les valeurs
    def recupererValeursCartes(self, listCartes: List[Carte])->List[int]:
        valeursCartes: List[int] = []
        for carte in listCartes:
            valeursCartes.append(carte.getValeur())

        return valeursCartes
            
    # On recherche les valeurs en regardant combien y a de valeurs identiques
    # on retourne une liste qui contient la liste des valeurs identiques et une autre liste avec le total trouvés
    # Par exemple ça peut retourner [[1, 5, 6], [1, 4, 2]] : on voit ici que la valeur 5 a été trouvé 5 fois 
    def recupererNombreValeursIdentiques(self, valeursCartes: List[int])->List[List[int]]:
        valeursIdentiquesCartes: List[int] = []
        totalMemeValeurCartes: List[int] = []

        for valeur in valeursCartes:
            if (valeur not in valeursIdentiquesCartes):
                valeursIdentiquesCartes.append(valeur)
                totalMemeValeurCartes.append(valeursCartes.count(valeur))

        return [valeursIdentiquesCartes, totalMemeValeurCartes]

    # Permet de vérifier si les valeurs de la liste list1 se trouve bien dans list2
    # si identique on retourne true
    def verifierValeursListsIdentiques(self, list1: List[int], list2: List[int])->bool:
        identique: bool = True

        for valeur in list1:
            if (valeur not in list2):
                identique = False
                break
        
        return identique
    
    # Permet de vérifier si on a une suite de 5 cartes, on retourne la valeur de la plus grosse valeur de la suite
    def verifierSiSuite(self, listeValeurs: List[int])->int:
        valeurCarteSuitePlusForte = None
        
        # On va trier la liste des valeurs par ordre croissant
        listeValeurs.sort()
        
        indiceValeur = 0
        valeurPrecedente = None
        nombreValeursSuite = 1
        for valeur in listeValeurs:
            if (indiceValeur > 0):
                if (valeurPrecedente + 1 == valeur):
                    nombreValeursSuite = nombreValeursSuite + 1
                    
                    if (nombreValeursSuite == 5):
                        valeurCarteSuitePlusForte = valeur
                else:
                    nombreValeursSuite = 1
            
            valeurPrecedente = valeur
            indiceValeur = indiceValeur + 1
            
        return valeurCarteSuitePlusForte
    
    # Regroupe les cartes par familles (coeurs, pique...) avec les cartes correspondant à la famille
    # on retourne un dictionnaire
    # par exemple {'pique': [2, 4, 5, 7], 'coeur': [3, 6, 2]}, les valeurs de carte pour la famille coeur sera : 3, 6, 2
    def regrouperCartesTriesParFamille(self, cartesJoueur: List[Carte])->dict:
        valeursCarteParFamille: dict = {}
        # On va regrouper les valeurs des cartes par couleur
        for carte in cartesJoueur:
            famille = carte.getFamille()
            valeur = carte.getValeur()
            if (valeursCarteParFamille.get(famille) == None):
                valeursCarteParFamille[famille] = [valeur]
            else:
               valeursCarteParFamille[famille].append(valeur)  
               
        # On va trier les valeurs pour chaque couleur       
        for famille in valeursCarteParFamille:
            valeursCarteParFamille[famille].sort()
               
        return valeursCarteParFamille     
                      
    # Vérifie si quinte flush royale dans les cartes, retourne un boolean
    def jeuAvecQuinteFlushRoyale(self, cartesJoueur: List[Carte])->bool:
        #  valet : 11 - dame : 12 - roi : 13 - as : 14
        valeursCartesRoyale = [10, 11, 12, 13, 14]

        existQuinte: bool = False
        valeursCarteParFamille: dict = self.regrouperCartesTriesParFamille(cartesJoueur)

        # Pour chaque famille on va vérifier la valeur des cartes pour savoir si on a une quinte flush royale
        for famille in valeursCarteParFamille:
            existQuinte = self.verifierValeursListsIdentiques(valeursCartesRoyale, valeursCarteParFamille[famille])
            if (existQuinte):
                break
  
        return existQuinte

    # Vérifie si quinte flush dans les cartes, retourne la valeur de la carte la plus importante de la quinte flush sinon si pas de quinte flush None
    def jeuAvecQuinteFlush(self, cartesJoueur: List[Carte])->int:
        maxCarte: int = None

        valeursCarteParFamille: dict = self.regrouperCartesTriesParFamille(cartesJoueur)
        
        # Pour chaque famille on va vérifier la valeur des cartes pour savoir si on a une suite de la même couleur
        for famille in valeursCarteParFamille:        
            maxCarte = self.verifierSiSuite(valeursCarteParFamille[famille])
            if (maxCarte != None):
                break
      
        return maxCarte

    # Vérifie si carré dans les cartes, retourne la valeur de la carte du carré si trouvé
    def jeuAvecCarre(self, cartesJoueur: List[Carte])->int:
        maxCarteCarre: int = None

        valeursCartes: List[int] = self.recupererValeursCartes(cartesJoueur)
        listValeurIdentique, listTotalValeursIdentiques = self.recupererNombreValeursIdentiques(valeursCartes)
        
        # on va regarder si on a 4 quatres identiques
        if (listTotalValeursIdentiques.count(4) == 1):
            indiceTableau = listTotalValeursIdentiques.index(4)
            maxCarteCarre = listValeurIdentique[indiceTableau]

        return maxCarteCarre

    # Vérife si full dans les cartes, retourne la valeur des 3 cartes identiques si trouvé
    def jeuAvecFull(self, cartesJoueur: List[Carte])->int:
        maxValeur3CartesIdentique: int = None

        valeursCartes: List[int] = self.recupererValeursCartes(cartesJoueur)
        listValeurIdentique, listTotalValeursIdentiques = self.recupererNombreValeursIdentiques(valeursCartes)
        
        # on va regarder si on a 3 cartes identiques et une paire
        indiceTableau3Cartes = -1
        
        # Si on a trouvé 3 cartes identiques et une paire
        if (listTotalValeursIdentiques.count(3) > 0 and listTotalValeursIdentiques.count(2) > 0):
            # On va rechercher la valeur des 3 cartes identiques
            indiceTableau3Cartes = listTotalValeursIdentiques.index(3)
            maxValeur3CartesIdentique = listValeurIdentique[indiceTableau3Cartes]

        return maxValeur3CartesIdentique

    # Vérifie si 5 cartes avec la même couleur dans les cartes, si trouvé retourne la plus grosse valeur de carte de la couleur
    def jeuAvecCouleurIdentique(self, cartesJoueur: List[Carte])->int:
        valeurPlusGrosseCarteCouleur = None
        
        valeursCarteParFamille: dict = self.regrouperCartesTriesParFamille(cartesJoueur)
        
        # Pour chaque famille on va vérifier si on a une couleur de 5 cartes de même famille
        for famille in valeursCarteParFamille:
            valeursFamille = valeursCarteParFamille[famille]
            if (len(valeursFamille) >= 5):
                valeurPlusGrosseCarteCouleur = max(valeursFamille)

        return valeurPlusGrosseCarteCouleur

    # Vérifie si suite dans les cartes, si trouvé retourne la plus grosse valeur de carte de la suite
    def jeuAvecSuite(self, cartesJoueur: List[Carte])->int:
        valeurPlusGrosseCarte = None
        
        valeursCartes: List[int] = self.recupererValeursCartes(cartesJoueur)
        valeurPlusGrosseCarte = self.verifierSiSuite(valeursCartes)

        return valeurPlusGrosseCarte

    # Vérifie si brelan dans les cartes, si trouvé retourne la valeur de carte du brelan
    def jeuAvecBrelan(self, cartesJoueur: List[Carte])->int:
        maxCarteBrelan: int = None

        valeursCartes: List[int] = self.recupererValeursCartes(cartesJoueur)
        listValeursIdentiques, listTotalValeursIdentiques = self.recupererNombreValeursIdentiques(valeursCartes)
        
        # on va regarder si on a 3 cartes identiques
        if listTotalValeursIdentiques.count(3) > 0:
            indiceTableau3Cartes = listTotalValeursIdentiques.index(3)
            maxCarteBrelan = listValeursIdentiques[indiceTableau3Cartes]
                                 
        return maxCarteBrelan

    # Vérifie si double pairs dans les cartes, si trouvé retourne la valeur de carte de la plus grosse paire
    def jeuAvecDoublepairs(self, cartesJoueur: List[Carte])->int:
        nombrePairs = 0
        carteMaxDoublePaire = 0
        
        valeursCartes: List[int] = self.recupererValeursCartes(cartesJoueur)       
        listValeursIdentiques, listTotalValeursIdentiques = self.recupererNombreValeursIdentiques(valeursCartes)
    
        indiceTab = 0
        for total in listTotalValeursIdentiques:
            if total >= 2:
                nombrePairs = nombrePairs + 1
                valeur = listValeursIdentiques[indiceTab]
                if (valeur > carteMaxDoublePaire):
                    carteMaxDoublePaire = valeur
                        
            indiceTab = indiceTab + 1
            
        if (nombrePairs >= 2):
            return carteMaxDoublePaire
        else:
            return None

    # Vérifie si pair dans les cartes, si trouvé retourne la valeur de carte de la pair
    def jeuAvecPair(self, cartesJoueur: List[Carte])->int:
        carteMaxPaire = None

        valeursCartes: List[int] = self.recupererValeursCartes(cartesJoueur)
        listValeursIdentiques, listTotalValeursIdentiques = self.recupererNombreValeursIdentiques(valeursCartes)

        indiceTab = 0
        for total in listTotalValeursIdentiques:
            if total >= 2:
                carteMaxPaire = listValeursIdentiques[indiceTab]
                break
                        
            indiceTab = indiceTab + 1
            
        return carteMaxPaire

    # Récupère la plus grosse valeur de cartes de la liste de cartes
    def recupererCarteLaPusGrosse(self, cartesJoueur: List[Carte])->int:
        return max(self.recupererValeursCartes(cartesJoueur))

if __name__ == "__main__" : 
    print("-----------------------------------")    
    print("TEST :")

    fenetre = pygame.display.set_mode((900, 700))
    pygame.init()    

    # Test pour une liste de joueurs
    listeDictJoueurs = [{"nomJoueur": "Tata", "gainsJoueur": 50, "avatar": "athena.png"},
                        {"nomJoueur": "Toto", "gainsJoueur": 50, "avatar": "boy.png"},
                        {"nomJoueur": "Titi", "gainsJoueur": 50, "avatar": "chicken.png"},
                        {"nomJoueur": "Tutu", "gainsJoueur": 50, "avatar": "giraffe.png"}]
    listeJoueurs = []
    for joueurDict in listeDictJoueurs:
        joueur = Joueur(joueurDict["nomJoueur"], joueurDict["gainsJoueur"], "./Images/Avatar/{0}".format(joueurDict["avatar"]))
        listeJoueurs.append(joueur)
                
    pageJeu = PageJeu(listeJoueurs, fenetre, "./Images/Theme/Defaut/fondPageJouer.png")    

    # Test de toutes les combinaisons
    # Quinte Flush Royale (toutes les cartes de la même couleur, séquence as - roi - renne - valet - 10)
    print("Test Quinte Flush Royale")
    cartesJoueur = [Carte(13, "coeur"), Carte(2, "pique"), Carte(11, "coeur"), Carte(14, "coeur"), Carte(10, "coeur"), Carte(2, "trefle"), Carte(12, "coeur")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))

    # Quinte Royale (toutes les cartes de la même couleur avec une suite de 5 cartes)
    print("Test Quinte Royale")
    cartesJoueur = [Carte(8, "pique"), Carte(2, "pique"), Carte(10, "pique"), Carte(9, "pique"), Carte(2, "coeur"), Carte(7, "pique"), Carte(11, "pique")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))
        
    # Carré (quatre cartes de même valeur, par exemple A-A-A-A)
    print("Test Carré")
    cartesJoueur = [Carte(10, "coeur"), Carte(5, "coeur"), Carte(10, "pique"), Carte(10, "carreau"), Carte(5, "pique"), Carte(7, "trefle"), Carte(10, "coeur")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))

    # Full (trois cartes du même type et une paire)
    print("Full")
    cartesJoueur = [Carte(8, "trefle"), Carte(2, "pique"), Carte(10, "trefle"), Carte(8, "coeur"), Carte(5, "pique"), Carte(10, "carreau"), Carte(8, "pique")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))
        
    # Couleur (toutes les cartes de la même couleur)
    print("Couleur")
    cartesJoueur = [Carte(9, "coeur"), Carte(2, "pique"), Carte(2, "coeur"), Carte(5, "coeur"), Carte(2, "carreau"), Carte(12, "coeur"), Carte(8, "coeur")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))
    
    # Quinte (ou Suite) (une séquence de base comme 6-5-4-3-2)
    print("Suite")
    cartesJoueur = [Carte(9, "coeur"), Carte(2, "coeur"), Carte(7, "trefle"), Carte(8, "coeur"), Carte(3, "coeur"), Carte(10, "carreau"), Carte(6, "pique")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))

    # Brelan (trois cartes de même valeur, par exemple 5-5-5)
    print("Brelan")
    cartesJoueur = [Carte(10, "coeur"), Carte(5, "pique"), Carte(7, "trefle"), Carte(2, "coeur"), Carte(12, "pique"), Carte(10, "carreau"), Carte(10, "pique")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))

    # Double Paire (Deux paires, comme 9-9 ET 5-5)
    print("Double paire")
    cartesJoueur = [Carte(10, "coeur"), Carte(7, "trefle"), Carte(8, "trefle"), Carte(2, "coeur"), Carte(12, "pique"), Carte(8, "carreau"), Carte(10, "pique")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))
    
    # Paire (toute paire, qu'il s'agisse de A-A ou de 2-2). La paire d’As étant la plus forte et gagne contre une autre paire
    print("Paire")
    cartesJoueur = [Carte(4, "coeur"), Carte(7, "trefle"), Carte(8, "trefle"), Carte(12, "pique"), Carte(6, "coeur"), Carte(8, "carreau"), Carte(2, "pique")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))

    # Hauteur (carte la plus haute)
    print("Hauteur")
    cartesJoueur = [Carte(2, "coeur"), Carte(11, "trefle"), Carte(4, "trefle"), Carte(6, "coeur"), Carte(5, "coeur"), Carte(10, "carreau"), Carte(8, "pique")] 
    print(pageJeu.determinerJeuJoueur(cartesJoueur, 1))

    # On démarre le jeu
    pageJeu.demarrerNouvelleManche()