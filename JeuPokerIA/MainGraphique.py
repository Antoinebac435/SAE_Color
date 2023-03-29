import pygame
from Joueur import Joueur

from PageAcceuil import PageAcceuil
from PageChoixJouer import PageChoixJouer
from PageJeu import PageJeu
from PageOption import PageOption
from PageRegles import PageRegles
from PageMentionLegale import PageMentionLegale
from PagefinPartie import PagefinPartie
from typing import List
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if "__main__" == __name__:
    
    fenetre = pygame.display.set_mode((900, 700))
    pygame.init()
    
    musique = pygame.mixer.Sound('./musique/m.mp3')    # Musique par défaut
    canal_1 = pygame.mixer.Channel(0)
    canal_1.play(musique)      # Lancement de la musique
    background = "Defaut"       # On affiche un background par défaut au départ
    pageEnCours = "Acceuil"     # Par défaut on affiche l'accueil
    listeJoueurs: List[Joueur] = []

    run = True
    changementPage = True
    
    while run:
        pAcceuil = PageAcceuil(fenetre,"./images/Theme/"+ background+"/fondPageAcceuil.png")    
        pChoixJouer = PageChoixJouer(fenetre,"./images/Theme/"+ background+"/fondPageAutre.png")
        pOption = PageOption(fenetre, canal_1, "./images/Theme/"+ background+"/fondPageAutre.png")
        pRegles = PageRegles(fenetre,"./images/Theme/"+ background+"/fondPageAutre.png")
        PMentionLegale = PageMentionLegale(fenetre,"./images/Theme/"+ background+"/fondPageAutre.png")
        PfinPartie = PagefinPartie(fenetre,"./images/Theme/"+ background+"/fondPageAutre.png")
        
        # Affichage de la page accueuil
        if (changementPage == True and pageEnCours == "Acceuil"):
            pAcceuil.afficherPageAcceuil()
            pageEnCours = pAcceuil.attendreChoix()
            changementPage = True

            # On quitte
            if (pageEnCours == "Fermer"):
                pygame.QUIT
                run = False 

        # Affichage de la page de fin de partie on retourne ensuite sur l'accueil
        if (changementPage == True and pageEnCours == "finPartie"):
            PfinPartie.afficherPagefinPartie()
            choix = PfinPartie.attendreChoix()
   
            if (choix == "Acceuil"):
                pageEnCours = "Acceuil"
                changementPage = True
                listeJoueurs = []
            elif (choix == "Rejouer"):
                # On boucle sur le dictionnaire des joueurs pour créer les joueurs de la page du jeu
                listeJoueurs = []
                for joueurDict in listeDictJoueurs:
                    joueur = Joueur(joueurDict["nomJoueur"], joueurDict["gainsJoueur"], "./Images/Avatar/{0}".format(joueurDict["avatar"]),joueurDict["typeJoueur"])
                    listeJoueurs.append(joueur)
                pageEnCours = "Jouer"
                changementPage = True

        # Affichage des la page des options
        elif (changementPage == True and pageEnCours == "Option"):
            pOption.afficherPageOption()
            choix = pOption.attendreChoix()

            # Choix pour l'affichage des mentions légales
            if (choix == "MentionLegale"):
                pageEnCours = "MentionLegale"
                changementPage = True
            # Pas de choix on affiche l'accueil
            elif (choix == None):
                pageEnCours = "Acceuil"
                changementPage = True
                
            # on récupère le thème des options
            background = pOption.choixTheme

        # Affichage de la page des règles du jeu
        if (changementPage == True and pageEnCours == "Regles"): 
            pRegles.afficherPageRegles()
            choix = pRegles.attendreChoix()

            # pas de choix on retourne sur l'accueil
            if (choix == None):
                pageEnCours = "Acceuil"
                changementPage = True
        
        # Afichage de la page des mentions légales
        if (changementPage == True and pageEnCours == "MentionLegale"):
            PMentionLegale.afficherPageMention()
            choix = PMentionLegale.attendreChoix()
            
            # choix pour retourner sur l'accueil
            if (choix == "Acceuil"):
                pageEnCours = "Acceuil"
                changementPage = True

            # pas de choix on retourne sur les options
            if (choix == None):
                pageEnCours = "Option"
                changementPage = True
                
        # Affichage de la page du jeu, démarrage partie
        elif (changementPage == True and pageEnCours == "Jouer"):
            if (len(listeJoueurs) == 0):
                pChoixJouer.afficherPageChoixJouer()
                choix = pChoixJouer.attendreChoix()
                
                # On a choisit de revenir sur l'acceuil
                if (choix == None):
                    pageEnCours = "Acceuil"
                    changementPage = True
                elif (choix == "Partie"):
                    # On va récupérer la liste des joueurs
                    listeDictJoueurs = pChoixJouer.getListeJoueurs()
                            
                    # On boucle sur le dictionnaire des joueurs pour créer les joueurs de la page du jeu
                    for joueurDict in listeDictJoueurs:
                        joueur = Joueur(joueurDict["nomJoueur"], joueurDict["gainsJoueur"], "./Images/Avatar/{0}".format(joueurDict["avatar"]),joueurDict["typeJoueur"] )
                        # print("ttestjoueur", joueur.getBot())
                        listeJoueurs.append(joueur)
            else:
                choix = "Partie"
                
            # On a choisit les joueurs, la partie peut commencer
            if (choix == "Partie"):
                pageEnCours = "Partie"
                
                pagePartie = PageJeu(listeJoueurs, fenetre, "./Images/Theme/"+background+"/fondPageJouer.png") 
                retour = pagePartie.demarrerNouvelleManche()
                
                if retour == 'accueil':
                    pageEnCours = "Acceuil"
                    changementPage = True
                    listeJoueurs = []
                elif retour == 'finPartie':
                    pageEnCours = "finPartie"
                    changementPage = True                    
            else:
                changementPage = False   

        # Permet de quitter l'application
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False  
    


