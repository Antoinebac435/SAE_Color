from Jeu.Jeu import Jeu
from Jeu.Joueur import Joueur
from Jeu.Carte import Carte  
from os import listdir
import pygame
from PagesGraphique.PopUpMulticolor import PopUpMulticolor
import os

# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher une fenêtre. Cette fenêtre se compose  --
# -- des cartes du joueur courant, du nombre de cartes restantes de ce     --
# -- joueur mais aussi des autres. De l'avatar, et du nom des joueurs ...  --
# ---------------------------------------------------------------------------


class Fenetre():
    def __init__(self, dico, cartes_joueur, carte_centre, jeu, background ) : 
        self.fenetre = pygame.display.set_mode((900, 700))
        self.background = background
        self.jeu : Jeu = jeu 
        self.dico : list[dict]= dico 
        self.cartes_joueur : list[Carte] = cartes_joueur
        self.carte_centre : Carte = carte_centre
        
        ## Booléan servant à déterminer si la pioche et/ou le bouton a/ont été cliqué. 
        self.pioche_active : bool = False
        self.bouton_quitter : bool = False

        self.positions_centre = [400, 280]
        
        ## Ces positions diffèrent car lorsqu'un joueur possède 5 cartes, elles ne sont pas placées de la même manière que si il en avait que deux.
        self.positions = [[310 + 0*100, 530], [310 + 1*100, 530],[310 + 2*100, 530]]
        self.positions_une_carte_supplementaire = [[250 + 0*100, 530], [250 + 1*100, 530],[250 + 2*100, 530], [250 + 3*100, 530]]
        self.positions_deux_carte_supplementaire = [[130 + 0*100, 530], [130 + 1*100, 530],[130 + 2*100, 530], [130 + 3*100, 530], [130 + 4*100, 530]]

        ## Police d'écriture 
        self.fontNB = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 45)
        self.fontJOUEUR = pygame.font.Font(os.path.join('ressources', 'policeEcriture', 'Grandstander-clean.ttf'), 15)
        
        
        
        
      
    def afficherFenetre(self):
        '''Cette méthode sert à afficher une fenêtre'''
        
        pygame.init() 
        
        ## Background et croix pour quitter 
        self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Theme', self.background, 'background_jeu.png')),(0, 0))
        self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Outils' ,'signe-de-la-croix-removebg-preview.png')),(830, 15))
        
        ## Avatar / nom / cartes du joueur 1 
        self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[1]['avatar'])),(400, 100))
        self.fenetre.blit(self.fontJOUEUR.render(self.dico[1]['nomJoueur'], True, (255, 255, 255)), (420, 190))
        
        
        self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.carte_centre.getCouleur() + "_" + self.carte_centre.getTitre() + ".svg"), self.positions_centre)
        
        

        
        ## Affichage des cartes du Joueur Courrant dans le cas où il n'a qu'une carte dans sa main
        if len(self.cartes_joueur) ==1   : 
            self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[0]['avatar'])),(170, 550))
            self.fenetre.blit(self.fontJOUEUR.render(self.dico[0]['nomJoueur'], True, (255, 255, 255)), (190, 640))
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[0].getCouleur() + "_" + self.cartes_joueur[0].getTitre() + ".svg").convert_alpha(), [310 + 0*100, 530])
          
              
        ## Affichage des cartes du Joueur Courrant dans le cas où il n'a que deux cartes dans sa main 
        elif len(self.cartes_joueur) ==2   : 

            self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[0]['avatar'])),(170, 550))
            self.fenetre.blit(self.fontJOUEUR.render(self.dico[0]['nomJoueur'], True, (255, 255, 255)), (190, 640))
        
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[0].getCouleur() + "_" + self.cartes_joueur[0].getTitre() + ".svg").convert_alpha(), [310 + 0*100, 530])
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[1].getCouleur() + "_" + self.cartes_joueur[1].getTitre() + ".svg").convert_alpha(), [310 + 1*100, 530])  

        
        ## Affichage des cartes du Joueur Courrant dans le cas où trois cartes dans sa main        
        elif len(self.cartes_joueur) ==3   : 

            self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[0]['avatar'])),(170, 550))
            self.fenetre.blit(self.fontJOUEUR.render(self.dico[0]['nomJoueur'], True, (255, 255, 255)), (190, 640))
        
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[0].getCouleur() + "_" + self.cartes_joueur[0].getTitre() + ".svg").convert_alpha(), [310 + 0*100, 530])
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[1].getCouleur() + "_" + self.cartes_joueur[1].getTitre() + ".svg").convert_alpha(), [310 + 1*100, 530])  
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[2].getCouleur() + "_" + self.cartes_joueur[2].getTitre() + ".svg").convert_alpha()
        , [310 + 2*100, 530])   
            
                    
        ## Affichage des cartes du Joueur Courrant dans le cas où quatre cartes dans sa main        
        elif len(self.cartes_joueur) == 4   : 

            self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[0]['avatar'])),(170, 550))
            self.fenetre.blit(self.fontJOUEUR.render(self.dico[0]['nomJoueur'], True, (255, 255, 255)), (190, 640))
        
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[0].getCouleur() + "_" + self.cartes_joueur[0].getTitre() + ".svg").convert_alpha(), [250 + 0*100, 530])
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[1].getCouleur() + "_" + self.cartes_joueur[1].getTitre() + ".svg").convert_alpha(), [250 + 1*100, 530])  
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[2].getCouleur() + "_" + self.cartes_joueur[2].getTitre() + ".svg").convert_alpha()
        , [250 + 2*100, 530])   
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[3].getCouleur() + "_" + self.cartes_joueur[3].getTitre() + ".svg").convert_alpha(), [250 + 3*100, 530]  )



        ## Affichage des cartes du Joueur Courrant dans le cas où cinq cartes dans sa main        
        elif len(self.cartes_joueur) == 5   : 
            self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[0]['avatar'])),(50, 550))
            self.fenetre.blit(self.fontJOUEUR.render(self.dico[0]['nomJoueur'], True, (255, 255, 255)), (70, 640))
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[0].getCouleur() + "_" + self.cartes_joueur[0].getTitre() + ".svg").convert_alpha(), [130 + 0*100, 530])
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[1].getCouleur() + "_" + self.cartes_joueur[1].getTitre() + ".svg").convert_alpha(), [130 + 1*100, 530])  
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[2].getCouleur() + "_" + self.cartes_joueur[2].getTitre() + ".svg").convert_alpha(), [130 + 2*100, 530])   
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[3].getCouleur() + "_" + self.cartes_joueur[3].getTitre() + ".svg").convert_alpha(), [130 + 3*100, 530]  )
            self.fenetre.blit(pygame.image.load("./carte_color/carte_" + self.cartes_joueur[4].getCouleur() + "_" + self.cartes_joueur[4].getTitre() + ".svg").convert_alpha(), [130 + 4*100, 530]  )

        
          
        ## Affichage du nombre de cartes restantes dans la pioche du Joueur Courrant 
        nombre_carte_joueur_courant = len(self.jeu.listJoueur[0].getPiocheJoueur())
        txt_nb_carte_joueur_courant = self.fontNB.render(str(nombre_carte_joueur_courant), True, (248, 171, 12))
        self.fenetre.blit(txt_nb_carte_joueur_courant, (750, 500))
        
        self.fenetre.blit(pygame.image.load(os.path.join('ressources',  'dos_carte.svg')),(530, 40))
        
        
        ## Affichage du nombre de cartes restantes dans la pioche du Joueur Prochain
        nombre_carte_joueur_suivant_un = len(self.jeu.listJoueur[self.jeu.joueursuivant1].getPiocheJoueur())
        txt_nb_carte_joueur_suivant = self.fontNB.render(str(nombre_carte_joueur_suivant_un), True, (246, 1, 2))
        self.fenetre.blit(txt_nb_carte_joueur_suivant, (545, 78))
        
        
        ## Affichage du nombre de cartes restantes dans la pioche du Joueur qui suivent (3 et 4)
        if len(self.dico) == 3 : 
            self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[2]['avatar'])),(20, 365))
            self.fenetre.blit(self.fontJOUEUR.render(self.dico[2]['nomJoueur'], True, (255, 255, 255)), (35, 458))
            self.fenetre.blit(pygame.image.load(os.path.join('ressources',  'dos_carte.svg')),(80, 230))

            txt_nb_carte_joueur_suivant_deux= str(len(self.jeu.listJoueur[2].getPiocheJoueur()))
            font_txt = self.fontNB.render(str(txt_nb_carte_joueur_suivant_deux), True, (246, 1, 2))
            self.fenetre.blit(font_txt, (95, 268))
            
            
            
        if len(self.dico) == 4 : 
            
            self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[2]['avatar'])),(20, 365))
            self.fenetre.blit(self.fontJOUEUR.render(self.dico[2]['nomJoueur'], True, (255, 255, 255)), (35, 458))
            self.fenetre.blit(pygame.image.load(os.path.join('ressources',  'dos_carte.svg')),(80, 230))

            txt_nb_carte_joueur_suivant_deux= str(len(self.jeu.listJoueur[2].getPiocheJoueur()))
            font_txt = self.fontNB.render(str(txt_nb_carte_joueur_suivant_deux), True, (246, 1, 2))
            self.fenetre.blit(font_txt, (95, 268))
            
            self.fenetre.blit(pygame.image.load(os.path.join('ressources', 'Avatar', self.dico[3]['avatar'])),(800, 365))
            self.fenetre.blit(self.fontJOUEUR.render(self.dico[3]['nomJoueur'], True, (255, 255, 255)), (820, 458))
            self.fenetre.blit(pygame.image.load(os.path.join('ressources',  'dos_carte.svg')),(730, 230))
                
            txt_nb_carte_joueur_suivant_trois= str(len(self.jeu.listJoueur[3].getPiocheJoueur()))
            font_txt_trois = self.fontNB.render(str(txt_nb_carte_joueur_suivant_trois), True, (246, 1, 2))
            self.fenetre.blit(font_txt_trois, (745, 268))
            
        
                
        pygame.display.update()    
        
        return self.fenetre
    
    

        
    def get_carte_centre(self) : 
        ''' Méthode qui permet d'avoir la carte au centre'''
        return self.carte_centre
        
        
        
        
        
   
    def selectionnercarte(self): 
        
        
        done = False
        done2 = False
        
        
        
        ## Obligation de faire plusieurs boucles while car si un joueur possède 2 cartes, on ne peut pas cliquer au même endroit
        ## que si un joueur possédait 5 cartes. Les positions de clique sont différentes. 
        
        while not done : 
            
            ## Dans le cas où un joueur possède 1 carte à cliquer 
            if len(self.cartes_joueur) == 1   :
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_position = event.pos
                        
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_position = event.pos


                        ## Si il clique sur la pioche
                        if (630 <= mouse_position[0] <= 750) and (550 <= mouse_position[1] <= 650) : 
                            self.pioche_active = True 
                            return True
                        
                    
                        ## Si il clique sur la croix pour quitter
                        if (720 <= mouse_position[0] <= 865) and (10 <= mouse_position[1] <= 48) : 
                            self.bouton_quitter = True 
                            return True
        
                        ## Si il clique sur l'une positions des cartes
                        for i in range(len (self.positions)):
                            if (self.positions[i][0] <= mouse_position[0] <= self.positions[i][0] + 100) and (self.positions[i][1] <= mouse_position[1] <= self.positions[i][1] + 100):

                                pygame.draw.rect(self.fenetre, pygame.Color("#384468"), (self.positions[i][0]-2, self.positions[i][1]-2, 95, 148),  4, 17)
                                pygame.display.flip()
                                
                                # La carte est en sélection, mais il faut cliquer une deuxième fois dessus pour 
                                # qu'elle soit jouer et/ou déselectionée. 
                                
                                while not done2 :
                                    
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEMOTION:
                                            mouse_position = event.pos
                                            
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                        
                                            for i in range(len (self.positions)):
                                                if (self.positions[i][0] <= mouse_position[0] <= self.positions[i][0] + 100) and (self.positions[i][1] <= mouse_position[1] <= self.positions[i][1] + 100):
                                                    
                                                    if self.jeu.estJouable(self.cartes_joueur[i]) :
                                                        self.carte_centre = self.cartes_joueur[i]
                                                        self.centre = self.cartes_joueur[i]          
                                                        return True
                                    
                                                else : 
                                                    self.afficherFenetre()
                                                    done2 = True

                                                    
                        done = True
                
                
                
            ## Dans le cas où un joueur possède 2 cartes à cliquer 
            elif len(self.cartes_joueur) == 2   :
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_position = event.pos
                        
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_position = event.pos

                        ## Si il clique sur la pioche
                        if (630 <= mouse_position[0] <= 750) and (550 <= mouse_position[1] <= 650) : 
                            self.pioche_active = True 
                            return True
                        
                    
                        ## Si il clique sur la croix pour quitter
                        if (720 <= mouse_position[0] <= 865) and (10 <= mouse_position[1] <= 48) : 
                            self.bouton_quitter = True 
                            return True
        
        
                        ## Si il clique sur l'une positions des cartes
                        for i in range(len (self.positions)):
                            if (self.positions[i][0] <= mouse_position[0] <= self.positions[i][0] + 100) and (self.positions[i][1] <= mouse_position[1] <= self.positions[i][1] + 100):

                                pygame.draw.rect(self.fenetre, pygame.Color("#384468"), (self.positions[i][0]-2, self.positions[i][1]-2, 95, 148),  4, 17)
                                pygame.display.flip()
                                
                                # La carte est en sélection, mais il faut cliquer une deuxième fois dessus pour 
                                # qu'elle soit jouer et/ou déselectionée.
                                while not done2 : 
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEMOTION:
                                            mouse_position = event.pos
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            for i in range(len (self.positions)):
                                                if (self.positions[i][0] <= mouse_position[0] <= self.positions[i][0] + 100) and (self.positions[i][1] <= mouse_position[1] <= self.positions[i][1] + 100):
                                                    if self.jeu.estJouable(self.cartes_joueur[i]) : 
                                                        self.carte_centre = self.cartes_joueur[i]
                                                        self.centre = self.cartes_joueur[i]          
                                                      
                                                        return True
                                    
                                                
                                                else : 
                                                    self.afficherFenetre()
                                                    done2 = True
                                                    
                        done = True
            
            
            
            
            
            
            
            
            
            
            
                
                
            ## Dans le cas où un joueur possède 3 cartes à cliquer 
            elif len(self.cartes_joueur) == 3   :
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_position = event.pos
                        
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_position = event.pos
                        
                        ## Si il clique sur la pioche
                        if (630 <= mouse_position[0] <= 750) and (550 <= mouse_position[1] <= 650) : 
                            self.pioche_active = True 
                            return True
                        
                    
                        ## Si il clique sur la croix pour quitter
                        if (720 <= mouse_position[0] <= 865) and (10 <= mouse_position[1] <= 48) : 
                            self.bouton_quitter = True 
                            return True
        
                        ## Si il clique sur l'une positions des cartes
                        for i in range(len (self.positions)):
                            if (self.positions[i][0] <= mouse_position[0] <= self.positions[i][0] + 100) and (self.positions[i][1] <= mouse_position[1] <= self.positions[i][1] + 100):

                                pygame.draw.rect(self.fenetre, pygame.Color("#384468"), (self.positions[i][0]-2, self.positions[i][1]-2, 95, 148),  4, 17)
                                pygame.display.flip()
                                

                                # La carte est en sélection, mais il faut cliquer une deuxième fois dessus pour 
                                # qu'elle soit jouer et/ou déselectionée.
                                while not done2 : 
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEMOTION:
                                            mouse_position = event.pos
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            for i in range(len (self.positions)):
                                                if (self.positions[i][0] <= mouse_position[0] <= self.positions[i][0] + 100) and (self.positions[i][1] <= mouse_position[1] <= self.positions[i][1] + 100):
                                                    if self.jeu.estJouable(self.cartes_joueur[i]) : 
                                                        self.carte_centre = self.cartes_joueur[i]
                                                        self.centre = self.cartes_joueur[i]
                                                        
                                                        return True
                                    
                                                else : 
                                                    self.afficherFenetre()
                                                    done2 = True
                                                
                                                    
                        done = True
                        
                        
                        
                        
            ## Dans le cas où un joueur possède 4 cartes à cliquer 
            elif len(self.cartes_joueur) == 4   :
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_position = event.pos
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_position = event.pos
                        

                        ## Si il clique sur la pioche
                        if (630 <= mouse_position[0] <= 750) and (550 <= mouse_position[1] <= 650) : 
                            self.pioche_active = True 
                            return True
                        
                        
                        ## Si il clique sur la croix pour quitter
                        if (720 <= mouse_position[0] <= 865) and (10 <= mouse_position[1] <= 48) : 
                            self.bouton_quitter = True 
                            return True
                        
                        
                        ## Si il clique sur l'une positions des cartes
                        for i in range(len (self.positions_une_carte_supplementaire)):
                            if (self.positions_une_carte_supplementaire[i][0] <= mouse_position[0] <= self.positions_une_carte_supplementaire[i][0] + 100) and (self.positions_une_carte_supplementaire[i][1] <= mouse_position[1] <= self.positions_une_carte_supplementaire[i][1] + 100):

                                pygame.draw.rect(self.fenetre, pygame.Color("#384468"), (self.positions_une_carte_supplementaire[i][0]-2, self.positions_une_carte_supplementaire[i][1]-2, 95, 148),  4, 17)
                                pygame.display.flip()
                                
                                
                                # La carte est en sélection, mais il faut cliquer une deuxième fois dessus pour 
                                # qu'elle soit jouer et/ou déselectionée.
                                while not done2 : 
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEMOTION:
                                            mouse_position = event.pos
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                     
                                            for i in range(len (self.positions_une_carte_supplementaire)):
                                                if (self.positions_une_carte_supplementaire[i][0] <= mouse_position[0] <= self.positions_une_carte_supplementaire[i][0] + 100) and (self.positions_une_carte_supplementaire[i][1] <= mouse_position[1] <= self.positions_une_carte_supplementaire[i][1] + 100):
                                                    if self.jeu.estJouable(self.cartes_joueur[i]) : 
                                                        self.carte_centre = self.cartes_joueur[i]
                                                        self.centre = self.cartes_joueur[i]
                                                        return True
                                                    
                                                else : 
                                                    self.afficherFenetre()
                                                    done2 = True

                                                    
                        done = True
                    
                pygame.display.update()
        
    
    
    
    
    
    
    
    
            ## Dans le cas où un joueur possède 5 cartes à cliquer 
            elif len(self.cartes_joueur) == 5   :
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mouse_position = event.pos
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_position = event.pos

                        ## Si il clique sur la pioche
                        if (630 <= mouse_position[0] <= 750) and (550 <= mouse_position[1] <= 650) : 
                            self.pioche_active = True 
                            return True
                        
                    
                        ## Si il clique sur la croix pour quitter
                        if (720 <= mouse_position[0] <= 865) and (10 <= mouse_position[1] <= 48) : 
                            self.bouton_quitter = True 
                            return True
        
        
                        ## Si il clique sur l'une positions des cartes
                        for i in range(len (self.positions_deux_carte_supplementaire)):
                            if (self.positions_deux_carte_supplementaire[i][0] <= mouse_position[0] <= self.positions_deux_carte_supplementaire[i][0] + 100) and (self.positions_deux_carte_supplementaire[i][1] <= mouse_position[1] <= self.positions_deux_carte_supplementaire[i][1] + 100):

                                pygame.draw.rect(self.fenetre, pygame.Color("#384468"), (self.positions_deux_carte_supplementaire[i][0]-2, self.positions_deux_carte_supplementaire[i][1]-2, 95, 148),  4, 17)
                                pygame.display.flip()
                                
                                # La carte est en sélection, mais il faut cliquer une deuxième fois dessus pour 
                                # qu'elle soit jouer et/ou déselectionée.
                                while not done2 : 
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEMOTION:
                                            mouse_position = event.pos
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            
                                            for i in range(len (self.positions_deux_carte_supplementaire)):
                                                if (self.positions_deux_carte_supplementaire[i][0] <= mouse_position[0] <= self.positions_deux_carte_supplementaire[i][0] + 100) and (self.positions_deux_carte_supplementaire[i][1] <= mouse_position[1] <= self.positions_deux_carte_supplementaire[i][1] + 50):
                                                    if self.jeu.estJouable(self.cartes_joueur[i]) : 
                                                        self.carte_centre = self.cartes_joueur[i]
                                                        self.centre = self.cartes_joueur[i]
                                                        return True
                                    
                                                else : 
                                                    self.afficherFenetre()
                                                    done2 = True
                                                
                                                    
                        done = True                                 
                                                 
                pygame.display.update()
        pygame.display.update()
   
        
        
        
            
        
        
        
        
    
        
   
        
        
                

        


    