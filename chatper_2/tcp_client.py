from socket import *

def main():
    # Create a TCP socket
    tcp_socket = socket(AF_INET, SOCK_STREAM)

    # Define the server address and port
    server_address = ('localhost', 12000)

    # Connect to the server
    tcp_socket.connect(server_address)

    # Send a message to the server
    message = b'This is the message.'
    tcp_socket.sendall(message)

    # Receive a response from the server
    data = tcp_socket.recv(4096)
    print(f'Received {data}')

    # Close the socket
    tcp_socket.close()

if __name__ == '__main__':
    main()