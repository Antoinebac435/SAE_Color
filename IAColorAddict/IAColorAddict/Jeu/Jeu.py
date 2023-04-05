import random
from Jeu.Carte import Carte
from Jeu.JeuCartes import JeuCartes
from Jeu.Joueur import Joueur




# ------------------------------------------------------------------------
# -- Cette classe permet de créer un Jeu et toutes les méthodes         --
# -- nécesserent au déroulement du Jeu.                                 --
# ------------------------------------------------------------------------

titres = ['jaune','rouge','rose','vert','orange','noir','bleu', 'marron','gris','violet']



class Jeu():
    def __init__(self, listJoueur : list[Joueur]) :        
        self.listJoueur : list[Joueur] = listJoueur
        self.joueurCourant : int = 0
        self.joueursuivant1 : int = 1                                     #Ce procédé sert à faire tourner correctement les joueurs. Une queue/file d'attente
        self.joueursuivant2 : int = 2
        self.joueursuivant3 : int = 3
        
        ## Distribution et mélange du Jeu de Carte. 
        self.jeuCartes : JeuCartes = JeuCartes()
        self.jeuCartes.melanger()
        self.jeuCartes.distribuerJeu(len(listJoueur))
        
    
        ## Carte au centre ; qui va changer en fonction de ce qu'un joueur va jouer. 
        self.carteAuCentre : Carte  = self.jeuCartes.carteMilieu
        
        ## Permet d'avoir toutes les cartes des joueurs. 
        self.tabCartesJoueurs : list[list[Carte]] = self.jeuCartes.tab_CartesJoueurs
        
        
        ## On constitue la pioche des joueurs
        for indexJoueur in range (0,len(listJoueur)):
            joueur : Joueur = self.listJoueur[indexJoueur]
            joueur.setPiocheJoueur(self.tabCartesJoueurs[indexJoueur])
            
            for i in range(0,3):                                           #Pioche 3 cartes
                joueur.piocherCarteSiPossible()


    def printCarte(self) : 
        '''Méthode redéfinie car ne marchait pas'''
        print(self.tabCartesJoueurs)

    def getJoueurCourant(self):
        '''Méthode qui permet d'avoir le Joueur courant'''
        return self.listJoueur[self.joueurCourant]
    
    def getCarteMillieu(self):
        '''Méthode qui permet d'avoir la carte posée au milieu du jeu'''
        return self.carteAuCentre
    
    def setCarteMillieu(self, carteAuCentre : Carte):
        '''Méthode qui permet de modifier la carte du milieu (la remplacer par une autre qui vient d'être jouée)'''
        self.carteAuCentre = carteAuCentre
        
    def victoireJoueur(self):
        ''' Méthode qui vérifie si un joueur a gagné'''
        if (len(self.getJoueurCourant().getMainJoueur()) == 0):
            return True
        
        
    
        
    
    
    def changementDeJoueur(self):
        ''' Méthode qui permet de passer au joueur suivant '''                
        if (self.joueurCourant == len(self.listJoueur)-1) : 
            self.joueurCourant = 0
        else :
            self.joueurCourant += 1
            
            
        if (self.joueursuivant1 == len(self.listJoueur)-1) : 
            self.joueursuivant1 = 0
        else :
            self.joueursuivant1 += 1
        
        
        if len(self.listJoueur) == 3 :
              
            if (self.joueursuivant2 == len(self.listJoueur)-1) : 
                self.joueursuivant2 = 0
            else :
                self.joueursuivant2 += 1
            
                  
          
            if len(self.listJoueur) == 4:
                if (self.joueursuivant3 == len(self.listJoueur)-1) : 
                    self.joueursuivant3 = 0
                else :
                    self.joueursuivant3 += 1
                    
            
    
    
    def estJouable(self, carte : Carte):
        ''' Méthode qui permet de vérifier si il est possible de poser la carte (selon les règles 
        du jeu) '''
        jouable = False
        
        if (carte.getTitre() == self.carteAuCentre.getTitre()) or (carte.getCouleur() == self.carteAuCentre.getCouleur()) or (carte.getTitre() == self.carteAuCentre.getCouleur()) or (carte.getCouleur() == self.carteAuCentre.getTitre()):
            jouable = True
        elif (carte.getCouleur() == "multicolor") : 
            jouable = True 

        return jouable
    
    
    
    
    def jouerCarte(self, carte : Carte):
        ''' Méthode qui pose la carte souhaitée au centre du jeu. Et donc l'enlève de la main du joueur '''
        joueur : Joueur = self.listJoueur[self.joueurCourant]        

        if self.estJouable(carte) == True : 
            main_joueur : list[Carte]= joueur.getMainJoueur()
            main : list[Carte] = []
            
            ##On supprime la carte du main
            for element in main_joueur : 
                if (element.getCouleur() == carte.getCouleur()) and (element.getTitre() == carte.getTitre()) : 
                    if len(main_joueur) == 3 : 
                        joueur.piocherCarteSiPossible()
                else:
                    main.append(element)
                    

            joueur.setMainJoueur(main)
            self.carteAuCentre = carte
            
            
            
            
            
    def jeuIA(self) : 
        joueur : Joueur = self.listJoueur[self.joueurCourant]
        main_joueur : list[Carte]= joueur.getMainJoueur()
        print('Carte1', main_joueur[0].getCouleur(),  main_joueur[0].getTitre()) 
        print('Carte2', main_joueur[1].getCouleur(),  main_joueur[1].getTitre()) 
        print('Carte3', main_joueur[2].getCouleur(),  main_joueur[2].getTitre()) 
        
        jouable = False 
 
        
        if joueur.getNiveauIa() == 'Facile' : 
        ##IA DEBUTANT
        #Test pour savoir si une carte au moins est jouable 
            for i in range(len(main_joueur)) : 
                carte = main_joueur[i]
                if self.estJouable(carte) : 
                    jouable = True 
                    if carte.getCouleur() == 'multicolor' :  
                        ## Choisi une couleur au hasard
                        self.jouerCarte(carte)
                        new_carte = Carte(carte.getTitre(), random.choice(titres)) 
                        return new_carte, carte
                    else : 
                        self.jouerCarte(carte)
                        return carte, None
                    
            if jouable == False : 
                return 'pioche', None
        
        
        else : 
            ##IA MOYEN
            carte_meme_couleur_meme_titre = None 
            carte_multicolor = None 
            carte_pas_meme_couleur_pas_meme_titre= None
            
            
            for i in range(len(main_joueur)) : 
                carte = main_joueur[i]
                if self.estJouable(carte) : 
                    jouable = True 
                    if carte.getCouleur() == carte.getTitre() : 
                        carte_meme_couleur_meme_titre = carte
                    elif carte.getCouleur() == 'multicolor' :
                        carte_multicolor = True
                        ## Son choix doit être plus réflechi ! 
                        # Il doit choisir une couleur en fonction des autres cartes présentes dans sa main
                        carte_multicolor = carte
                    else :
                        carte_pas_meme_couleur_pas_meme_titre = carte
                        
            
            if carte_meme_couleur_meme_titre != None : 
                self.jouerCarte(carte_meme_couleur_meme_titre) 
                return carte_meme_couleur_meme_titre, None
            
            elif carte_pas_meme_couleur_pas_meme_titre != None  : 
                self.jouerCarte(carte_pas_meme_couleur_pas_meme_titre) 
                return carte_pas_meme_couleur_pas_meme_titre, None
            
            elif carte_multicolor != None :
                new_c = None
                self.jouerCarte(carte_multicolor) 
                choix_eff = False
                
                for indice_carte in range(len(main_joueur)) : 
                    une_carte = main_joueur[indice_carte]
                    
                    if une_carte.getCouleur() != 'multicolor' :
                        new_c= Carte(carte_multicolor.getTitre(), une_carte.getTitre()) 
                        print("non aleatoire",  une_carte.getTitre())
                        choix_eff = True 
                  
                # On rentre dans la boucle que quand on a QUE des cartes multicolor dans sa main (cas très rare)      
                if choix_eff == False : 
                    new_c = Carte(carte_multicolor.getTitre(), random.choice(titres)) 
                    print('aleatoire')
                    choix_eff = True 
        
                
                
                return new_c, carte_multicolor
            else : 
                return 'pioche', None
                
    
        
        
        
            
                
              
                
        
            
            
    
            
            
    
        
 