import socket
import sys

localhost = '127.0.0.1'
PORT = 5000
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysocket.bind((localhost, PORT))
except socket.error:
    print("La connexion au socket a échoué")
    sys.exit()

while True:
    print("Serveur prêt, en attente de requêtes ...")
    mysocket.listen(4)

    connexion, adresse = mysocket.accept()
    print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))
    connexion.send("Vous êtes connecté au serveur Marcel. Envoyez vos messages.".encode())

    msgClient = connexion.recv(1024).decode()

    while True:
        print("C> ", msgClient)
        if msgClient.upper() == "FIN" or msgClient == "":
            break
        msgServ = input("S> ")
        connexion.send(msgServ.encode())
        msgClient = connexion.recv(1024).decode()

    connexion.send("Au revoir !".encode())
    print("Connexion interrompue.")
    connexion.close()
    

   
