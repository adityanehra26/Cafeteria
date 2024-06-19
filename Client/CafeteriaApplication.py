import socket

def main():
    host = 'localhost'  # The server's hostname or IP address
    port = 12345        # The port used by the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect((host, port))
    
    # Receive and send login information
    username_prompt = client_socket.recv(1024).decode()
    username = input(username_prompt)
    client_socket.sendall(username.encode())
    
    password_prompt = client_socket.recv(1024).decode()
    password = input(password_prompt)
    client_socket.sendall(password.encode())
    
    # Receive welcome message or invalid credentials message
    response = client_socket.recv(1024).decode()
    print(response)
    
    # If login is successful, handle menu interaction
    if "Welcome" in response:
        while True:
            response = client_socket.recv(1024).decode()
            print(response)
            if "Exiting..." in response:
                break
            choice = input("Enter your choice: ")
            if response != None:
                client_socket.sendall(choice.encode())
            

if __name__ == "__main__":
    main()
