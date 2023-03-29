import pygame


class TexteCenter():
    def __init__(self, fenetre, texte : str , taillePolice : int, hauteur : int , largeur, x: int , y : int, couleur ) -> None:

        self.fenetre = fenetre
        self.texte = texte
        self.couleur = couleur
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = x
        self.y = y
                
        self.police = pygame.font.Font("policeEcriture/Grandstander-clean.ttf", taillePolice)
        self.afficherTexte()
        
    def modifierText(self, texte: str):
        # Effacer zone de texte (dans le cas où y a déjà du texte)
        pygame.draw.rect(self.fenetre, (243,223,36), self.positionSave)   

        self.texte = texte
        self.afficherTexte()
        
    def afficherTexte(self):
        texteRendu = self.police.render(self.texte, True, self.couleur)
        posTexte = texteRendu.get_rect()
        margeGauche = (self.largeur - posTexte.width) / 2
        margeHauteur = (self.hauteur - posTexte.height) / 2

        self.fenetre.blit(texteRendu, (self.x + margeGauche, self.y + margeHauteur)) 
        
        self.positionSave = posTexte
        self.positionSave.x = self.x + margeGauche 
        self.positionSave.y = self.y + margeHauteur
        
        pygame.display.update()       
