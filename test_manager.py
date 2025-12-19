import unittest
import os
from manager import ExpenseManager

# We create a class that inherits from unittest.TestCase
# This tells Python: "This class contains tests."
class TestExpenseManager(unittest.TestCase):

    # 1. SETUP: Runs automatically BEFORE every single test method
    def setUp(self):
        # We create a new manager instance
        self.mgr = ExpenseManager()
        
        # CRITICAL: We change the filename to a junk file
        # We do NOT want to overwrite your real "budget.json"
        self.mgr.filename = "test_budget.json" 
        
        # Ensure we start with an empty list
        self.mgr.expenses = [] 

    # 2. TEARDOWN: Runs automatically AFTER every single test method
    def tearDown(self):
        # Clean up the mess. If the test created a file, delete it.
        if os.path.exists("test_budget.json"):
            os.remove("test_budget.json")

    
    def test_add_expense(self):
        # A. The Action
        self.mgr.add_expense("Test Burger", 10.00, "Food")
        
        # B. The Assertions (The Proof)
        
        # Check 1: Did the list grow to size 1?
        self.assertEqual(len(self.mgr.expenses), 1)
        
        # Check 2: Is the price correct?
        # We look at the first item [0] and check its price
        self.assertEqual(self.mgr.expenses[0].price, 10.00)
        
        # Check 3: Is the name correct?
        self.assertEqual(self.mgr.expenses[0].name, "Test Burger")

    def test_get_total(self):
        #add two different expenses
        self.mgr.add_expense("Test Hot Dog", 10.00, "Food")
        self.mgr.add_expense("Test Chips", 4.99, "Food")
        
        #check if the math is right
        self.assertEqual(self.mgr.get_total(), 14.99)


#if __name__ == "__main__":
    #unittest.main()