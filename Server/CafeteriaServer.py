import socket
import threading
from database_handler import DatabaseHandler
from login_handler import LoginHandler

class CafeteriaServer:
    def __init__(self, host, port, db_host, db_user, db_password, db_name):
        self.host = host
        self.port = port
        self.db_handler = DatabaseHandler(db_host, db_user, db_password, db_name)
        self.login_handler = LoginHandler(self.db_handler)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start_server(self):
        self.db_handler.connect()
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
    
    def handle_client(self, client_socket):
        user = self.login_handler.authenticate(client_socket)
        user.show_menu()
        client_socket.close()

def main():
    host = 'localhost'
    port = 12345
    db_host = 'localhost'
    db_user = 'root'
    db_password = '12345678'
    db_name = 'cafeteria'
    
    server = CafeteriaServer(host, port, db_host, db_user, db_password, db_name)
    server_thread = threading.Thread(target=server.start_server)

    server_thread.start()
    server_thread.join()

if __name__ == "__main__":
    main()
