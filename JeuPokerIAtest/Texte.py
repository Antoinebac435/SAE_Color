import pygame


class Texte():
    def __init__(self, fenetre, texte :str, taillepolice : int, couleur, x : int, y : int) -> None:
        self.fenetre = fenetre
        self.police = pygame.font.Font("policeEcriture/Grandstander-clean.ttf", taillepolice)
        texteRendu = self.police.render(texte, True, couleur)
        self.fenetre.blit(texteRendu, (x, y)) 