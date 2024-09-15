balance = 5000
correct_pin = "1234"
def display_menu():
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
pin = input("Enter your PIN: ")
if pin == correct_pin:
    while True:
        display_menu()
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            print(f"Your current balance is: ₹{balance}")
        
        elif choice == 2:
            deposit_amount = float(input("Enter the amount to deposit: ₹"))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"₹{deposit_amount} has been deposited. Your new balance is: ₹{balance}")
            else:
                print("Invalid deposit amount.")
        
        elif choice == 3:
        
            withdraw_amount = float(input("Enter the amount to withdraw: ₹"))
            if withdraw_amount > balance:
                print("Insufficient balance.")
            elif withdraw_amount <= 0:
                print("Invalid withdrawal amount.")
            else:
                balance -= withdraw_amount
                print(f"₹{withdraw_amount} has been withdrawn. Your new balance is: ₹{balance}")
        
        elif choice == 4:
            
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a valid option.")
else:
    print("Incorrect PIN. Access denied.")
