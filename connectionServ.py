import socket
import subprocess

# Définir l'adresse IP du serveur et le port
SERVER_IP = "192.168.0.1"  # Remplace par l'IP de ton serveur
PORT = 12345  # Même port que celui utilisé par Netcat

def connectToServ(ip,port,command):
# Création du socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:
        # Connexion au serveur
        client.connect((ip, port))
        print(f"Connecté à {ip}:{port}")

        client.sendall(command.encode()) #convertit le str
        data = client.recv(32).decode()
        print(data)
        return [int(x) for x in data.split(",", 1)]

        

    except Exception as e:
        print("Erreur:", e)

    finally:
        # Fermer la connexion
        client.close()


#connectToServ("192.168.0.2",12345,"GTP")

#GGS
#GBS
#GTP
#GBP
#GGP