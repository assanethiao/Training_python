import socket
import sys

localhost = '127.0.0.1'
PORT = 5000
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysocket.connect((localhost, PORT))  
except socket.error:
    print("La connexion au socket a échoué")
    sys.exit()

print("La connexion est établie")

msgServ = mysocket.recv(1024).decode()

while True:
    
    if msgServ.upper() == "FIN" or msgServ.strip() == "":
        break
    print("S>", msgServ)
    msgClient = input("C> ")
    mysocket.send(msgClient.encode())
    msgServ = mysocket.recv(1024).decode()

print("Connexion interrompue.")
mysocket.close()
