from socket import *

def main():
    # Create a UDP socket
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # Define the server address and port
    server_address = ('localhost', 12000)

    # Send a message to the server
    message = b'This is the message.'
    udp_socket.sendto(message, server_address)

    # Receive a response from the server
    data, server = udp_socket.recvfrom(4096)
    print(f'Received {data} from {server}')

    # Close the socket
    udp_socket.close()
if __name__ == '__main__':
    main()