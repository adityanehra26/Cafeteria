from userHandler.user import User

class Admin(User):
    def __init__(self, name, db_handler, client_socket):
        super().__init__(name, db_handler, "Admin", client_socket)

    def show_menu(self):
        self.client_socket.sendall(f"\n\nWelcome, {self.get_name()}!\n\n".encode())
        
        while True:
            menu = "Admin Menu:\n1. Add Food Item \n2. Exit\n"
            self.client_socket.sendall((menu + "\n").encode())
            choice = self.client_socket.recv(1024).decode().strip()
            response = self.handle_choice(choice)
            self.client_socket.sendall((response + "\n").encode())
            if response == "Exiting...":
                break
    
    def get_name(self):
        return super().get_name()
    
    def get_role(self):
        return super().get_role()

    def handle_choice(self, choice):
        if choice == '1':
            return "Performing Food Item Update..."
        elif choice == '2':
            return "Exiting..."
        return "Invalid choice!"