# this is a text based slot machine details in notes.txt
#adding a global constant. CONSTANTS ARE IN ALL CAPS
MAX_LINES = 3 
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

#collect bet

def get_number_of_lines():
     while True :
        lines =input("Enter the mumber of lines to bet on (1-" + str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines =int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

     return lines
   

def main():
    balance=deposit()
    lines=get_number_of_lines()
    print(balance,lines)

main()


    