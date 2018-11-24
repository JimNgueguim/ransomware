import socket

port = 0
hote = ''

connexion_prin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


connexion_prin.bind((hote,port))
connexion_avec_client, infos_connexion = connexion_principale.accept()


