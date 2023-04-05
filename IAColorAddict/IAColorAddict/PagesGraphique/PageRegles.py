import pygame
from Boutons.Bouton import Bouton
from Autre.Texte import Texte
import os
from Autre.TexteCentrer import TexteCenter


# ---------------------------------------------------------------------------
# -- Cette page permet d'afficher les règles du Jeu.                       --
# ---------------------------------------------------------------------------


class PageRegles():
    def __init__(self, fenetre, background_image) :
        self.fenetre = fenetre
        self.background_image = background_image
        
    def afficherPageRegles(self):
        pygame.init()

        #Background
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        # Les règles lignes par lignes (seul moyen d'afficher un texte avec Pygame) 
        texteRegles = TexteCenter(self.fenetre, "Règles du Color Addict", 30, 400, 50, 400, -160, (0, 0, 0))
        Reglesintro = Texte(self.fenetre, "Le jeu Color Addict est un jeu composé de 110 cartes qui ne sont pas identiques,",11, (255, 255, 255),150, 75 )
        Reglesintro1 = Texte(self.fenetre, "il y a au moins de 2 joueurs.",11, (255, 255, 255),150, 95 )
        Reglestitre1 = Texte(self.fenetre, "But du jeu: ",11, (0, 0, 0),150, 135 )
        Regles = Texte(self.fenetre, "Les joueurs doivent déposer toutes leurs cartes au centre pour pouvoir gagner",11, (255, 255, 255),150, 150 )
        Reglestitire2 = Texte(self.fenetre, "Distribution des cartes:",11, (0, 0, 0),150, 175 )
        Reglesdistribution = Texte(self.fenetre, "Après le mélange des cartes, chaque joueur reçoit trois 3 cartes qui leur permettent de",11, (255, 255, 255),150, 195 )
        Reglesdistribution = Texte(self.fenetre, "composer leur main, puis les cartes restantes sont distribuées pour composer les pioches de chaque joueur.",11, (255, 255, 255),150, 215 )
        Reglestitre3 = Texte(self.fenetre, "Déroulement du jeu:",11, (0, 0, 0),150, 245 )
        Reglesderoulement = Texte(self.fenetre, "Lorsque vient le tour du joueur, il peut réaliser plusieurs actions en fonction des ces cartes",11, (255, 255, 255),150, 265 )
        ReglesPremiercas = Texte(self.fenetre, " premier cas le joueur peut jouer (et possède moins de 4 cartes en main):",11, (255, 255, 255),150, 285 )
        ReglesPremiercas1 = Texte(self.fenetre, " - Il pose sa carte au centre ",11, (255, 255, 255),150, 305 )
        ReglesPremiercas2 = Texte(self.fenetre, " - Il pioche une carte dans sa pioche ",11, (255, 255, 255),150, 325 )
        Reglesdeuxiemecas = Texte(self.fenetre, " - Il pioche une carte dans sa pioche.Le joueur peut jouer (et possède plus de 4 cartes en main):",11, (255, 255, 255),150, 345 )
        Reglesdeuximecas1 = Texte(self.fenetre, "    ~ Il pose sa carte au centre ",11, (255, 255, 255),150, 365 )
        Reglesdeuxiemecas2 = Texte(self.fenetre, "    ~ Il pioche une carte dans sa pioche ",11, (255, 255, 255),150, 385 )
        Reglestroisièmecas = Texte(self.fenetre, " - Il pose sa carte au centre. Il ne pioche PAS de carte Le joueur ne peut pas jouer :",11, (255, 255, 255),150, 405 )
        Reglestroisièmecas1 = Texte(self.fenetre, "    ~ Il pioche une carte  ",11, (255, 255, 255),150, 425 )
        Reglestroisièmecas2 = Texte(self.fenetre, "    ~ Il passe son tour  ",11, (255, 255, 255),150, 445 )
    
        Reglescombi1 = Texte(self.fenetre, "Combinaison 1 :",11, (35, 35, 35),150, 475 )
        Reglescombi1ex = Texte(self.fenetre, "Le mot écrit sur la carte à poser correspond avec la couleur de la carte au centre  ",11, (255, 255, 255),200, 495)
        Reglescombi2 = Texte(self.fenetre, "Combinaison 2: ",11, (35, 35, 35),150, 515 )
        Reglescombi2ex = Texte(self.fenetre, "La couleur de la carte à poser correspond avec le mot écrit de la carte au centre ",11, (255, 255, 255),200, 535)
        Reglescombi3 = Texte(self.fenetre, "Combinaison 3: ",11, (35, 35, 35),150, 555 )
        Reglescombi3ex = Texte(self.fenetre, "Le mot écrit sur la carte à poser correspond avec le mot écrit sur la carte au centre",11, (255, 255, 255),200, 575)
        Reglescombi4 = Texte(self.fenetre, "Combinaison 4: ",11, (35, 35, 35),150, 595 )
        Reglescombi4ex = Texte(self.fenetre, "La couleur de la carte à poser correspond avec celle de la carte au centre",11, (255, 255, 255),200, 615)
        Reglescombi5 = Texte(self.fenetre, "Combinaison 5: ",11, (35, 35, 35),150, 635 )
        Reglescombi5ex = Texte(self.fenetre, "Le mot écrit sur la carte à poser possède toutes les couleurs",11, (255, 255, 255),200, 655)

        # Bouton retour
        retour = os.path.join('ressources','Outils', 'retour.png')
        background = pygame.image.load(retour)
        self.boxRetour = background.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(background, self.boxRetour)

        pygame.display.update()



    def attendreChoix(self):
        ''' Méthode qui permet d'attendre si le bouton retour a été cliqué ou non'''
        choixEffectue = False
        choix = None
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
 
                elif (event.type == pygame.QUIT):
                    choixEffectue = True   

