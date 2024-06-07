'''
Objectives
1. Deposit money to balance
2. Select number of lines going to bet
2. Place bet for each lines
3. Spin the slot machine
4. For every win, calculate the multiplier
5. Update balance
'''

import random


NUMBER_OF_REELS = 3

ITEMS_PER_REEL = 3

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


def generate_reels():
    # Generate all occurences/copy of each item
    items = []
    for key, amt in SYMBOL_AMOUNT.items():
        for i in range(amt):
            items.append(key)

    #Create each reel and append a random item for each index
    reels = []
    for i in range(NUMBER_OF_REELS):
        reel = []
        for j in range(ITEMS_PER_REEL):
            num = random.randint(0, len(items)-1)
            item = items.pop(num)
            reel.append(item)
        reels.append(reel)
    return reels

def play_slot(bal, numLine, bet):
    slot = generate_reels()
    print(slot)
    pass

def place_bet(balance, numLine):
    while True:
        try:
            bet = int(input(f'\nEnter the amount to bet per chosen line: '))
            if balance < (bet * numLine):
                print('Invalid amount! Try again.')
            else:
                print(f'You have successfully bet {bet} on {numLine} line(s).\n')
                play_slot(balance, numLine, bet)
                break
        except:
            print('Invalid amount of bet per line!')


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
        while True:
            try:
                numLine = int(input('\nEnter the number of lines you are going to bet on (1-3): '))
                if numLine > 3 or numLine <= 0:
                    print('Invalid number of lines!')
                else:
                    place_bet(balance, numLine)
                    break
            except:
                print('Invalid input!')
    elif decision == '3':
        print('\nThank you for playing!')
        break
    else:
        print('Invalid input! Try again.\n')
        continue