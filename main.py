# this is a text based slot machine details in notes.txt

def deposit():
    while True :
        amount =input("What would you like to deposit? $")
        if amount.isdigit():
            amount =int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

deposit()
    