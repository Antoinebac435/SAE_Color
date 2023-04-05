import pygame
import os



from Boutons.Bouton import Bouton
from Boutons.Boutoncercle import Boutonc





class PageReseau():
    def __init__(self, fenetre, background_image) :
        pygame.init()
        
        #Fenetre
        self.fenetre = fenetre
        self.background_image = background_image

    

    
    def afficherPageReseau(self):
        # -- 
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        retour = os.path.join('ressources', 'Outils', 'retour.png')

        retourImage = pygame.image.load(retour)
        self.boxRetour = retourImage.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(retourImage, self.boxRetour)
        
        
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
        self.boutonCreer = Bouton(265,300,370,50,(243,223,36),"Créer une partie",self.fenetre,30,True)
        self.boutonRejoindre = Bouton(265,400,370,50,(243,223,36),"Rejoindre une partie",self.fenetre,30,True)
        self.boutonCroix = Boutonc(30,25,(0,0,0),self.fenetre,15)

        pygame.display.update()
        
        
        
        
    def attendreChoix(self): 
        ''' Cette méthode attend le choix de l'utilisateur. Elle attend que l'utilisateur clique sur l'un des boutons. '''
        choixEffectue = False
        choix = ""
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
                    if self.boutonCreer.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Creer"
                    elif self.boutonRejoindre.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Rejoindre"
                        
                    elif self.boutonCroix.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "Fermer"
    
                elif (event.type == pygame.QUIT):
                    choixEffectue = True
        
        return choix       
    
    