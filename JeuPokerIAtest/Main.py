# from Jeu import Jeu
from JeuCartes import JeuCartes
from Joueur import Joueur
from Carte import Carte
from typing import List

Joueur1 : Joueur = Joueur('Lucie')
Joueur2 : Joueur = Joueur('GrosseTchouin')

jeu : Jeu = Jeu([Joueur1,Joueur2])

# ch_tour = jeu.changement_tour()
# print(ch_tour)
pioche = jeu.pioche_carte()
# print(pioche)

gains : int = int (input("Quelle est la mise de départ pour tout le monde :"))
# gainsjoueurs : int = jeu.getJoueurCourant().setGains(gains)
# print(gainsjoueurs)

# for i in range (len(jeu.listJoueur)):
#     gainsjoueurs : int = Joueur.setGains(gains)
# print(gainsjoueurs)


victoire = False 


# ----------------------------------------------

while (victoire== False):
    
    if jeu.victoireJoueur() == True: 
        victoire = True
    # for i in range (0,2):
    # Joueurcourant : list[Carte] = JeuCartes.distribuerJeu(jeu)
    ## La main du joueur 
    JeuJoueur : List[Carte] = jeu.getJoueurCourant().getMainJoueur()
   
      
    
    print("\n")

    print("------------------------------------------------------------")
    print("| Au tour de : " + jeu.getJoueurCourant().getNom())
    print("------------------------------------------------------------")

    print("\n")

    # print(jeu.carteAuCentre.getValeur())

    print(jeu.getJoueurCourant().getNom(), "vos cartes sont : ")
    
    #  problème le joueur n'as pas de main
    jeu.getJoueurCourant().afficherMain()
    variable = jeu.getJoueurCourant().getMainJoueur()

    if (jeu.changement_tour() == 1):
        for i in range (0,3):
            print("Cartes au centre sont :" +jeu.carteAuCentre.AfficheCarte())
          
    elif (jeu.changement_tour() == 2 or jeu.changement_tour() == 3):
        for y in range (0,2):
            jeu.carteAuCentre.AfficheCarte()
  

    bonneCarte = False
    while bonneCarte == False:

        demander_pb = False
        demander_gb = False

        if (demander_pb == False):
            if (jeu.getJoueurCourant() == 0):
                jeu.petite_blind()
                demander_pb = True

        if (demander_gb == False):
            if (jeu.getJoueurCourant() == 1):
                jeu.grande_blind()
                demander_gb = True
       
        print("\n")
        optionpossible : str = str(input( "Vous pouvez choisir entre Coucher, Miser, Doubler : " + "\n" ))
        jeu.option(optionpossible)
        if (optionpossible == "Coucher") :
            #  si coucher alors supprimer joueur de la liste
            jeu.getJoueurCourant().pop()
        else:
            jeu.changementDeJoueur()
            
        
        carte_valeur : str = str(input(jeu.getJoueurCourant().getNom()+ ", choisi ta carte (donne sa couleur)  " + "\n"))
        carte_familles : str = str(input(jeu.getJoueurCourant().getNom() + ", choisi ta carte (donne son type)"   + "\n"))
        
        cartaAjouer = Carte(carte_valeur, carte_familles)
        
        
        
        if jeu.estJouable(cartaAjouer):
            jeu.jouerCarte(cartaAjouer)
            # jeu.retirerCarte(cartaAjouer)
            bonneCarte = True
        else :
            print("Vous ne pouvez pas jouer cette carte")
            
    
    