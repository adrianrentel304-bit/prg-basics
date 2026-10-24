
pin = "1234"
balance = 1000
attempts = 3
while attempts > 0:
    entered_pin = input("Enter 4-digit PIN: ")
    if len(entered_pin) == 4 and entered_pin.isdigit() and entered_pin == pin:
        print("PIN correct!")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")
else:
    print("Card blocked!")
    exit()

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Exit")
    choice = input("Choose option: ")
    
    if choice == '1':
        print(f"Balance: {balance} PLN")
    elif choice == '2':
        balance += float(input("Enter amount to deposit: "))
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds.")
    elif choice == '4':
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN successfully changed.")
        else:
            print("Invalid PIN format. Must be exactly 4 digits.")
    elif choice == '5':
        break