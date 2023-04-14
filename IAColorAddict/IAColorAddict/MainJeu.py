from Jeu.Jeu import Jeu
from Jeu.Joueur import Joueur
from Jeu.Carte import Carte  
from PagesGraphique.Fenetre import Fenetre
from PagesGraphique.PopUp import PopUp
from PagesGraphique.PopUpIA import PopUpIA
# from PagesGraphique.pop import PopUpIA

from PagesGraphique.PopUpMulticolor import PopUpMulticolor

from os import listdir
import pygame
import time
import psycopg2

import os




# --------------------------------------------------------------------------
# -- Ce programme permet de gérer le jeu Graphique                        --
# --------------------------------------------------------------------------



class MainJeu():
    def __init__(self, dictionnaire_joueur : list, background) :
        self.dictionnaire_joueur = dictionnaire_joueur
        self.liste = self.dictionnaire_joueur
        self.background = background
        self.count_multicouleur = 0
        self.cartes_multicouleur = []
        self.count_pioche = 0
        self.count_pioche = []
        
        self.nom_joueur : list[Joueur] = []

        self.mydb = psycopg2.connect(
        host = "localhost",
        database = "base_color_addict",
        port = "5432",
        user = "laetitia",
        password = "1806"
)
        self.mycursor = self.mydb.cursor()

        
        
        ## Liste du nom des joueurs (pour la classe Jeu)
        for i in range(len(dictionnaire_joueur)) : 
            self.nom_joueur.append(Joueur(dictionnaire_joueur[i]['nomJoueur'],dictionnaire_joueur[i]['type'], dictionnaire_joueur[i]['niveau']))
            print( self.nom_joueur.append(Joueur(dictionnaire_joueur[i]['nomJoueur'],dictionnaire_joueur[i]['type'], dictionnaire_joueur[i]['niveau'])))
            
    
        # Le jeu 
        self.jeu : Jeu = Jeu(self.nom_joueur)
        
        # Carte au centre du Jeu ; modifiée à chaque fois qu'un joueur pose une carte  
        self.carte_centre = Carte(self.jeu.carteAuCentre.getCouleur(), self.jeu.carteAuCentre.getTitre())
                
        # Nouvelle fenêtre qui se réactualise à chaque fois que l'on change de joueur       
        self.nouvelle_fenetre = Fenetre(self.liste, self.jeu.getJoueurCourant().getMainJoueur(), self.carte_centre, self.jeu, self.background)



    def update_liste(self) : 
        ''' Cette classe permet de modifier la file d'attente. Le Joueur 1 après avoir joué, se retrouve
        dernier de la file d'attente.'''
        variable = self.liste.pop(0) 
        self.liste.append(variable)

        
         
        
    def PassageJoueurSuivant(self) : 
        ''' Cette méthode permet de réactualiser la fenêtre et d'autres paramètres'''
        nouveau = []
        variable = ''
        
        for i in range(len(self.dictionnaire_joueur)) : 
            if i == 0 : 
                variable = self.dictionnaire_joueur[0] 
            else : 
                nouveau.append(self.dictionnaire_joueur[i])
        
        nouveau.append(variable)
        self.update_liste()
        
        print('-------------------------------------------------------------')
        
        
        self.nouvelle_fenetre = Fenetre(self.liste, self.jeu.getJoueurCourant().getMainJoueur(), self.carte_centre, self.jeu, self.background)
        

        
           
        
    def afficherPop(self,  nom, avatar): 
        ''' Cette méthode permet d'afficher le pop up de changement de joueur, d'une durée de 1.25s'''
        fin = time.time() + 1.25 
        pop = PopUp( nom, self.background, avatar)
        
        while time.time()<fin:
            pop.afficherPopUp()


    def afficherPopIA(self, avatar, JeuIa, multi): 
        ''' Cette méthode permet d'afficher le pop up de changement de joueur, d'une durée de 1.25s'''
        # if JeuIa == None : 
        if JeuIa == None : 
            fin = time.time() + 3
        else : 
            fin = time.time() + 1.75
        pop = PopUpIA(avatar,  self.background, fin, JeuIa, multi)
        i = 10
        while time.time()<fin:
            i = i-0.1
            pop.afficherPopUp(int(i))

            



    def afficherPopMulticolor(self): 
        ''' Cette méthode permet d'afficher le pop up qui permet au joueur de choisir sa couleur après avoir posé une carte multicolor'''

        pop = PopUpMulticolor(self.background)
        pop.afficherPopUpMulticolor()
        valeur = pop.attendreChoix()
        
        return valeur
    

                
    def run(self): 
        ''' Cette méthode gère le jeu ; change de joueur, vérifie si victoire, en fonction de la réponse du joueur, joue la carte... '''
        run = True
        i = 0
        

        while run:
            
            
            # En cas de victoire ; on retourne "Fin" pour que dans MainGraphique, on affiche la page de Fin
            if self.jeu.victoireJoueur() == True : 
                run = False
                return "Fin"
            
            # Dans le cas où le bouton fermer à été cliqué ; on retourne "Fermer" pour que dans MainGraphique, on affiche la page d'accueil
            if self.nouvelle_fenetre.bouton_quitter == True : 
                run = False
                return "Fermer"

            
            
            # Affichage Pop Up / et fene^tre 
            self.afficherPop( self.jeu.getJoueurCourant().getNom(), self.liste[0]["avatar"])
            self.nouvelle_fenetre.afficherFenetre()
            print("le dico joueur" + self.jeu.getJoueurCourant().afficherMain())

            

            for carte in self.jeu.getJoueurCourant().getMainJoueur():
                #  boucle sur les cartes que possède un joueur dans sa main
                multicouleur = carte
                print ("joueur courant est: " + self.jeu.getJoueurCourant().getNom())
                print (multicouleur.getCouleur())
                print (multicouleur.getTitre())
                # print("valeur de i:" +i)
                # print("carte Joueur:"+ multicouleur)

                if (multicouleur.getCouleur() == 'multicolor' and multicouleur not in self.cartes_multicouleur):
                    #  si la carte est une multicouleur et que cette carte 'est pas dans le tableau empêche de compter 2 x la même
                    print ('multicouleur')
                    self.count_multicouleur = self.count_multicouleur + 1
                    #  +1 au compteur
                    self.cartes_multicouleur.append(multicouleur)
                    self.cartes_multicouleur.append(self.jeu.getJoueurCourant().getNom())
                    #  ajoute dans le tableau 
                    print (self.cartes_multicouleur)
                    print("le joueur courant :" + self.jeu.getJoueurCourant().getNom())
                    
                    if ( len(self.cartes_multicouleur) != 0):
                        print (  len(self.cartes_multicouleur))
                        print ("salut diif de 0")
                        sqlnom = "SELECT nom_joueur FROM deroulement_partie WHERE nom_joueur = %s"
                        valeurs = (self.jeu.getJoueurCourant().getNom(),)
                        self.mycursor.execute(sqlnom,valeurs)
                        result = self.mycursor.fetchone()
                        print("--------------")
                        print(valeurs)
                    
                        if result is None:
                            print("pas dans le tableau")
                            sql = "INSERT INTO deroulement_partie (nom_joueur,carte_multicouleur) values (%s,1)"
                            valeurs = (self.jeu.getJoueurCourant().getNom(),)
                            self.mycursor.execute(sql, valeurs)
                            self.mydb.commit()
                            print(sql)
                            print("--------------")
                            print(valeurs)
                        else:
                            print ("je suis DANS LE TABLEAU")
                            sqlcount = "SELECT carte_multicouleur FROM deroulement_partie WHERE nom_joueur = %s"
                            print(self.jeu.getJoueurCourant().getNom())

                            self.mycursor.execute(sqlcount, (self.jeu.getJoueurCourant().getNom(),))
                     
                            result = self.mycursor.fetchone()
                            count = result[0]
                            sql = "UPDATE deroulement_partie SET carte_multicouleur = %s WHERE nom_joueur = %s"
                            valeurs = (count + 1, self.jeu.getJoueurCourant().getNom())
                            self.mycursor.execute(sql, valeurs)
                            self.mydb.commit()

             

                
            print("carteaucentre",self.jeu.getCarteMillieu().getCouleur(), self.jeu.getCarteMillieu().getCouleur() )
            
            if (self.jeu.getJoueurCourant().getNom() == 'IA') : 
                self.afficherPopIA(self.liste[0]["avatar"], None, None)
                # valeur, multi = self.jeu.jeuIA()
                valeur, multi= self.jeu.jeuIA()

                if valeur == "pioche" : 
                    if len(self.jeu.getJoueurCourant().getMainJoueur()) < 5 : 
                        self.jeu.getJoueurCourant().piocherCarteSiPossible()
                        

                else : 
                    self.carte_centre = valeur
                    
                self.afficherPopIA(self.liste[0]["avatar"], valeur, multi)

            else : 
         
                # Attente d'une réponse de l'utilisateur
                while self.nouvelle_fenetre.selectionnercarte() != True : 
                    self.nouvelle_fenetre.selectionnercarte()
                    sqlnom = "SELECT nom_joueur FROM partie_pioche WHERE nom_joueur = %s"
                    valeurs = (self.jeu.getJoueurCourant().getNom(),)
                    self.mycursor.execute(sqlnom,valeurs)
                    result = self.mycursor.fetchone()
                    print("--------------")
                    print(valeurs)
                        
                    if result is None:
                        print("pas dans le tableau")
                        sql = "INSERT INTO partie_pioche (nom_joueur,count_pioche) values (%s,1)"
                        valeurs = (self.jeu.getJoueurCourant().getNom(),)
                        self.mycursor.execute(sql, valeurs)
                        self.mydb.commit()
                        print(sql)
                        print("--------------")
                        print(valeurs)
                    else:
                        print ("je suis DANS LE TABLEAU")
                        sqlcount = "SELECT count_pioche FROM partie_pioche WHERE nom_joueur = %s"
                        print(self.jeu.getJoueurCourant().getNom())

                        self.mycursor.execute(sqlcount, (self.jeu.getJoueurCourant().getNom(),))
                        self.mydb.commit()
                        result = self.mycursor.fetchone()
                        count = result[0]
                        sql = "UPDATE partie_pioche SET count_pioche = %s WHERE nom_joueur = %s"
                        valeurs = (count + 1, self.jeu.getJoueurCourant().getNom())
                        self.mycursor.execute(sql, valeurs)
                        self.mydb.commit()

                        print(sql)
                        print("--------------")
                        print(valeurs)
                    
                # Dans le cas où le bouton fermer à été cliqué ; on retourne "Fermer" pour que dans MainGraphique, on affiche la page d'accueil
                if self.nouvelle_fenetre.bouton_quitter == True : 
                    run = False
                    return "Fermer"
                
                # Si il a cliqué sur la pioche, on pioche si possible
                if self.nouvelle_fenetre.pioche_active == True : 
                    if len(self.jeu.getJoueurCourant().getMainJoueur()) < 5 : 
                        self.jeu.getJoueurCourant().piocherCarteSiPossible()
                        # self.count_pioche = self.count_pioche + 1
                        
                        # self.cartes_multicouleur.append(multicouleur)
                        # print (self.cartes_multicouleur)
                        # print("le joueur courant :" + self.jeu.getJoueurCourant().getNom())
                        # return self.cartes_multicouleur and self.count_multicouleur
                    
                    
                else : 
                    
                    # Si il a cliqué sur une carte, on joue la carte
                    self.carte_centre = self.nouvelle_fenetre.get_carte_centre()
                    self.jeu.jouerCarte(self.carte_centre)
                    
                    # Vérification si elle est multicolor ; si oui -> PopUp Multicolor
                    if self.carte_centre.getCouleur() == "multicolor" :
                        valeur = self.afficherPopMulticolor()
                        self.carte_centre = Carte(self.jeu.getCarteMillieu().getTitre(),valeur)
                        self.jeu.setCarteMillieu(self.carte_centre)
                        
                    
                    
            if self.jeu.victoireJoueur() == True : 
                run = False
                return "Fin"
            
            
            self.jeu.changementDeJoueur()
            self.PassageJoueurSuivant()
           
            
            
            
            pygame.display.update()
            
            

   
            
       
            
            
            

    