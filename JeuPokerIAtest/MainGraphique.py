import datetime
import psycopg2
import pygame
import mysql.connector 
from Joueur import Joueur
# import MySQLdb

from PageAcceuil import PageAcceuil
from PageChoixJouer import PageChoixJouer
from PageJeu import PageJeu
from PageOption import PageOption
from PageRegles import PageRegles
from PageStats import PageStats
from PageMentionLegale import PageMentionLegale
from PagefinPartie import PagefinPartie
from typing import List

if "__main__" == __name__:

    fenetre = pygame.display.set_mode((900, 700))
    pygame.init()
    
    musique = pygame.mixer.Sound('./musique/m.mp3')    # Musique par défaut
    canal_1 = pygame.mixer.Channel(0)
    canal_1.play(musique)      # Lancement de la musique
    background = "Defaut"       # On affiche un background par défaut au départ
    pageEnCours = "Acceuil"     # Par défaut on affiche l'accueil
    listeJoueurs: List[Joueur] = []
    
    mydb = psycopg2.connect(
        host = "localhost",
        database = "base_poker",
        port = "5432",
        user = "laetitia",
        password = "1806"
)
    mycursor = mydb.cursor()

    run = True
    changementPage = True
    
    while run:
        pAcceuil = PageAcceuil(fenetre,"./images/Theme/"+ background+"/fondPageAcceuil.png")    
        pChoixJouer = PageChoixJouer(fenetre,"./images/Theme/"+ background+"/fondPageAutre.png")
        pOption = PageOption(fenetre, canal_1, "./images/Theme/"+ background+"/fondPageAutre.png")
        pRegles = PageRegles(fenetre,"./images/Theme/"+ background+"/fondPageAutre.png")
        pStats = PageStats(fenetre,"./images/Theme/"+ background+"/fondPageAutre.png")
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
                compteurRobot = 1

                for joueurDict in listeDictJoueurs:
                    if joueurDict["typeJoueur"] == "Robot":
                        joueur = Joueur("Bot"+str(compteurRobot), joueurDict["gainsJoueur"], "./Images/Avatar/bot.png", True, joueurDict["difficulte"])
                        compteurRobot += 1
                    else :
                        joueur = Joueur(joueurDict["nomJoueur"], joueurDict["gainsJoueur"], "./Images/Avatar/{0}".format(joueurDict["avatar"]), False, None)


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
        
        # Affichage de la page des Stats du jeu
        if (changementPage == True and pageEnCours == "Stats"): 
            pStats.afficherPageStats()
            choix = pStats.attendreChoix()

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
                    compteurRobot = 1
                    for joueurDict in listeDictJoueurs:
                        if joueurDict["typeJoueur"] == "Robot":
                            joueur = Joueur("Bot"+str(compteurRobot), joueurDict["gainsJoueur"], "./Images/Avatar/bot.png", True, joueurDict["niveauIA"])
                            compteurRobot += 1
                    else:
                        joueur = Joueur(joueurDict["nomJoueur"], joueurDict["gainsJoueur"], "./Images/Avatar/{0}".format(joueurDict["avatar"]), False, None)
                        print(joueurDict["nomJoueur"])
                        sqlnom = "select nom_joueur from joueur where joueur.nom_joueur = %s"
                        mycursor.execute(sqlnom, (joueurDict["nomJoueur"],))
                        result = mycursor.fetchone()
                        if result is None:
                            sql = "INSERT INTO joueur (nom_joueur,nb_partie) VALUES (%s,1)"
                            valeurs = (joueurDict["nomJoueur"],)
                            mycursor.execute(sql, valeurs)
                            mydb.commit()
                        else:
                            sqlnom = "select nom_joueur from joueur"
                            sqlcount = "select count(nb_partie) from joueur where nom_joueur = %s"
                            mycursor.execute(sqlcount, (joueurDict["nomJoueur"],))
                            result = mycursor.fetchone()
                            count = result[0]
                            sql = "INSERT INTO joueur (nom_joueur,nb_partie) VALUES (%s,%s)"
                            valeurs = (joueurDict["nomJoueur"], count)
                            mycursor.execute(sql, valeurs)
                            count = result[0]
                            sql = "delete from joueur where nom_joueur = %s and nb_partie < %s"
                            valeurs = (joueurDict["nomJoueur"], count)
                            mycursor.execute(sql, valeurs)
                            mydb.commit()

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
    
# mycursor.close()

