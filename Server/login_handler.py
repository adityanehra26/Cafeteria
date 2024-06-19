from userHandler.admin import Admin
from userHandler.chef import Chef
from userHandler.employee import Employee

class LoginHandler:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.client_socket = None
    
    
    def get_credentials(self):
        self.client_socket.sendall("Username: ".encode())
        username = self.client_socket.recv(1024).decode().strip()
        self.client_socket.sendall("Password: ".encode())
        password = self.client_socket.recv(1024).decode().strip()
        return username, password

    def check_credentials(self, username, password):
        role_id = self.db_handler.check_login(username, password)
        if role_id == 1:
            return Admin(username, self.db_handler, self.client_socket)
        elif role_id == 2:
            return Chef(username, self.db_handler, self.client_socket)
        elif role_id == 3:
            return Employee(username, self.db_handler, self.client_socket)
        else:
            return None


    def authenticate(self, client_socket):
        self.client_socket = client_socket
        username, password = self.get_credentials()
        user = self.check_credentials(username, password)
        if user:
            return user
        else:
            client_socket.sendall("Invalid credentials, disconnecting.\n".encode())
            client_socket.close()