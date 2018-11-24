import socket

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connexion_avec_serveur.connect(('localhost', 12809))

connexion_avec_serveur.send(b"je suis en ligne")

while 1:
    rec = connexion_avec_serveur.recv(1024)
    print(rec)

    connexion_avec_serveur.send(b"resultat de la commande")
