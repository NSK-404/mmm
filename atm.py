balance = 10000
PIN = "1234"  
def pincheck():
    while True:
        entered_pin = input("Enter your ATM PIN: ")
        if entered_pin == PIN:
            print("Access granted.")
            break
        else:
            print("Incorrect PIN. Try again.")
def check_balance():
    print(f"Your current balance is: ₹{balance:.2f}")
def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")
    except:
        print("Invalid input!")
def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            balance -= amount
            print("Please collect your cash.")
    except:
        print("Invalid input!")
pincheck()
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you for using ATM.")
        break
    else:
        print("Invalid choice. Try again.")
