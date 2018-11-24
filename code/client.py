import socket

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connexion_avec_serveur.connect(('localhost', 12800))
