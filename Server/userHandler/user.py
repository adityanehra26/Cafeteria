class User:
    def __init__(self, name, db_handler, role, client_socket):
        self.__name = name
        self.__role = role
        self.db_handler = db_handler
        self.client_socket = client_socket

    def show_menu(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def handle_choice(self, choice):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def get_role(self):
        return self.__role
    
    def get_name(self):
        return self.__name

    def send_message_to_user(self, msg):
        self.client_socket.sendall((msg + "\n").encode())

    def recieve_message_from_user(self):
        return self.client_socket.recv(1024).decode().strip()





