import socket
import os
import time


port = 12800
hote = 'localhost'

connexion_prin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


connexion_prin.bind((hote,port))

connexion_prin.listen(5)
connexion_avec_client, infos_connexion = connexion_prin.accept()
recu = connexion_avec_client.recv(1024)
print(recu.decode())
def receive_upload():
    accepte = "non"
    #etat = 1
    while (connexion_avec_client.connect):
        recu = connexion_avec_client.recv(1024)

        if accepte == "non": # Condition si on a pas deja envoyer le nom et la taille du fichier
                try:
                    nomFich = recu.split(b"NAME ")[1]
                    nomFich = nomFich.split(b"OCTETS ")[0]
                    nomFich = nomFich.decode()
                    taille = recu.split(b"OCTETS ")[1]
                    taille = taille.decode()
                except:
                    print(">> ##" + recu.split()[0].decode() + "  fichier introuvable")
                    return 0
                print (" >> Fichier '" + nomFich + "' [" + taille + " Ko]")

                accepte = input(" >> Acceptez vous le transfert [o/n] : ") # demande si on accepte ou pas le transfert                               

                if accepte == "o" or accepte == "oui": # Si oui en lenvoi au client et on cree le fichier
                    connexion_avec_client.send(b"GO")
                    print (time.strftime(" >> [%H:%M] transfert en cours veuillez patienter..."))
                    print ("")
                    f = open(nomFich, "wb")
                    
                    taille = float(taille) * 1024 # Conversion de la taille en octets pour le %
                                       
                else :
                    # Si pas accepte on ferme le transfert
                    print("transfert annule")
                    return 0

        
        elif recu == b"BYE": # Si on a recu "BYE" le transfer est termine
            f.close()
            print ("")
            accepte == "non"
            print (time.strftime(" >> Le %d/%m a %H:%M transfert termine !"))
            etat = 1
            return 2

        else: # Sinon on ecrit au fur et a mesure dans le fichier
            f.write(recu)
            if taille > 1024: # Si la taille est plus grande que 1024 on s'occupe du %

                # Condition pour afficher le % du transfert :
                if pourcent == 0 and num > taille / 100 * 10 and num < taille / 100 * 20:
                    print (" >> 10%")
                    pourcent = 1
                elif pourcent == 1 and num > taille / 100 * 20 and num < taille / 100 * 30:
                    print (" >> 20%")
                    pourcent = 2
                elif pourcent < 3 and num > taille / 100 * 30 and num < taille / 100 * 40:
                    print (" >> 30%")
                    pourcent = 3
                elif pourcent < 4 and num > taille / 100 * 40 and num < taille / 100 * 50:
                    print (" >> 40%")
                    pourcent = 4
                elif pourcent < 5 and num > taille / 100 * 50 and num < taille / 100 * 60:
                    print (" >> 50%")
                    pourcent = 5
                elif pourcent < 6 and num > taille / 100 * 60 and num < taille / 100 * 70:
                    print (" >> 60%")
                    pourcent = 6
                elif pourcent < 7 and num > taille / 100 * 70 and num < taille / 100 * 80:
                    print (" >> 70%")
                    pourcent = 7
                elif pourcent < 8 and num > taille / 100 * 80 and num < taille / 100 * 90:
                    print (" >> 80%")
                    pourcent = 8
                elif pourcent < 9 and num > taille / 100 * 90 and num < taille / 100 * 100:
                    print (" >> 90%")                    
                    pourcent = 9
                    
                num = num + 1024


while 1:
   
    commande = input("terminal>")
    
    connexion_avec_client.send(commande.encode())
    if commande.split()[0] == "upload":
        d = receive_upload()
        if d == 0:
            pass        
    else:
        mess = b""
        while mess == b"":
            print (1)
            mess = connexion_avec_client.recv(1024)

        print(mess)






