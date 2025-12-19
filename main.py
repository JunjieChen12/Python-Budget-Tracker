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
            #ask user for the name of the item
            item_name = input("What did you buy? ")
            #Check for correct price input
            while True:
                try:
                    #get price of the item
                    item_price = float(input("How much was it? "))
                    break
                except ValueError:
                    print("Invalid price. Please enter a number like 10.50")
            #get category of the item
            item_category = input("Category e.g (Food, Rent, Fun): ")
            
            #call add expense and save values to budget.json
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
            #call get total and save to totap price
            total_price = mgr.get_total()
            #display
            print("\n--- Expense total ---")
            print(f"Your total amount is {total_price:.2f}")
            
            #Check 1. if Price is greater than 0 display a pay option
            if total_price > 0:
                pay_input = input(f"Would you like to pay off this balance? (Yes/No): ")
                #If user wants to pay get payment type
                if pay_input == "Yes":
                    payment_type = input("Pay (Total) or (Custom) amount?: ")
                    
                    amount_to_pay = 0.0
                    #if type is total take total price to pay
                    if payment_type == "Total":
                        amount_to_pay = total_price
                    #if not total get user custom payment
                    elif payment_type == "Custom":
                        # Convert input to float so we can do math
                        amount_to_pay = float(input("Enter amount to pay: "))

 
                    # call add_expense with a negative expense
                    #checks if price is greater than 0 to avoid subtracting 0
                    if amount_to_pay > 0:
                        #Call add expense with Name, negative amount to subtract, Category
                        mgr.add_expense("Payment", -amount_to_pay, "Debt Payoff")
                        #save to file to keep track
                        mgr.save_to_file() 
                        #Display to user of payment amoount
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