import socket

# Number of bytes a message header is in length
MESSAGE_HEADER = 64
# Ports 0 to 1023 are reserved 
PORT = 5050
# Message format
MESSAGE_FORMAT = 'utf-8'
# Client disconnection
DISCONNECT_MESSAGE = "!DISCONNECT"
# Streaming data through a socket using ipv4 adddresses. 
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
MESSAGE_FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Successfully connected a client to a server
client.connect(ADDRESS)

def send_message(message):
    client_message = message.encode(MESSAGE_FORMAT)
    
    client_message_length = len(client_message)
    
    client_message_send_length = str(client_message_length).encode(MESSAGE_FORMAT)

    # Byte representation of a string when a string has a preceeding b
    client_message_send_length += b' ' * (MESSAGE_HEADER - len(client_message_send_length))
    
    client.send(client_message_send_length)
    
    client.send(client_message) 
    
    print(client.recv(MESSAGE_HEADER))