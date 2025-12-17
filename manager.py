import json

#import my expense class
from expense import Expense

class ExpenseManager:

    def __init__(self):
        self.expenses = []
        self.filename = "budget.json"
        self.load_from_file()


    #function adds expenses to a list
    def add_expense(self, name, price, category):
        #creates a new expense
        new_expense = Expense(name, price, category)
        #adds expense to the list
        self.expenses.append(new_expense)

    #function get total price from the list
    def get_total(self):
        #total starts at 0
        total = 0
        #loops through expense in self.epxenses
        for expense in self.expenses:
            #adds the each expense price to the total
            total += expense.price
        return total

    #function saves it to a json and converts python data to json data.
    def save_to_file(self):
        #empty list
        json_data = []
        #loop through each expense 
        for expense in self.expenses:
            #create a temporay storage for each description and converts it into json
            temp_format = {
                "name" : expense.name,
                "price" : expense.price,
                "type" : expense.category
            }
            #appends the converted text to the json.data list
            json_data.append(temp_format)
        
        #save the json.data list to the file
        with open("budget.json", "w") as file:
            json.dump(json_data, file, indet = 4)

    def load_from_file(self):
        # 1. Try to open the file 
        try:
            with open("budget.json", "r") as file:
                # This loads the data as a LIST OF DICTIONARIES
                # e.g. [{"name": "Burger", "price": 10, ...}, {...}]
                data = json.load(file)
                
                # 2. Loop through the list of dictionaries
                for entry in data:
                    # 3. Create a new Object using the dictionary data
                    recreated_expense = Expense(entry['name'] , entry['price'], entry['category']) 
                    # 4. Add it to our main list
                    self.expenses.append(recreated_expense)
                    
        except FileNotFoundError:
            # If the file doesn't exist, we just start with an empty list.
            pass