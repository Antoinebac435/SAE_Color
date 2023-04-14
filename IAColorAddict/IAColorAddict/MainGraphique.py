import datetime
import psycopg2
import pygame
import os
import random
from Jeu.GestionPartieReseau import GestionPartieReseau

from PagesGraphique.PageAcceuil import PageAcceuil
from PagesGraphique.PageChoixJouer import PageChoixJouer
from PagesGraphique.PageCreationJoueurEnLigne import PageCreationJoueurEnLigne
from PagesGraphique.PageCreationPartieEnLigne import PageCreationPartieEnLigne
from PagesGraphique.PageJoueurAttenteEnLigne import PageAttenteJoueurEnLigne
from PagesGraphique.PageOption import PageOption
from PagesGraphique.PageRegles import PageRegles
from PagesGraphique.PageStats import PageStats
from PagesGraphique.PageMentionLegale import PageMentionLegale
from PagesGraphique.PageReseau import PageReseau
from PagesGraphique.PagefinPartie import PagefinPartie
from MainJeu import MainJeu
from Jeu.Joueur import Joueur
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# --------------------------------------------------------------------------
# -------------------------     Bienvenu !    ------------------------------
# ---------------------    Lancez le programme !    ------------------------
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# -- Ce programme permet de lancer de jeu de manière graphique le jeu     --
# -- Cet de gérer les différentes pages.                                  --
# --------------------------------------------------------------------------



