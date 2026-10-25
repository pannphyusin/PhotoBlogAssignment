import socket
import os
from datetime import datetime

HOST = '0.0.0.0'
PORT = 8000

# Create request directory if it doesn't exist
os.makedirs("request", exist_ok=True)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Socket Server listening on port {PORT}...")

try:
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        request_data = client_socket.recv(1024)
        if request_data:
            timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            filename = os.path.join("request", f"{timestamp}.bin")
            
            with open(filename, "wb") as f:
                f.write(request_data)
                
            print(f"Saved raw request to {filename}")
            
            # Send standard HTTP 200 OK response back
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 2\r\n\r\nOK"
            client_socket.sendall(response.encode('utf-8'))
            
        client_socket.close()
except KeyboardInterrupt:
    print("\nServer shutting down.")
    server_socket.close()
