'''
Objectives
1. Deposit money to balance
2. Select number of lines going to bet
2. Place bet for each lines
3. Spin the slot machine
4. For every win, calculate the multiplier
5. Update balance
'''

def deposit():
    while True:
        try:
            deposit = int(input(f"\nCurrent Balance: {balance}\nEnter the amount to deposit: "))
            print(f'{deposit} is successfully added to the balance!')
            return int(deposit)
        except:
            print('Invalid input!')

def place_bet():
    pass

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