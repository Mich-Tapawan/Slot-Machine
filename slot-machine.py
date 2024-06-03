'''
Objectives
1. Deposit money to balance
2. Select number of lines going to bet
2. Place bet for each lines
3. Spin the slot machine
4. For every win, calculate the multiplier
5. Update balance
'''

SYMBOL_AMOUNT = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3
}

SYMBOL_VALUES = {
    'A' : 2,
    'B' : 3,
    'C' : 4,
    'D' : 5
}

def deposit():
    while True:
        try:
            deposit = int(input(f"\nCurrent Balance: {balance}\nEnter the amount to deposit: "))
            print(f'{deposit} is successfully added to the balance!')
            return int(deposit)
        except:
            print('Invalid input!')

def play_slot(bal, numLine, bet):
    pass

def place_bet(balance, numLine):
    while True:
        try:
            bet = int(input(f'\nEnter the amount to bet per chosen line: '))
            if balance < (bet * numLine):
                print('Invalid amount! Try again.')
            else:
                print(f'You have successfully bet {bet} on {numLine} line(s).')
                play_slot(balance, numLine, bet)
        except:
            print('Invalid input!')

print('||| SLOT MACHINE GAME |||\n')
balance = 0
while(True):
    print(f'Current Balance: {balance}\n1. Deposit money\n2. Place a bet\n3.Exit')
    decision = input("Enter the number of the option you want to choose: ")

    if decision == '1':
        dep = deposit()
        balance += dep
        print(f"Updated Balance: {balance}\n")
    elif decision == '2':
        place_bet()
    elif decision == '3':
        print('\nThank you for playing!')
        break
    else:
        print('Invalid input! Try again.\n')
        continue