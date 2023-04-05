import pygame
from Boutons.Bouton import Bouton
import os
from Autre.Texte import Texte
from Autre.TexteCentrer import TexteCenter


# ---------------------------------------------------------------------------
# -- Cette classe permet d'afficher une fenêtre qui contient les mentions  --
# -- légales.                                                              --
# ---------------------------------------------------------------------------




class PageMentionLegale():
    def __init__(self, fenetre, background_image) :
        self.fenetre = fenetre
        self.background_image = background_image
        
    def afficherPageMention(self):
        pygame.init()

        #BackgroUnd
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))

        # Les règles lignes par lignes (seul moyen d'afficher un texte avec Pygame) 
        MentionLegale = TexteCenter(self.fenetre, "Mentions légales", 30, 400, 75, 400, -110, (0, 0, 0))
        Intro = Texte(self.fenetre, "Conformément aux dispositions de la loi n°2004 575 du 21 juin 2004 pour la",12, (255, 255, 255),200, 150 )
        Intro1 = Texte(self.fenetre, "confiance en économie numérique, il est précisé aux utilisateurs de",12, (255, 255, 255),200, 170 )
        Intro2 = Texte(self.fenetre, "l'application 'Jeu Color Addict' l'identité des différents intervenants dans",12, (255, 255, 255),200, 190 )
        Intro3 = Texte(self.fenetre, "le cadre de sa réalisation et de son suivi",12, (255, 255, 255),200, 210 )
        Edition = Texte(self.fenetre, "Edition du projet",12, (20, 20, 20),200, 280 )
        
        Bacquet = Texte(self.fenetre, "Bacquet Antoine : Chef de Projet",12, (255, 255, 255),200, 300 )
        Langrez = Texte(self.fenetre, "Langrez Marine : Programmeuse",12, (255, 255, 255),200, 320 )
        Le_Fur = Texte(self.fenetre, "Le Fur Lucie : Programmeuse",12, (255, 255, 255),200, 340 )
        Bernard = Texte(self.fenetre, "Bernard Laetitia : chargée de communication",12, (255, 255, 255),200, 360 )
        Duvieubourg = Texte(self.fenetre, "Duvieubourg Clément : Programmeur",12, (255, 255, 255),200, 380 )
        
        Sources = Texte(self.fenetre, "Sources",12, (20, 20, 20),200, 450 )
        github = Texte(self.fenetre, "Carte : github ",12, (255, 255, 255),200, 470 )
        avatar = Texte(self.fenetre, "Avatar et logo : flaticon ",12, (255, 255, 255),200, 490 )
        fond = Texte(self.fenetre, "Fond : dreamstime",12, (255, 255, 255),200, 510 )

        NousContacter = Texte(self.fenetre, "Données personnelles",12, (20, 20, 20),200, 580 )
        donnees = Texte(self.fenetre, "Aucun traitement de données personnelles n'est effectué au sein de l'application",12, (255, 255, 255),200, 600 )
        donnnes1 = Texte(self.fenetre, "puisque aucune donnée n'est stockée. Le RGPD n'entre pas en vigueur dans ce cas.",12, (255, 255, 255),200, 620 )

    
        

        # bouton retour
        retour = os.path.join('ressources','Outils', 'retour.png')
        background = pygame.image.load(retour)
        self.boxRetour = background.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(background, self.boxRetour)

        pygame.display.update()

        # bouton acceuil
        Acceuil = os.path.join('ressources','Outils', 'maison.png')
        background = pygame.image.load(Acceuil)
        self.boxAcceuil = background.get_rect()
        self.boxAcceuil.x = 700
        self.boxAcceuil.y = 10       
        self.fenetre.blit(background, self.boxAcceuil)

        pygame.display.update()




    def attendreChoix(self):
        ''' Méthode qui permet d'attendre que l'on clique soit sur le bouton retour ou le bouton accueil'''
        choixEffectue = False
        choix = None
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
                    if self.boxAcceuil.colliderect(positionClick):
                        choixEffectue = True
                        choix = "Acceuil"
                        
                elif (event.type == pygame.QUIT):
                    choixEffectue = True   

        return choix
    
