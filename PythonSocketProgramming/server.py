from http import client
import socket
import threading

# Number of bytes a message header is in length
MESSAGE_HEADER = 64
# Ports 0 to 1023 are reserved 
PORT = 5050
# Dynamically get the private ip address of the computer running the script
SERVER = socket.gethostbyname(socket.gethostname())
# Binds the server and port to an address tuple. Tuples are immutable ordered lists. 
ADDRESS = (SERVER, PORT)
# Message format
MESSAGE_FORMAT = 'utf-8'
# Client disconnection
DISCONNECT_MESSAGE = "!DISCONNECT"
# Streaming data through a socket using ipv4 adddresses. 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind both the server and server port to the server. 
server.bind(ADDRESS)

def handle_client(connection, address):
    print(f"New connection {address} connected")
    
    client_connected = True
    while client_connected:
        client_message_length = connection.recv(MESSAGE_HEADER).decode(MESSAGE_FORMAT)
        if client_message_length:
            client_message_length = int(client_message_length)
            client_message = connection.recv(client_message_length).decode(MESSAGE_FORMAT)
            if client_message == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{address}] {client_message}")
            connection.send("Message was received".encode(MESSAGE_FORMAT))
    client_connected.close()

def start():
    server.listen()
    while True:
        # Think of this as similar to javascript destructuring with array elements. The 'address' argument stores the ipv4 address and port information.
        # The 'connection' argument stores an object that allows us to send information about the server to the connection itself.  
        connection, address = server.accept()
        # When a new connection to the server is created, a thread which runs the function handle_client is created, and passed the server connection arguments. 
        # Each thread will be running concurrently with each new connection to the server, until the server can no longer handle more requests and fails. 
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"Active connections: {threading.activeCount - 1}")
        
print("Server is starting")
start()