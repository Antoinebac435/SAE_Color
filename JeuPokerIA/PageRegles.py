import pygame
from Bouton import Bouton
from Texte import Texte

from TexteCentrer import TexteCenter

class PageRegles():
    def __init__(self, fenetre, background_image) -> None:
        self.fenetre = fenetre
        self.background_image = background_image
        
    def afficherPageRegles(self):
        pygame.init()

        #Backgrond
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        
        #texte Option 
        texteRegles = TexteCenter(self.fenetre, "Règles du Poker", 30, 400, 75, 400, -160, (255, 255, 255))
        Reglesintro = Texte(self.fenetre, "Le jeu Poker est un jeu composé de 52 cartes qui ne sont pas identiques, qui se joue ",16, (255, 255, 255),100, 75 )
        Reglesintro1 = Texte(self.fenetre, "avec 2 joueurs minimum. Un jeu de stratégie et de combinaison de cartes.",16, (255, 255, 255),110, 100 )

        Regles = Texte(self.fenetre, "Le joueur doit rassembler dans ses gains tous les jetons du jeu Après le mélange ",16, (255, 255, 255),150, 140 )

        Reglesdistribution = Texte(self.fenetre, "des cartes, chaque joueur reçoit 2 cartes qui leur permettent de composer",16, (255, 255, 255),150, 165 )
        Reglesdistribution1 = Texte(self.fenetre, "leur main, puis les autres cartes constituent la pioche. Ainsi le premier",16, (255, 255, 255),150, 190 )
        Reglesdistribution2 = Texte(self.fenetre, " joueur mise la grosse blinde, suivi du joueur suivant avec la petite blinde.",16, (255, 255, 255),150, 215 )

        ReglesTours1cas = Texte(self.fenetre, "Lors du premier tours, le joueur peux alors miser ou se coucher,tant que la dernière ",16, (255, 255, 255),125, 255 )
        ReglesTours1cas1 = Texte(self.fenetre, "mise n'est pas égale pour chacun des joueurs encore en jeu, alors c'est aux tours du  ",16, (255, 255, 255),100, 280 )
        ReglesTours1cas2 = Texte(self.fenetre, "joueur suivant. A la fin du tours, une carte de la pioche est enlevée et trois autres sont ",16, (255, 255, 255),85, 305 )
        ReglesTours1cas3 = Texte(self.fenetre, "disposées au centre de la table de jeu. Le deuxième tour commence, chaque joueur peut alors :",16, (255, 255, 255),75, 330 )
        ReglesTours2cas = Texte(self.fenetre, " check, miser ou se coucher.",16, (255, 255, 255),100, 355 )
        ReglesTours2cas2 = Texte(self.fenetre, "Une carte est enlevée et une autre au centre de la table.Le troisième tours.",16, (255, 255, 255),75, 380 )
        ReglesTours2cas2 = Texte(self.fenetre, "est identique au deuxième.",16, (255, 255, 255),75, 405 )

        ReglesFin1 = Texte(self.fenetre, "Les joueurs qui ne sont pas couchés peuvent alors analyser leurs cartes et ",16, (255, 255, 255),50, 445 )
        ReglesFin1 = Texte(self.fenetre, "les cartes au milieu de la table de jeu, pour ainsi dévoiler ses combinaisons.",16, (255, 255, 255),50, 470 )
        ReglesFin2 = Texte(self.fenetre, " C'est le joueur qui possède la plus grosse combinaison qui gagne tout les jetons misés ",16, (255, 255, 255),50, 495 )
        ReglesFin2 = Texte(self.fenetre, "pendant la partie. Une autre partie peut alors avoir lieu.",16, (255, 255, 255),75, 520 )
        ReglesFin3 = Texte(self.fenetre, " Le poker se termine lorsqu'un joueur possède tout les jetons du jeu.",16, (255, 255, 255),50, 545 )
        ReglesFin3 = Texte(self.fenetre, "Les combinaisons dans l’ordre croissant (de la plus petite à la plus grosse):",16, (255, 255, 255),50, 570 )
        ReglesFin4 = Texte(self.fenetre, "- la paire / la double paire / le brelan ",16, (255, 255, 255),125, 595 )
        ReglesFin4 = Texte(self.fenetre, "- la suite / la couleur / le full ",16, (255, 255, 255),125, 620 )
        ReglesFin4 = Texte(self.fenetre, "- le carre / la quinte flush / la quinte flush royale",16, (255, 255, 255),125, 645 )
        # bouton retour
        retour = "./images/Outils/retour.png"
        background = pygame.image.load(retour)
        self.boxRetour = background.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(background, self.boxRetour)

        pygame.display.update()

    def attendreChoix(self):
        choixEffectue = False
        choix = None
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEMOTION):
                    positionCurseur = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    # on affiche un pointer de souris au survol sur le bouton retour
                    if self.boxRetour.colliderect(positionCurseur):
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))  

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
                        
                elif (event.type == pygame.QUIT):
                    choixEffectue = True   

