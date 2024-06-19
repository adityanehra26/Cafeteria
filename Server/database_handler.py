import mysql.connector

class DatabaseHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
    
    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
    
    def check_login(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT RoleID FROM User WHERE Name=%s AND Password=%s", (username, password))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result[0]
        return None
    
    def view_menu_items(self, meal_type_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT ID, Name, Price, AvailabilityStatus FROM menuitem WHERE MealTypeID=%s", (meal_type_id,))
        items = cursor.fetchall()
        cursor.close()
        
        available_items = "\nAvailable Items:\nID,   NAME (PRICE)   \n"
        unavailable_items = "Unavailable Items:\n"
        
        for item in items:
            item_str = f"{item[0]},    {item[1]} ({item[2]})\n"
            if item[3]:  # AvailabilityStatus is True (1)
                available_items += item_str
            else:
                unavailable_items += item_str
        menu = available_items + '\n' +  unavailable_items
        return menu

    def close(self):
        if self.conn:
            self.conn.close()
