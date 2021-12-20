print("Welcome to Shlok's ATM")
restart = ('Y')
chances = 3
balance = 100000
while chances >= 0:
    pin = int (input('Please Enter Your 4 Digit Pin: '))
    if pin == (1901):
        print('Welcome back! XYZ\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 To Check Your Balance\n')
            print('Please Press 2 To Withdraw Cash\n')
            print('PLease Press 3 To Pay in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What would you like to choose?'))
            if option == 1:
                print('Your Balance is ₹', balance,'\n')
                restart = input('Would you like to go back? ')
            if restart in ('n', 'NO', 'no','N'):
                print('Thank Your for Banking With Us')
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How much would you like to withdraw? \₹500/₹1000/₹1500/₹2000/₹5000/₹10000/₹20000/₹50000 for other enter 1: '))
            if withdrawl in [500, 1000, 1500, 2000, 5000, 10000, 20000, 50000]:
                balance = balance - withdrawl
                print ('\nYour Current Balance is now ₹',balance)
                restart = input('Would you like to go back? ')
            if restart in ('n', 'NO', 'n', 'N'):
                print('Thank You')
                break
    elif withdrawl != [500, 1000, 1500, 2000, 5000, 10000, 20000, 50000]:
        print('Invalid Amounnt, Please Re-try\n')
        restart = ('y')
    elif withdrawl == 1:
        withdrawl = float(input('Please Enter Desired Amount'))

    elif option == 3:
        Pay_in = float(input('How much would you like to Pay In? '))
        balance = balance + Pay_in
        print('\nYour balance is now ₹',balance)
        restart = input('Would you like to go back? ')
        if restart in ('n', 'NO','no','N'):
            print('Thank You')
            break
        elif option == 4:
            print('Please wait while your card is returned...\n')
            print('Thank You For Banking With Us')
            break
        else:
            print('Please enter a correct number. \n')
            restart = ('y')
    elif pin != (1901):
            print('correct Pin')
            chances = chances - 1
            if chances ==0:
                print('\nSorry transcation Failed!')
                break
