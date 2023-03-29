from os import listdir
import pygame
from Bouton import Bouton

from BoutonListe import BoutonListe
from BoutonImageListe import BoutonImageListe
from ChampSaisie import ChampSaisie



class PageChoixJouer():
    
    def __init__(self, fenetre : pygame.display, background_image) -> None:
        self.fenetre = fenetre
        self.listeOrdre = ["Aléatoire","Dans l'ordre"]
        self.listeNbJoueur = ["2","3","4"]
        self.listeGains = ["100","1000","10000", "100000"]
        self.listetypeJoueur = ["Humain","Robot"]
        self.listeniveau = ["facile","difficile"]
        self.ImagesAvatar = listdir("./images/Avatar")
        self.joueur = 1
        self.listeJoueurs = []
        self.background_image = background_image
        self.gainsJoueurs = 0        
        self.nombreJoueurs = 0
        self.typePartie = None
        self.typejoueur = ""
        self.niveauIA = " "
        self.champListBot = BoutonListe("AI" ,25,self.listetypeJoueur,280,400,350,45,(243,223,36),self.fenetre) 
        # self.champniveau = BoutonListe("Difficulte" ,25,self.listeniveau,280,520,350,45,(243,223,36),self.fenetre)
            
        
    def afficherPageChoixJouer(self, estJoueur1 = True):
        pygame.init()

        #Backgrond
        background = pygame.image.load(self.background_image).convert()
        self.fenetre.blit(background,(0, 0))

        if (estJoueur1):
            # Nb Joueur 
            self.champListNbJoueurs = BoutonListe("Nombre de joueurs",25,self.listeNbJoueur,280,80,350,45,(243,223,36),self.fenetre)
            # Ordre Joueur
            self.champListOrdreJoueurs = BoutonListe("Ordre des joueurs",25,self.listeOrdre,280,200,350,45,(243,223,36),self.fenetre)
            # Choix du gain
            self.champListeGains = BoutonListe("Mise des joueurs",25,self.listeGains,280,320,350,45,(243,223,36),self.fenetre)
            # self.champListBot : BoutonListe
            positionYAvatar = 490
            self.champSaisieNom = ChampSaisie(280, positionYAvatar + 100,350,45,(243,223,36),self.fenetre)

        else:            
            self.champListeGains = None
            positionYAvatar = 200
            self.champListBot = BoutonListe("AI" ,25,self.listetypeJoueur,280,400,350,45,(243,223,36),self.fenetre) 
            if (self.champListBot.getChoix() == "Humain"):       
                self.champSaisieNom = ChampSaisie(280, positionYAvatar + 100,350,45,(243,223,36),self.fenetre)
            if (self.champListBot.getChoix() == "Robot"):
                self.champniveau = BoutonListe("Difficulte" ,25,self.listeniveau, 280 , 520,350,45,(243,223,36),self.fenetre)

            

        # Choix image avatar
        self.champListAvatars = BoutonImageListe("Joueur "+ str(self.joueur),self.ImagesAvatar,280,positionYAvatar,350,45,(243,223,36),self.fenetre)

        # bouton valider
        self.boutonValider = Bouton(720,620,120,50,(243,223,36),"Valider",self.fenetre,18)
        rectContour = pygame.draw.rect(self.fenetre, (0,0,0),(720,620,120,50), 3, 5)
        
        # bouton retour
        retour = "./images/Outils/retour.png"
        retourImage = pygame.image.load(retour)
        self.boxRetour = retourImage.get_rect()
        self.boxRetour.x = 10
        self.boxRetour.y = 10       
        self.fenetre.blit(retourImage, self.boxRetour)
    
        pygame.display.update()
        
    def ajoutBot(self):
        self.champniveau = BoutonListe("Difficulte" ,25,self.listeniveau, 280 , 520,350,45,(243,223,36),self.fenetre)
        
    
    def verifierValider(self, positionClick)->bool:
        if (self.joueur == 1):
            self.nombreJoueurs = self.champListNbJoueurs.getChoix()
            self.typePartie = self.champListOrdreJoueurs.getChoix()
            # self.typejoueur = self.champListBot.getChoix()
        if (self.joueur != 1):
            self.typejoueur = self.champListBot.getChoix()
            print(self.typejoueur)

        clickBouton: bool = self.boutonValider.verifier_click_bouton(positionClick)

        if (self.boutonValider.verifier_click_bouton(positionClick) and self.joueur <= int(self.champListNbJoueurs.getChoix()) ):
            # On va récupérer avant de supprimer le champ gain, la valeur des gains

            if (self.champListeGains != None):
                self.gainsJoueurs = int(self.champListeGains.getChoix())
            
            # print()
            # récupérer la valeur du type de joueur
            self.typejoueur = str(self.champListBot.getChoix())

            # récupérer la valeur du type de joueur
            if (self.typejoueur == "Humain"):
                self.niveauIA = None
                # Si pas de nom, on va en mettre un par défaut
                nomJoueur = self.champSaisieNom.getTexte()
                if (nomJoueur == ""):
                    nomJoueur = "Joueur {0}".format(self.joueur)
                # self.champniveau = None
            else:
                self.niveauIA = str(self.champniveau.getChoix())
                nomJoueur = self.champSaisieNom.getTexte()
                if (nomJoueur == ""):
                    nomJoueur = "IA {0}".format(self.joueur)

            infosJoueur = {"nomJoueur": nomJoueur,
                           "avatar": self.champListAvatars.getImageAvatar(),
                           "gainsJoueur": self.gainsJoueurs,
                           "typeJoueur" : self.typejoueur,
                           "niveauIA" : self.niveauIA}
   
            print(infosJoueur)         
            self.listeJoueurs.append(infosJoueur)
            self.joueur += 1
            self.afficherPageChoixJouer(False)    
            
        return clickBouton
    
    def getListeJoueurs(self):
        return self.listeJoueurs

    def attendreChoix(self)->dict:
        choixEffectue = False
        choix = None
        while choixEffectue == False:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEMOTION):
                    positionCurseur = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if (self.champListeGains != None and self.champListeGains.verifierPositionSurBoutonFleche(positionCurseur))  or self.boutonValider.verifier_click_bouton(positionCurseur) or self.boxRetour.colliderect(positionCurseur) or self.champListAvatars.verifierPositionSurBoutonFleche(positionCurseur) or self.champListNbJoueurs.verifierPositionSurBoutonFleche(positionCurseur) or self.champListOrdreJoueurs.verifierPositionSurBoutonFleche(positionCurseur) :
                        
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boxRetour.colliderect(positionClick):
                        choixEffectue = True
                    self.champListAvatars.verifierClickDeplacement(positionClick)
                    self.champListNbJoueurs.verifierClickDeplacement(positionClick)
                    self.champListOrdreJoueurs.verifierClickDeplacement(positionClick)
                    self.champListBot.verifierClickDeplacement(positionClick)
                    # self.champniveau.verifierClickDeplacement(positionClick)
                    # self.ajoutBot()
    
                    print("bot est : ",self.champListBot.getChoix())
                    if (self.champListeGains != None):
                        self.champListeGains.verifierClickDeplacement(positionClick)
                        self.champListNbJoueurs.verifierClickDeplacement(positionClick)
                    
                    if (self.champListBot.getChoix() == "Robot"):
                        self.ajoutBot()
                        self.champniveau.verifierClickDeplacement(positionClick)
                        print("niveau est : ", self.champniveau.getChoix())
                        # self.champniveau.verifierClickDeplacement(positionClick)
                        # self.champListBot.verifierClickDeplacement(positionClick)
                        
                        

                    # if (self.champListBot.getChoix() == "Humain"):
                    #     self.champniveau = None
                        
                        
                    self.verifierValider(positionClick)
                    
                    # Si on a validé et on a tous les joueurs
                    if self.joueur == int(self.champListNbJoueurs.getChoix()) + 1:
                        choix = "Partie"
                        choixEffectue = True
                    
                elif (event.type == pygame.KEYDOWN):
                    self.champSaisieNom.verifierSaisie(event.key)    
                elif (event.type == pygame.QUIT):
                    choixEffectue = True   
        
        return choix       