import pygame
from Boutons.Bouton import Bouton
from Boutons.BoutonListe import BoutonListe
from Autre.Texte import Texte
from PagesGraphique.PageMentionLegale import PageMentionLegale

from Autre.TexteCentrer import TexteCenter
import os

# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher la fenêtre des options. Cette fenêtre  --
# -- permet de couper ou non le son. De baisser le volume, et de changer   --
# -- le thème                                                              --
# ---------------------------------------------------------------------------


class PageOption():
    def __init__(self, fenetre, musique, background_image) :
        
        self.musique = musique
        self.fenetre = fenetre
        self.background_image = background_image
        self.nombreJoueurs = 0
        self.typePartie = None
        self.listeVolume = ["1","2","3","4","5","6","7","8","10"]
        self.listeTheme = ["Defaut", "Haloween", "Noel", "Paques"]
        self.choixTheme = ""
        
        

    def afficherPageOption(self):
        pygame.init()

        #Background
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        #Texte Option 
        texteOption = TexteCenter(self.fenetre, "Options", 50, 400, 100, 400, -120, (255, 255, 255))
        
        # Musique
        Texte(self.fenetre,"Réglage son", 30, (255,255,255), 150, 155)
        Texte(self.fenetre,"Couper le son ", 20,(255,255,255), 150, 220)
        
        # Icone du bouton son
        boutonSon = os.path.join('ressources','Outils', 'son.png')
        background = pygame.image.load(boutonSon)
        self.boxSon = background.get_rect()
        self.boxSon.x = 320
        self.boxSon.y = 215      
        self.fenetre.blit(background, self.boxSon)
        self.son = 1
        
        
        # Zone pour augmenter ou baisser le son
        Texte(self.fenetre,"Changer le volume", 20,(255,255,255), 150, 260)
        self.volume = BoutonListe("",17,self.listeVolume,450, 240, 300, 50,(243,223,36),self.fenetre)

        # Zone pour changer le thème
        Texte(self.fenetre,"Theme", 30, (255,255,255), 150, 355)
        Texte(self.fenetre,"Choix du thème", 20, (255,255,255), 150, 400)
        self.theme = BoutonListe("",17,self.listeTheme,450, 380, 300, 50,(243,223,36),self.fenetre)
        
        # bouton mention légale
        self.mentionlegale = Bouton(40,600,200,50,(243,223,36),"Mentions légales",self.fenetre,18)
        
        # bouton retour
        retour = os.path.join('ressources','Outils', 'retour.png')
        background = pygame.image.load(retour)
        self.boxRetour = background.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(background, self.boxRetour)

        pygame.display.update()

    
    
    
    
    def ajoutSon(self):
        pygame.draw.rect(self.fenetre, (236,149,104),(150, 220,150, 30),0,5)
        pygame.draw.rect(self.fenetre, (236,149,104),(320, 215,50, 50),0,5)

        if self.son > 0 :

            Texte(self.fenetre,"Ajouter le son ", 20,(255,255,255), 150, 220)
            self.son = 0
            nomSon = "sonCoupe"
            self.musique.pause()
            
        else :

            Texte(self.fenetre,"Couper le son ", 20,(255,255,255), 150, 220)
            self.musique.unpause()
            self.son = 1
            nomSon = "son"
            
        boutonSon = os.path.join('ressources','Outils', nomSon+".png")
        background = pygame.image.load(boutonSon)
        self.boxSon = background.get_rect()
        self.boxSon.x = 320
        self.boxSon.y = 215      
        self.fenetre.blit(background, self.boxSon)
        pygame.display.update()
        
        
        
        
        
    def modifierVolume(self):
        self.musique.set_volume(float(self.volume.getChoix())/10)
        
        
        
        
        
    def changerFond(self):
        return self.theme.getChoix() 


            
            
            
    def attendreChoix(self):
        choixEffectue = False
        choix = None
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    self.theme.verifierClickDeplacement(positionClick)
                    self.choixTheme = self.theme.getChoix()
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
                    
                    if self.boxSon.colliderect(positionClick):
                        self.ajoutSon()
                        
                    if self.volume.verifierClickDeplacement(positionClick)==True:
                        self.modifierVolume()

                    if self.mentionlegale.verifier_click_bouton(positionClick) == True:
                        choixEffectue = True
                        choix = "MentionLegale"
                        
                elif (event.type == pygame.QUIT):
                    choixEffectue = True  

        return choix 
