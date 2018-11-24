import socket

port = 12809
hote = 'localhost'

connexion_prin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


connexion_prin.bind((hote,port))

connexion_prin.listen(5)
connexion_avec_client, infos_connexion = connexion_prin.accept()
while 1:



    
    commande = input("terminal>")
    connexion_avec_client.send(commande.encode())
    mess = b""
    while mess == b"":
        print (1)
        mess = connexion_avec_client.recv(1024)

    print(mess)
