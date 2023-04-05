import socket
import json

from PagesGraphique.PageJoueurAttenteEnLigne import PageAttenteJoueurEnLigne

class GestionPartieReseau() :
    def __init__(self, pageAttenteJoueur: PageAttenteJoueurEnLigne, port = 15555):
        self.port = port
        self.pageAttenteJoueur = pageAttenteJoueur
        self.infosPartie = None
        self.socketsClient = []
        self.adressesIpClient = []
        self.listeJoueursEnLigne = []
                
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def creerServeur(self):
        self.socket.bind(('', self.port))
        
    def connecterServeur(self, infosJoueurs: dict, adresseIpServeur = "127.0.0.1"):
        
        while self.infosPartie == None or self.listeJoueursEnLigne < self.infosPartie["nbJoueur"]:
            self.adresseIpServeur = adresseIpServeur
            self.socket.connect((adresseIpServeur, self.port))
            # On envoie les informations du joueur au serveur
            encode_infosJoueurs = json.dumps(infosJoueurs).encode('utf-8')
            self.socket.sendall(encode_infosJoueurs)
        
            # Attente liste joueurs
            tmp = self.socket.recv(1024)
            listeInfos = json.loads(tmp.decode('utf-8'))
            self.infosPartie = listeInfos[0]
            self.listeJoueursEnLigne = listeInfos[1:]
            print("infosPartie", self.infosPartie)
            print("listeJoueurs", self.listeJoueurs)
            self.pageAttenteJoueur.afficherPageJoueurEnAttente(self.infosPartie, self.listeJoueurs)

    def attendreJoueursClient(self, infosPartie: dict, infosJoueur: dict):
        self.infosPartie = infosPartie
        print("Attendre joueur !")
        self.listeJoueursEnLigne.append(infosJoueur)
        self.pageAttenteJoueur.afficherPageJoueurEnAttente(infosPartie, self.listeJoueursEnLigne)        
        
        indiceJoueur = 1
        nombreJoueurs = infosPartie["nbJoueur"]
        while indiceJoueur < nombreJoueurs:
            self.socket.listen(nombreJoueurs - 1)
            
            # On attend qu'un joueur se connect
            clientSocket, addresseIp = self.socket.accept()
            self.socketsClient.append(clientSocket)
            self.adressesIpClient.append(addresseIp)
            print("Adresse Ip client {0}".format(addresseIp));
            
            # On récupère les informations de ce joueur            
            tmp = clientSocket.recv(1024)
            infosJoueur = json.loads(tmp.decode('utf-8'))
            self.listeJoueursEnLigne.append(infosJoueur)
            print('Nom : ' + infosJoueur['nomJoueur'])
            print('Avatar : ' + infosJoueur['avatar'])
            self.pageAttenteJoueur.afficherPageJoueurEnAttente(infosPartie, self.listeJoueursEnLigne)     
            
            # On envoie à tous les clients la liste des joueurs
            listeInfos: list[dict] = []
            listeInfos.append(infosPartie)
            for joueur in self.listeJoueursEnLigne:
                listeInfos.append(joueur)
            
            indice = 0
            for socketClient in self.socketsClient:
                print("envoi client {0}".format(str(indice)))
                encode_listeInfos = json.dumps(listeInfos).encode('utf-8')
                print("encode_listeJoueurs", encode_listeInfos)
                socketClient.sendall(encode_listeInfos)
                indice += 1
            
            indiceJoueur += 1
            
        return self.listeJoueursEnLigne

if __name__ == "__main__" : 
    print("test")
