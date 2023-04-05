from Jeu.Jeu import Jeu
from Jeu.JeuCartes import JeuCartes
from Jeu.Joueur import Joueur
from Jeu.Carte import Carte





# --------------------------------------------------------------------------
# -- Ce programme permet de lancer de jeu sur une console TERMINALE       --
# -- RIEN de graphique.                                                   --
# --------------------------------------------------------------------------




print("--------------------------")
print("| Lancement de la partie |")
print("--------------------------")

Correct = False 
nombreJoueur = 0 
nomJoueurs : list[Joueur]= []


# Test si le nombre de Joueur est correct ou pas 
while Correct == False : 
    nombreJoueur = int(input("Combien y'a-t-il de joueurs ? "))
    if (nombreJoueur >= 2 and nombreJoueur <5): 
        Correct = True 
    else : 
        print("Le nombre de joueurs demandé n'est pas correct")


# Test si le nom des Joueurs est correct ou pas 
for i in range(0, nombreJoueur) :
    # nom = input("Comment voulez-vous appeler le joueur "  + str(i) +  " : ")
    
    NomCorrect = False
    while NomCorrect == False:  
        nom = input("Comment voulez-vous appeler le joueur "  + str(i) +  " : ")

        correct = True 
        for lettre in range(len(nom)) :
            if (nom[lettre].isdigit() == True) or (nom.isspace() == True) : 
                correct = False
         
        if correct == True : 
            NomCorrect = True 
            LeJoueur : Joueur = Joueur(nom.capitalize())
            nomJoueurs.append(LeJoueur) 
        else : 
            # nom = input("Comment voulez-vous appeler le joueur "  + str(i) +  " : ")
            print('Nom incorrect (le nom ne doit pas contenir de chiffre ou de caractères spéciaux)')
    

   
    

jeu : Jeu = Jeu(nomJoueurs)

    



victoire = False 
# ----------------------------------------------

while (victoire== False):
    print('--------------------------------------------------------------------------')
    
    if jeu.victoireJoueur() == True : 
        victoire = True
    
    JeuJoueur : list[Carte] = jeu.getJoueurCourant().getMainJoueur()
    print('Il vous reste : ', len(jeu.tabCartesJoueurs[0]))
    
    print("\n")

    print("--------------------------------")
    print("| Au tour de : " + jeu.getJoueurCourant().getNom() )
    print("--------------------------------")

    print("\n")

    print("---------------------")
    print("| Cartes de "+ jeu.getJoueurCourant().getNom()  )
    print("---------------------")  
    jeu.getJoueurCourant().afficherMain()
    print("\n")

    
    print("La carte au centre est : " + jeu.carteAuCentre.AfficheCarte() + "\n")
    print("---------------------")
    print("| Choix de la carte | ")
    print("---------------------")

    
    print("C'est le moment de choisir la carte que vous souhaitez jouer",jeu.getJoueurCourant().getNom())
    
    bonneCarte = False
    while bonneCarte == False:
        print('\n')
        carte_couleur : str = str(input("Quelle est la couleur de la carte ?    (Exemple : Carte ... de type rouge)" + "\n"))
        carte_type : str = str(input("Quelle est le type de la carte ?     (Exemple : Carte rouge de type ...)"  + "\n"))
        
        cartaAjouer = Carte(carte_couleur, carte_type)
        
        print("\n")
        print("La carte que vous voulez jouer est : " + cartaAjouer.AfficheCarte())
        
        if jeu.estJouable(cartaAjouer):
            jeu.jouerCarte(cartaAjouer)
            bonneCarte = True
        else :
            print("Vous ne pouvez pas jouer cette carte")            
            reponse : str = str(input(jeu.getJoueurCourant().getNom() + " veux-tu piocher une carte ? (oui/non) "))
            
            if reponse == 'oui' : 
                jeu.getJoueurCourant().piocherCarte()
                bonneCarte = True
                
                
                
            
    jeu.changementDeJoueur()
    