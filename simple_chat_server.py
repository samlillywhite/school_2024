import socket
import threading

# Server configuration
host = '0.0.0.0'  # Listen on all available interfaces
port = 55555        # Port to bind the server to

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f'Server started on {host}:{port}')

# List to keep track of connected clients
clients = []

# Event to signal threads to stop
stop_event = threading.Event()

def broadcast(message, sender_socket):
    """Send the message to all clients except the sender."""
    for client in clients:
        try:
            client.send(message)
        except:
            client.close()
            clients.remove(client)

def handle_client(client_socket):
    """Handle incoming messages from a client."""
    while not stop_event.is_set():
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))
                #broadcast(message, client_socket)
            else:
                break
        except:
            break

    client_socket.close()
    if client_socket in clients:
        clients.remove(client_socket)

def send_messages():
    """Send messages to the server."""
    while not stop_event.is_set():
        message = input('')
        try:
            broadcast(message.encode('utf-8'), None)
        except:
            break

# Accepting incoming client connections in a thread
def accept_connections():
    while not stop_event.is_set():
        try:
            client_socket, client_address = server_socket.accept()
            print(f'Connection from {client_address}')
            
            clients.append(client_socket)
            
            threading.Thread(target=handle_client, args=(client_socket,)).start()
        except:
            break

try:
    # Start the thread for accepting connections
    threading.Thread(target=accept_connections).start()
    send_messages()
    
except KeyboardInterrupt:
    print("\nShutting down server...")
    stop_event.set()

    # Close all client connections
    for client in clients:
        client.close()

    # Close the server socket
    server_socket.close()

    print("Server shut down successfully.")
