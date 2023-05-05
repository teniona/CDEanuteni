import socket
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/employee', methods=['POST'])
def handle_employee_data():
    # extract employee data from HTTP request
    employee_data = request.get_json()

    # process employee data
    # here, can add code to store employee data in a database or file
    # for now, just return the data as a JSON response
    response_data = {
        "status": "success",
        "employee_name": f"{employee_data['first_name']} {employee_data['last_name']}",
        "employee_age": employee_data['age'],
        "employee_currently_employed": employee_data['currently_employed']
    }
    return jsonify(response_data)

def handle_client_connection(client_socket):
    try:
        # receive data from the client
        json_data = client_socket.recv(1024).decode()

        # send the data to the Flask app for processing
        with app.test_request_context('/employee', method='POST', data=json_data):
            response = app.full_dispatch_request()

        # send the response back to the client
        client_socket.send(response.get_data())
    
    except Exception as e:
        print(f"Error handling client connection: {e}")
        # send error response to the client
        error_response = {
            "status": "error",
            "message": "An error occurred while processing your request"
        }
        client_socket.send(json.dumps(error_response).encode())
    
    finally:
        # close the connection
        client_socket.close()


if __name__ == '__main__':
    # start the Flask app in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={'debug': False})
    flask_thread.start()

    # create a new socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    server_address = ('localhost', 8001)

    # bind the socket to a specific address and port
    server_socket.bind(server_address)

    # listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {server_address}")

    while True:
        # accept a new connection
        client_socket, client_address = server_socket.accept()

        # handle the client connection in a separate thread
        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_thread.start()
