from os import listdir
import os
import pygame
from Boutons.Bouton import Bouton

from Boutons.BoutonImageListe import BoutonImageListe
from Autre.ChampSaisie import ChampSaisie




class PageCreationJoueurEnLigne():
    
    def __init__(self, fenetre, background_image) :
        self.fenetre = fenetre

        self.ImagesAvatar = listdir(os.path.join('ressources', 'avatar'))
        self.background_image = background_image

        
    def afficherPageChoixJouer(self):
        pygame.init()

        self.infosJoueur = None

        #Background
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))

        # Choix image avatar
        self.champListAvatars = BoutonImageListe("Joueur ", self.ImagesAvatar,280,200,350,45,(243,223,36),self.fenetre)

        # nom
        self.champSaisieNom = ChampSaisie(280, 200 + 100,350,45,(243,223,36),self.fenetre)
        
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
            nomJoueur = self.champSaisieNom.getTexte()
           
            if (nomJoueur == ""):
                nomJoueur = self.champSaisieNom.getTexte()
                
            # self.boutonNiveau = None
         
            self.infosJoueur = {"nomJoueur": nomJoueur,
                        "avatar": self.champListAvatars.getImageAvatar(), 
                        "type": "Joueur", 
                        "niveau" : None}
            
        return clickBouton
    
    def getInfosJoueur(self):
        return self.infosJoueur
    
    def attendreChoix(self):
        ''' Cette méthode attend le choix de l'utilisateur. Elle attend que l'utilisateur clique sur l'un des boutons. '''

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

                    # Si le bouton vérifier valider a été cliqué
                    self.verifierValider(positionClick)
                    # Si on a validé et on a tous les joueurs
                    if self.boutonValider.verifier_click_bouton(positionClick):
                        choix = "Attente"
                        choixEffectue = True

                    
                # Si on écrit au clavier
                elif (event.type == pygame.KEYDOWN):
                    self.champSaisieNom.verifierSaisie(event.key)   
                    
                # Si on appuie sur la croix pour quitter 
                elif (event.type == pygame.QUIT):
                    pygame.quit()
                    choixEffectue = True   
        
        return choix       
