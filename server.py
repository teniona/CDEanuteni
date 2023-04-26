import socket
import threading
import json

def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")

    while True:
        # receive data from client
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
        except Exception as e:
            print(f"Error receiving data from client {client_address}: {e}")
            break

        # parse JSON data received from client
        try:
            employee_data = json.loads(data)
            print(f"Received data from {client_address}: {employee_data}")
        except Exception as e:
            print(f"Error parsing JSON data received from {client_address}: {e}")
            continue

        # process employee data
        # here, can add code to store employee data in a database or file
        # for now, just print the data to console
        print(f"Employee name: {employee_data['first_name']} {employee_data['last_name']}")
        print(f"Employee age: {employee_data['age']}")
        print(f"Employee currently employed: {employee_data['currently_employed']}")

    client_socket.close()
    print(f"Connection with {client_address} closed")


def start_server():
    # create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind socket to a address
    server_address = ('localhost', 8001)
    server_socket.bind(server_address)

    # listen for incoming connections (max backlog of 5)
    server_socket.listen(5)
    print("Server is listening on port 8000")

    while True:
        # wait for a connection
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()

        # create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    start_server()