if "__main__" == __name__:
    
    fenetre = pygame.display.set_mode((900, 700))
    pygame.init()
    musique = pygame.mixer.Sound(os.path.join('ressources','musique', 'musique.mp3'))
    canal_1 = pygame.mixer.Channel(0)
    canal_1.play(musique)
    background = "Defaut"
    pageEnCours = "Acceuil"
    listeJoueurs: list[Joueur] = []


    mydb = psycopg2.connect(
        host = "localhost",
        database = "base_color_addict",
        port = "5432",
        user = "laetitia",
        password = "1806"
)
    mycursor = mydb.cursor()

    run = True
    changementPage = True
    joueur_gagne = None
        
    while run:
        
        pAcceuil = PageAcceuil(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))    
        pChoixJouer = PageChoixJouer(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        pOption = PageOption(fenetre, canal_1, os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        pRegles = PageRegles(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        PMentionLegale = PageMentionLegale(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        pStats = PageStats(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        PfinPartie = PagefinPartie(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'), joueur_gagne)
        pReseau = PageReseau(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        pCreationPartieEnLigne = PageCreationPartieEnLigne(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        pjoueurEnLigne = PageCreationJoueurEnLigne(fenetre,os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        pAttenteJoueurEnLigne = PageAttenteJoueurEnLigne(fenetre, os.path.join('ressources', 'Theme', background, 'fondPageAcceuil.png'))
        gestionPartieReseau = GestionPartieReseau(pAttenteJoueurEnLigne)


        ## Affichage de la page d'accueil
        if (changementPage == True and pageEnCours == "Acceuil"):
            pAcceuil.afficherPageAcceuil()
            pageEnCours = pAcceuil.attendreChoix()
            changementPage = True
            if (pAcceuil.attendreChoix() == "Fermer"):
                pygame.QUIT
                run = False 


        ## Affichage de la page des options     
        if (changementPage == True and pageEnCours == "Option"):
            pOption.afficherPageOption()
            choix = pOption.attendreChoix()

            if (choix == "MentionLegale"):
                pageEnCours = "MentionLegale"
                changementPage = True
   
            if (choix == None):
                pageEnCours = "Acceuil"
                changementPage = True
                
            background = pOption.choixTheme

        if (changementPage == True and pageEnCours == "EnLigne"):
            pReseau.afficherPageReseau()
            choix = pReseau.attendreChoix()
            if (choix == None):
                pageEnCours = "Acceuil"
                changementPage = True
                
            if (choix == "Creer"):
                pageEnCours = "CreationPartieEnLigne"
                changementPage = True
            elif (choix == "Rejoindre"):
                pjoueurEnLigne.afficherPageChoixJouer()
                pjoueurEnLigne.attendreChoix()   
                gestionPartieReseau.connecterServeur(pjoueurEnLigne.infosJoueur)

        if (changementPage == True and pageEnCours == "CreationPartieEnLigne"):
            pCreationPartieEnLigne.afficherPageCreationPartie()
            choix = pCreationPartieEnLigne.attendreChoix()
   
            if (choix == None):
                pageEnCours = "EnLigne"
                changementPage = True
            elif (choix == "joueur"):
                pageEnCours = "CreationJoueurEnLigne"
                changementPage = True
                
        if (changementPage == True and pageEnCours == "CreationJoueurEnLigne"):
                pjoueurEnLigne.afficherPageChoixJouer()
                choix = pjoueurEnLigne.attendreChoix()
                pjoueurEnLigne
                
                if (choix == "None"):
                    pageEnCours = "CreationPartie"
                    changementPage = True
                elif (choix == "Attente"):
                    # Création de la partie réseau
                    gestionPartieReseau.creerServeur()
                    gestionPartieReseau.attendreJoueursClient(pCreationPartieEnLigne.getInfoPartie(), pjoueurEnLigne.getInfosJoueur())
                                
        ## Affichage de la page des règles      
        if (changementPage == True and pageEnCours == "Regles"):
            pRegles.afficherPageRegles()
            choix = pRegles.attendreChoix()

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
         
        ## Affichage de la page des mentions légales   
        if (changementPage == True and pageEnCours == "MentionLegale"):
            PMentionLegale.afficherPageMention()
            choix = PMentionLegale.attendreChoix()

            if (choix == "Acceuil"):
                pageEnCours = "Acceuil"
                changementPage = True

            if (choix == None):
                pageEnCours = "Option"
                changementPage = True                
                
                
        ## Affichage de la page du choix des joeurs ET lancement de la partie
        elif (changementPage == True and pageEnCours == "Jouer"):
            pChoixJouer.afficherPageChoixJouer()
            choix = pChoixJouer.attendreChoix()
            
            if (choix == None):
                pageEnCours = "Acceuil"
                changementPage = True
                
            elif (choix == "Partie"):
                liste_joueur = pChoixJouer.listeJoueurs
                ordre = pChoixJouer.typePartie

                

                listeDictJoueurs = pChoixJouer.getListeJoueurs()
                               
                    # On boucle sur le dictionnaire des joueurs pour créer les joueurs de la page du jeu
                compteurRobot = 1
                for joueurDict in listeDictJoueurs:
                    if joueurDict["type"] == "IA":
                        joueur = Joueur("Bot"+str(compteurRobot), joueurDict["type"], joueurDict["niveau"])
                        compteurRobot += 1
                    else:
                        joueur = Joueur(joueurDict["nomJoueur"], joueurDict["type"], joueurDict["niveau"])
                        print(joueurDict["nomJoueur"])
                        sqlnom = "SELECT nom_joueur FROM joueur WHERE nom_joueur = %s"
                        mycursor.execute(sqlnom, (joueurDict["nomJoueur"],))
                        result = mycursor.fetchone()
                        if result is None:
                            sql = "INSERT INTO joueur (nom_joueur, nb_partie) VALUES (%s, 1)"
                            valeurs = (joueurDict["nomJoueur"],)
                            mycursor.execute(sql, valeurs)
                            mydb.commit()
                        else:
                            sqlcount = "SELECT nb_partie FROM joueur WHERE nom_joueur = %s"
                            mycursor.execute(sqlcount, (joueurDict["nomJoueur"],))
                            result = mycursor.fetchone()
                            count = result[0]
                            sql = "UPDATE joueur SET nb_partie = %s WHERE nom_joueur = %s"
                            valeurs = (count + 1, joueurDict["nomJoueur"])
                            mycursor.execute(sql, valeurs)
                            mydb.commit()


                        listeJoueurs.append(joueur)
                

                # Gestion d'ordre des joueurs
                if ordre != "Dans l'ordre": 
                    random.shuffle(liste_joueur)

                # Lancement de la partie
                p = MainJeu(liste_joueur, background)
                # print("la main du joueur est " +p.jeu.getJoueurCourant().getMainJoueur())

                p.run()
                pageEnCours = "Main" # changer le truc

                # Si victoire
                if p.run() == "Fin" : 
                    joueur_gagne = p.jeu.getJoueurCourant().getNom()
                    print("Le joueur qui a gagné est", joueur_gagne)


                    # sqlnom = "select id_joueur from joueur where nom_joueur = %s"
                    # sqlcount = "select count(nb_partie) from joueur where nom_joueur = %s"
                    # mycursor.execute(sqlcount, (joueurDict["nomJoueur"],))
                    # result = mycursor.fetchone()
                    # count = result[0]
                    sql = "INSERT INTO partie (nom_joueur,victoire) VALUES (%s,1)"
                    print(sql)
                    valeurs = (joueurDict["nomJoueur"],)
                    mycursor.execute(sql, valeurs)
                    # sqlnom = "select nom_joueur from joueur"

                    # if 

                    mydb.commit()
                    pageEnCours = "FinPartie"
                    changementPage = True
                    
                # si la croix a été cliquée : on retourne à l'acceuil    
                if p.run() == "Fermer" : 
                    pageEnCours = "Acceuil"
                    changementPage = True
                    
            else:
                changementPage = False
                
             
                
        ## Affichage de la page FIN de partie       
        elif (changementPage == True and pageEnCours == "FinPartie"):
            PfinPartie.afficherPagefinPartie()
            choix = PfinPartie.attendreChoix()
     
            
            if (choix == "Acceuil"):
                pageEnCours = "Acceuil"
                changementPage = True
            elif (choix == "Rejouer"):
                pageEnCours = "Jouer"
                changementPage = True

                
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False  
    
