from features.functionality import Functionality
from database_handler import DatabaseHandler

class ViewMenu(Functionality):
    def __init__(self, db_handler: DatabaseHandler):
        self.db_handler = db_handler

    def execute(self):
        try:
            menu_items = self.db_handler.get_menu_items()

            if not menu_items:
                return "No menu items available."

            # Print the header
            output = "Menu:\n"
            output += "{:<5} {:<20} {:<10} {:<15} {:<15}\n".format("ID", "Name", "Price", "Availability", "MealType")
            output += "-"*70 + "\n"

            # Print each row
            for item in menu_items:
                id = item['ID']
                name = item['Name']
                price = item['Price']
                availability = "Yes" if item['AvailabilityStatus'] else "No"
                meal_type = item['MealType']
                output += "{:<5} {:<20} {:<10} {:<15} {:<15}\n".format(id, name, price, availability, meal_type)

            return output

        except Exception as e:
            return f"Error: {e}"
