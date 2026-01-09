while True:
    try:
        bank_code = 1234
        user_input = int(input("Enter your bank code: "))

        if user_input == bank_code:
            
            amount = int(input("Access Granted. Welcome! How much to withdraw? "))
            
            if amount > 500:
                print("Insufficient funds. Transaction cancelled.")
            elif amount < 0:
                print("Invalid amount.")
            else:
                print("Transaction complete. Please take your cash.")
                break 
        
        else:
            
            print("Access Denied. Incorrect bank code.")

    except ValueError:
        
        print("Invalid input. Please enter a valid bank code.")