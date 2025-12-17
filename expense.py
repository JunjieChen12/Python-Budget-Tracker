#define an expense
class Expense:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    #return a formatted string instead of the memory address
    def __repr__(self):
        #.2f means displaying with 2 decimals instead of one. (.5 -> .50)
        return f"Item: {self.name}, Price: {self.price:.2f}, Type: {self.category}"
