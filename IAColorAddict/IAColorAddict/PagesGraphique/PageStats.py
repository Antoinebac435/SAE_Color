import pygame
import psycopg2
from Boutons.Bouton import Bouton
from Autre.Texte import Texte
import os
from Autre.TexteCentrer import TexteCenter




class PageStats():
    def __init__(self, fenetre, background_image) -> None:
        self.fenetre = fenetre
        self.background_image = background_image
        self.icone = pygame.image.load("./ressources/icone/bored.png")
        self.icone2 = pygame.image.load("./ressources/icone/loser.png")
        self.icone3 = pygame.image.load("./ressources/icone/mvp.png")
        self.icone4 = pygame.image.load("./ressources/icone/trophy.png")
       
        
    def select_joueurs(self):
        conn = psycopg2.connect(database="SAEcolor", user="antoinebac", password="bacquet", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM joueur")
        rows = cursor.fetchall()
        
        return rows
   
    def select_partie(self):
        conn = psycopg2.connect(database="SAEcolor", user="antoinebac", password="bacquet", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM partie")
        rows = cursor.fetchall()
        
        return rows
    
    def select_maxjoueurs(self):
        conn = psycopg2.connect(database="SAEcolor", user="antoinebac", password="bacquet", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM joueur ORDER BY nb_partie DESC LIMIT 1")
        rows = cursor.fetchall()
        
        return rows
    
    def select_maxvictoire(self):
        conn = psycopg2.connect(database="SAEcolor", user="antoinebac", password="bacquet", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM partie ORDER BY victoire DESC LIMIT 1")
        rows = cursor.fetchall()
        
        return rows
    
    def select_minjoueurs(self):
        conn = psycopg2.connect(database="SAEcolor", user="antoinebac", password="bacquet", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM joueur ORDER BY nb_partie ASC LIMIT 1")
        rows = cursor.fetchall()
        
        return rows
    
    def select_minvictoire(self):
        conn = psycopg2.connect(database="SAEcolor", user="antoinebac", password="bacquet", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM partie ORDER BY victoire ASC LIMIT 1")
        rows = cursor.fetchall()
        
        return rows
    
   
        
    def afficherPageStats(self):
        pygame.init()

        #Backgrond
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))
        texteRegles = TexteCenter(self.fenetre, 'Statistique des Parties', 30, 400, 75, 400, -160, (255, 255, 255))
        
        
        # joueurs = self.select_joueurs()
        # y = 50
       
        # for joueur in joueurs:
        #     nom_joueur = joueur[1]
        #     nb_partie = joueur[2]
        #     texte = f"{nom_joueur}: {nb_partie} parties"
        #     self.texte = Texte(self.fenetre, texte, 30, 400, y, 200)
        #     y += 250
            
        max_joueur = self.select_maxjoueurs()
        
        
        for joueur in max_joueur:
            nom_joueur = joueur[1]
            nb_partie = joueur[2]
            texte = f"Le joueur {nom_joueur} a joué le plus de parties avec {nb_partie} parties"
            self.texte = Texte(self.fenetre, texte, 22, (255, 255, 255) , 95, 200)
        
        max_victoire = self.select_maxvictoire()
        
        for victoire in max_victoire:
            nom_joueur = victoire[1]
            victoire = victoire[2]
            texte = f"Le joueur {victoire} a gagné le plus de parties avec {nom_joueur} victoires"
            self.texte = Texte(self.fenetre, texte, 22, (255, 255, 255),  95, 300) 
            
        min_joueur = self.select_minjoueurs()
        
        for joueur in min_joueur:
            nom_joueur = joueur[1]
            nb_partie = joueur[2]
            texte = f"Le joueur {nom_joueur} a joué le moins de parties avec {nb_partie} parties"
            self.texte = Texte(self.fenetre, texte, 22, (255, 255, 255) , 95, 400)
            
            
        min_victoire = self.select_minvictoire()
        
        for victoire in min_victoire:
            nom_joueur = victoire[1]
            victoire = victoire[2]
            texte = f"Le joueur {victoire} a gagné le moins de parties avec {nom_joueur} victoires"
            self.texte = Texte(self.fenetre, texte, 22, (255, 255, 255) , 95, 500)
            
        
        
   
        
        retour = os.path.join('ressources','Outils', 'retour.png')
        background = pygame.image.load(retour)
        self.boxRetour = background.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(background, self.boxRetour)
        self.fenetre.blit(self.icone,  (20, 385)) 
        self.fenetre.blit(self.icone2, (20, 485))
        self.fenetre.blit(self.icone3, (20, 185))
        self.fenetre.blit(self.icone4, (20, 285))
        
    
    
        pygame.display.flip()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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