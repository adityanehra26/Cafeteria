from userHandler.user import User

class Chef(User):

    def __init__(self, name, db_handler, client_socket):
        super().__init__(name, db_handler, "Chef", client_socket)
    
    def show_menu(self):
        self.client_socket.sendall(f"\n\nWelcome, {self.get_name()}!\n\n".encode())
        while True:
            option_menu = "Chef Menu:\n1. Food Selection\n2. See Feedback\n3. Generate Report\n4. Exit"
            self.send_message_to_user(option_menu)
            choice = self.recieve_message_from_user()
            response = self.handle_choice(choice)
            if response == "Exiting...":
                break        
    
    def get_name(self):
        return super().get_name()
    
    def get_role(self):
        return super().get_role()

    def mealTypesSelection(self):
        while True:
            meal_type_option = "\nSelect Meal Type\n1. BreakFast\n2. Lunch\n3. Dinner"
            self.send_message_to_user(meal_type_option)
            response = self.recieve_message_from_user()
            match response:
                case '1':
                    menu = self.db_handler.view_menu_items(1)
                    self.send_message_to_user(str(menu))
                case '2':
                    menu = self.db_handler.view_menu_items(2)
                    self.send_message_to_user(menu)
                case '3':
                    menu = self.db_handler.view_menu_items(3)
                    self.send_message_to_user(menu)
                case _:
                    break 

    def handle_choice(self, choice):
        if choice == '1':
            self.mealTypesSelection()
        elif choice == '2':
            return "Viewing Feedback..."
        elif choice == '3':
            return "Generating Report..."
        elif choice == '4':
            return "Exiting..."
        else:
            return "Invalid choice!"
        