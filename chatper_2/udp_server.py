from socket import *
def main():
    # Create a UDP socket
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # Bind the socket to an address and port
    server_address = ('localhost', 12000)
    udp_socket.bind(server_address)

    print('Waiting for a message...')

    while True:
        # Receive a message from a client
        data, client_address = udp_socket.recvfrom(4096)
        print(f'Received {data} from {client_address}')

        # Send a response back to the client
        response = b'This is the response.'
        udp_socket.sendto(response, client_address)
        print(f'Sent {response} to {client_address}')

    # Close the socket
    udp_socket.close()
if __name__ == '__main__':
    main()
# This code creates a UDP server that listens for messages from clients and responds to them.