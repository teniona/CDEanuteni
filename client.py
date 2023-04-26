import socket
import json

def get_employee_data():
    # get employee details from user
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    currently_employed = input("Currently employed? (y/n): ").lower() == 'y'

    # create a dictionary to hold employee details
    employee_data = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "currently_employed": currently_employed
    }

    # serialize dictionary to JSON string
    json_data = json.dumps(employee_data)
    print(json_data)

    return json_data

def connect_to_server():
    # create socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    server_address = ('localhost', 8000)

    # connect to the server
    try:
        client_socket.connect(server_address)
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return

    # get employee data
    json_data = get_employee_data()

    # send employee data to server
    try:
        client_socket.send(json_data.encode())
    except Exception as e:
        print(f"Error sending data to server: {e}")

    client_socket.close()

if __name__ == '__main__':
    connect_to_server()
