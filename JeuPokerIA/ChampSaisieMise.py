import pygame
from Bouton import Bouton

from TexteCentrer import TexteCenter


class ChampSaisieMise():
    def __init__(self, gains: int, plusGrosseMise: int, fenetre) -> None:
        self.touchesPossibles = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]"]

        self.fenetre = fenetre
        self.miseString = ""
        self.gains = gains
        self.plusGrosseMise = plusGrosseMise
        self.boutonValider = Bouton(600,660,70,30,(243,223,36),"Valider",self.fenetre,15)
        rectContour = pygame.draw.rect(self.fenetre, (0,0,0),((600,660,70,30)), 3, 5)
        
        #rectangle
        pygame.draw.rect(self.fenetre, (243,223,36), (350, 660, 200, 30),0, 40)
        pygame.draw.rect(self.fenetre, (0,0,0),(350, 660, 200, 30), 2, 40)
        self.texteCenter = TexteCenter(fenetre, "Saisissez votre mise", 15, 30, 200, 350, 660, (0,0,0))
        
    def getMise(self):
        if (len(self.miseString) > 0):
            return int(self.miseString)
        else:
            return 0

    def verifierMiseSaisie(self):
        mise = self.getMise()                       
        return mise >= self.plusGrosseMise

    def attendreSaisieMise(self)->int:
        choixMiseEffectue = False  
        
        while choixMiseEffectue == False:
            for event in pygame.event.get():
                # On change le pointer de la souris au survol sur un bouton
                if (event.type == pygame.MOUSEMOTION):
                    positionCurseur = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boutonValider.verifier_click_bouton(positionCurseur):
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

                # Si clique sur le bouton valider
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    positionClick=pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if self.boutonValider.verifier_click_bouton(positionClick):
                        choixMiseEffectue = self.verifierMiseSaisie()
                      
                elif (event.type == pygame.KEYDOWN):
                    key = event.key
                    touche = pygame.key.name(event.key)
                    
                    mise = 0
                    if (len(self.miseString) > 0):
                        mise = int(self.miseString)
        
                    if len(self.miseString) < 100 and touche in self.touchesPossibles:
                        # Touche du pavé numérique
                        if (len(touche) > 1):
                            touche = touche[1]

                        nouvelleMise = self.miseString + touche
                        if int(nouvelleMise) <= self.gains: 
                            self.miseString = nouvelleMise
                            self.texteCenter.modifierText(self.miseString) 
                    elif key == pygame.K_BACKSPACE:
                        self.miseString = self.miseString[:-1]
                        self.texteCenter.modifierText(self.miseString)
                    elif key ==  pygame.K_RETURN:   # Appui sur la touche entrée
                        choixMiseEffectue = self.verifierMiseSaisie()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                            
        return self.getMise()