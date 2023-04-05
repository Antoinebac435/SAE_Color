from os import listdir
import os
import pygame
from Autre.Texte import Texte
from Boutons.Bouton import Bouton

from Boutons.BoutonListe import BoutonListe
from Boutons.BoutonImageListe import BoutonImageListe
from Autre.ChampSaisie import ChampSaisie


# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher une fenêtre qui est la page du choix   --
# -- des joueurs. Ils peuvent choisir leurs noms/avatars, si la partie     --
# -- est en mode aléatoire, ou non...                                      --
# ---------------------------------------------------------------------------



class PageCreationPartieEnLigne():
    
    def __init__(self, fenetre, background_image) :
        
        self.fenetre = fenetre
        self.listeOrdre = ["Aléatoire","Dans l'ordre"]
        self.listeNbJoueur = ["2","3","4"]
        self.background_image = background_image
        self.nombreJoueurs = 0
        # self.type 
        
    def afficherPageCreationPartie(self):
        pygame.init()
      
        #Background
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        Texte(self.fenetre,"Nom de la partie", 25, (255,255,255), 340, 160)

        # nom Partie
        self.champSaisieNomPartie = ChampSaisie(280, 200,350,45,(243,223,36),self.fenetre)
        
        
        self.champListNbJoueurs = BoutonListe("Nombre de joueurs",25,self.listeNbJoueur,280,350,350,45,(243,223,36),self.fenetre)
        # Ordre Joueur
        self.champListOrdreJoueurs = BoutonListe("Ordre des joueurs",25,self.listeOrdre,280,450,350,45,(243,223,36),self.fenetre)
        
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
        clickBouton: bool = self.boutonValider.verifier_click_bouton(positionClick)
        
        if (self.boutonValider.verifier_click_bouton(positionClick)):

            # Si pas de nom, on va en mettre un par défaut
            nomPartie = self.champSaisieNomPartie.getTexte()
           
            if (nomPartie == ""):
                nomPartie = "NO NAME"
                
            # self.boutonNiveau = None
                
            self.infoPartie = {"nomPartie": nomPartie,
                        "nbJoueur": int(self.champListNbJoueurs.getChoix())}
            
        return clickBouton
    
    def getInfoPartie(self):
        return self.infoPartie
               
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
                    self.champListNbJoueurs.verifierClickDeplacement(positionClick)
                    self.champListOrdreJoueurs.verifierClickDeplacement(positionClick)
                    
                    
                    # Si le bouton vérifier valider a été cliqué
                    self.verifierValider(positionClick)
                    
                    # Si on a validé et on a tous les joueurs
                    if self.boutonValider.verifier_click_bouton(positionClick) == True:
                        choix = "joueur"
                        choixEffectue = True
                    
                # Si on écrit au clavier
                elif (event.type == pygame.KEYDOWN):
                    self.champSaisieNomPartie.verifierSaisie(event.key)   
                    
                # Si on appuie sur la croix pour quitter 
                elif (event.type == pygame.QUIT):
                    choixEffectue = True   
        
        return choix       



