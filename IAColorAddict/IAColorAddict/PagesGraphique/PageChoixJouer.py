from os import listdir
import os
import pygame
from Boutons.Bouton import Bouton

from Boutons.BoutonListe import BoutonListe
from Boutons.BoutonImageListe import BoutonImageListe
from Autre.ChampSaisie import ChampSaisie


# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher une fenêtre qui est la page du choix   --
# -- des joueurs. Ils peuvent choisir leurs noms/avatars, si la partie     --
# -- est en mode aléatoire, ou non...                                      --
# ---------------------------------------------------------------------------



class PageChoixJouer():
    
    def __init__(self, fenetre, background_image) :
        self.fenetre = fenetre
        self.listeOrdre = ["Aléatoire","Dans l'ordre"]
        self.listeType = ["Joueur","IA"]
        self.listeNiveau = ["Facile","Moyen"]
        self.listeNbJoueur = ["2","3","4"]
        self.ImagesAvatar = listdir(os.path.join('ressources', 'avatar'))
        self.joueur = 1
        self.listeJoueurs = []
        self.background_image = background_image
        self.nombreJoueurs = 0
        self.typejoueur = None
        self.typePartie = None
        self.typeNiveau = None 
        # self.type 
        
        
        
    def afficherPageChoixJouer(self, estJoueur1 = True):
        pygame.init()
        print('test')

        #Background
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))

        if (estJoueur1):
            # Nb Joueur 
            self.champListNbJoueurs = BoutonListe("Nombre de joueurs",25,self.listeNbJoueur,280,80,350,45,(243,223,36),self.fenetre)
            # Ordre Joueur
            self.champListOrdreJoueurs = BoutonListe("Ordre des joueurs",25,self.listeOrdre,280,200,350,45,(243,223,36),self.fenetre)
            # Choix du gain
            self.boutonIA = None
            self.boutonNiveau = None
            positionYAvatar = 400
        else:            
            positionYAvatar = 135
            
            self.boutonIA = BoutonListe("Type de joueur",25,self.listeType,280,400,350,45,(243,223,36),self.fenetre)
            self.boutonNiveau = BoutonListe("Niveau de l'IA",25,self.listeNiveau,280,550,350,45,(243,223,36),self.fenetre)



        # Choix image avatar
        self.champListAvatars = BoutonImageListe("Joueur "+ str(self.joueur),self.ImagesAvatar,280,positionYAvatar,350,45,(243,223,36),self.fenetre)

        # nom
        self.champSaisieNom = ChampSaisie(280, positionYAvatar + 100,350,45,(243,223,36),self.fenetre)
        
        # bouton valider
        self.boutonValider = Bouton(720,620,120,50,(243,223,36),"Valider",self.fenetre,18)
        rectContour = pygame.draw.rect(self.fenetre, (0,0,0),(720,620,120,50), 3, 5)
        
        # bouton retour
        retour = os.path.join('ressources', 'Outils', 'retour.png')

        retourImage = pygame.image.load(retour)
        self.boxRetour = retourImage.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(retourImage, self.boxRetour)
    
        pygame.display.update()
        
        
        
        
    def verifierValider(self, positionClick):
        ''' Cette méthode récupère une fois qu'on a cliqué sur Valider toutes les informations que l'utilisateur a choisi'''
        if (self.joueur == 1):
            self.nombreJoueurs = self.champListNbJoueurs.getChoix()
            self.typePartie = self.champListOrdreJoueurs.getChoix()
            
      
        clickBouton: bool = self.boutonValider.verifier_click_bouton(positionClick)
        
        
        
        if (self.boutonValider.verifier_click_bouton(positionClick) and self.joueur <= int(self.champListNbJoueurs.getChoix()) ):
            if self.boutonIA != None : 
                self.typejoueur = self.boutonIA.getChoix()
                
                
            if self.boutonNiveau != None : 
                self.typeNiveau = self.boutonNiveau.getChoix()
                
            print(self.typeNiveau)

            # Si pas de nom, on va en mettre un par défaut
            nomJoueur = self.champSaisieNom.getTexte()
           
            if (nomJoueur == ""):
                nomJoueur = "Joueur {0}".format(self.joueur)
                
            # self.boutonNiveau = None
                
            if self.typejoueur == "IA" : 
                infosJoueur = {"nomJoueur": 'IA' ,
                           "avatar": os.path.join('ia.png'),
                           "type" : "IA",
                           "niveau" : self.typeNiveau}
                
            else : 

                infosJoueur = {"nomJoueur": nomJoueur,
                            "avatar": self.champListAvatars.getImageAvatar(), 
                            "type": "Joueur", 
                            "niveau" : None}
   
            self.listeJoueurs.append(infosJoueur)
            self.joueur += 1
            self.afficherPageChoixJouer(False)    
            
        return clickBouton
    
    
    
    def getListeJoueurs(self):
        return self.listeJoueurs
    
    
               
    def attendreChoix(self):
        ''' Cette méhode attend le choix de l'utilisateur. Elle attend que l'utilisateur clique sur l'un des boutons. '''

        choixEffectue = False
        choix = None
        
        while choixEffectue == False:
            for event in pygame.event.get():
                
                # Si on clique gauche n'importe où
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
                        
                    # Si c'est ces champs qui ont été cliqué 
                    self.champListAvatars.verifierClickDeplacement(positionClick)
                    self.champListNbJoueurs.verifierClickDeplacement(positionClick)
                    self.champListOrdreJoueurs.verifierClickDeplacement(positionClick)
                    
                    if self.boutonIA != None : 
                        self.boutonIA.verifierClickDeplacement(positionClick)
                        
                    if self.boutonNiveau != None : 
                        self.boutonNiveau.verifierClickDeplacement(positionClick)
                    
                    # Si le bouton vérifier valider a été cliqué
                    self.verifierValider(positionClick)
                    
                    # Si on a validé et on a tous les joueurs
                    if self.joueur == int(self.champListNbJoueurs.getChoix()) + 1:
                        choix = "Partie"
                        choixEffectue = True
                    
                    
                # Si on écrit au clavier
                elif (event.type == pygame.KEYDOWN):
                    self.champSaisieNom.verifierSaisie(event.key)   
                    
                # Si on appuie sur la croix pour quitter 
                elif (event.type == pygame.QUIT):
                    choixEffectue = True   
        
        return choix       



