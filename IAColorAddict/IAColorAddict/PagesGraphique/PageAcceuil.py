import pygame
import os

from Boutons.Bouton import Bouton
from Boutons.Boutoncercle import Boutonc


# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher une fenêtre qui est la page d'acceuil  --
# -- du jeu. Elle se compose de 3 boutons ; Jouer, Options et Règles       --
# ---------------------------------------------------------------------------



class PageAcceuil():
    def __init__(self, fenetre, background_image) :
        pygame.init()
        
        #Fenetre
        self.fenetre = fenetre
        self.background_image = background_image

    

    
    def afficherPageAcceuil(self):
        pygame.display.set_caption("Jeu : Color Addict - serveur")
        
        # -- 
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        #Croix pour quitter
        self.croixQuitter = os.path.join('ressources', 'Outils', 'signe-de-la-croix-removebg-preview.png')
        background = pygame.image.load(self.croixQuitter)
        self.fenetre.blit(background,(10, 10))
        
        #Logo Stats
        self.Stats = os.path.join('ressources', 'Outils', 'Resize_statistics.png')
        background = pygame.image.load(self.Stats)
        self.fenetre.blit(background,(10, 50))
        
        
        # Image Background en fonction du thème choisi par l'utilisateur
        # Obligé de faire plusieurs conditions car les logos ne font pas la même taille, 
        # Et ne sont pas positionnés de la même manière. Exemple : le background Noel a une bannière en haut
        # donc le logo doit se trouver plus bas sur la page.
        if self.background_image == os.path.join('ressources', 'Theme','Noel',  'fondPageAcceuil.png') : 
            logo =  os.path.join('ressources', 'Theme','Noel','logoAcceuil.png')
            background = pygame.image.load(logo)
            self.fenetre.blit(background,(292, 110))

        elif self.background_image == os.path.join('ressources', 'Theme','Haloween',  'fondPageAcceuil.png') : 
            logo =  os.path.join('ressources',  'Theme','Haloween','logoAcceuil.png')
            background = pygame.image.load(logo)
            self.fenetre.blit(background,(310, 90))

        elif self.background_image == os.path.join('ressources', 'Theme','Paques',  'fondPageAcceuil.png') : 
            logo =  os.path.join('ressources',  'Theme','Paques','logoAcceuil.png')
            background = pygame.image.load(logo)
            self.fenetre.blit(background,(310, 78))

        else :
            logo =  os.path.join('ressources', 'logo_color_addict.png')
            background = pygame.image.load(logo)
            self.fenetre.blit(background,(275, 60))
        
        
        
        
        #Boutons (Jouer, Option, Règle)
        self.boutonJouer = Bouton(300,300,300,50,(243,223,36),"Jouer",self.fenetre,30,True)
        self.boutonOption = Bouton(300,400,300,50,(243,223,36),"Options",self.fenetre,30,True)
        self.boutonRegle = Bouton(300,500,300,50,(243,223,36),"Règles",self.fenetre,30,True)
        self.boutonEnLigne = Bouton(300,600,300,50,(243,223,36),"Jouer en réseau",self.fenetre,30,True)
   
        self.boutonCroix = Boutonc(30,25,(0,0,0),self.fenetre,15)
        self.BoutonStats = Boutonc(30,75,(0,0,0),self.fenetre,15)

        pygame.display.update()
        
        
    def attendreChoix(self): 
        ''' Cette méthode attend le choix de l'utilisateur. Elle attend que l'utilisateur clique sur l'un des boutons. '''
        choixEffectue = False
        choix = ""
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boutonJouer.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Jouer"
                    elif self.boutonOption.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Option"
                    elif self.boutonRegle.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Regles"
                    elif self.BoutonStats.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Stats"
                    elif self.boutonEnLigne.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "EnLigne"
                        print("jdbvmskjvb")
                    elif self.boutonCroix.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Fermer"
    
                elif (event.type == pygame.QUIT):
                    choixEffectue = True
        
        return choix       
    