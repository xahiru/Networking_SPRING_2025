from socket import *

def start_tcp_server(host='localhost', port=12000):
    # Create a TCP socket
    tcp_socket = socket(AF_INET, SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = (host, port)
    tcp_socket.bind(server_address)

    # Listen for incoming connections
    tcp_socket.listen(1)
    print(f"Listening on {host}:{port}")

    while True:
        # Wait for a connection
        connection, client_address = tcp_socket.accept()
        try:
            print(f"Connection from {client_address}")

            # Receive data from the client
            data = connection.recv(4096)
            print(f"Received: {data}")

            # Send a response back to the client
            response = b'This is the response.'
            connection.sendall(response)
            print(f"Sent: {response}")

        finally:
            # Clean up the connection
            connection.close()

# def start_tcp_server(host='127.0.0.1', port=65432):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((host, port))
#         server_socket.listen()
#         print(f"Server listening on {host}:{port}")
        
#         while True:
#             conn, addr = server_socket.accept()
#             with conn:
#                 print(f"Connected by {addr}")
#                 while True:
#                     data = conn.recv(1024)
#                     if not data:
#                         break
#                     print(f"Received: {data.decode()}")
#                     conn.sendall(data)  # Echo the data back to the client

if __name__ == "__main__":
    start_tcp_server()