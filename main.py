# this is a text based slot machine details in notes.txt

def deposit():
    while True :
        amount =input("What would you like to deposit? $")
        if amount.isdigit():
            amount =int(amount)
        
    