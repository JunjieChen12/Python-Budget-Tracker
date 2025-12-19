from manager import ExpenseManager


def main():
    #call ExpenseManager 
    mgr = ExpenseManager()

    while True:
        #print MENU
        print("\n=== BUDGET TRACKER ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total")
        print("4. Quit")
        
        #get user input
        input_choice = int(input("Choose an option "))
                
        #OPTION 1
        if input_choice == 1:
            print("\n--- New Expense ---")
            item_name = input("What did you buy? ")
            while True:
                try:
                    item_price = float(input("How much was it? "))
                    break
                except ValueError:
                    print("Invalid price. Please enter a number like 10.50")

            item_category = input("Category e.g (Food, Rent, Fun): ")
 
            mgr.add_expense(item_name, item_price, item_category)
            mgr.save_to_file()
                
        #OPTION 2
        elif input_choice == 2:
            print("\n--- All Expenses ---")
            #check if there is any expesnes first
            if len(mgr.expenses) == 0:
                print("No expenses recorded yet")
                #print if there are expenses
            else:
                for expense in mgr.expenses:
                    print(expense)

        #OPTION 3
        elif input_choice == 3:
            total_price = mgr.get_total()
            print("\n--- Expense total ---")
            print(f"Your total amount is {total_price:.2f}")

            if total_price > 0:
                pay_input = input(f"Would you like to pay off this balance? (Yes/No): ")
                
                if pay_input == "Yes":
                    payment_type = input("Pay (Total) or (Custom) amount?: ")
                    
                    amount_to_pay = 0.0
                    
                    if payment_type == "Total":
                        amount_to_pay = total_price
                    
                    elif payment_type == "Custom":
                        # Convert input to float so we can do math
                        amount_to_pay = float(input("Enter amount to pay: "))

                    # --- THE MAGIC FIX ---
                    # Don't do subtraction here. 
                    # Just tell the manager: "I spent NEGATIVE money."
                    if amount_to_pay > 0:
                        mgr.add_expense("Payment", -amount_to_pay, "Debt Payoff")
                        # Force a save immediately so it sticks
                        mgr.save_to_file() 
                        print(f"Payment of ${amount_to_pay:.2f} accepted!")
                        print(f"New Balance: ${mgr.get_total():.2f}")

        #OPTION 4
        elif input_choice == 4:
            print("Goodbye")
            break
        #Checks if user input is valid (1-4)
        else:
            print("Invalid choice. Please try again")

        #slows down the program
        input("\nPress Enter to continue")
 

if __name__ == "__main__":
    main()