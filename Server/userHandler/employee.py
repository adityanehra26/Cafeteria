from userHandler.user import User

class Employee(User):

    def __init__(self, name, db_handler, client_socket):
        super().__init__(name, db_handler, "Employee", client_socket)

    def get_name(self):
        return super().get_name()
    
    def get_role(self):
        return super().get_role()

    def show_menu(self):
        self.client_socket.sendall(f"\n\nWelcome, {self.get_name()}!\n\n".encode())
        while True:
            option_menu = "Employee Menu:\n1. Give Feedback\n2. Menu Items\n3. Exit"
            self.client_socket.sendall((option_menu + "\n").encode())
            choice = self.client_socket.recv(1024).decode().strip()
            response = self.handle_choice(choice)
            self.client_socket.sendall((response + "\n").encode())
            if response == "Exiting...":
                break

    def handle_choice(self, choice):
        if choice == '1':
            return "Giving Feedback..."
        elif choice == '2':
            return "Viewing Menu Items..."
        elif choice == '3':
            return "Exiting..."
        return "Invalid choice!"