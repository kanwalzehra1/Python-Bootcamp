#initial Setup FUnction:

def initial_setup():
    accounts = {
        '123456' : {'pin' : '1234' , 'name' : 'John Doe' , 'balance' : 1500.0 },
        '789012' : {'pin' : '5678' , 'name' : 'Jane Smith' , 'balance' : 2000.0 },
        '345678' : {'pin' : '9999' , 'name' : 'Bob Johnson' , 'balance' : 500.0 },
    }
    return accounts

#login Function:

def login(accounts):
    acc_no = input('Enter Your Account Number: ')
    pin = input('Enter Your PIN: ')
    if acc_no in accounts and pin == accounts[acc_no]['pin']:
        #print(acc_no)
        return acc_no
    else:
        print('Error: your account doesn\'t exist.')
        
accounts = initial_setup()


#display menu function:

def display_menu():
    print('Select your choice: ')
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Transfer Money')
    print('5. Change PIN')
    print('6. Exit')
    user_choice = int(input('Enter Your Choice(1-6): '))
    return user_choice
 
 #1. check balance:

def check_balance(accounts,account_number):
    balance = float(accounts[account_number]['balance'])
    # print(balance)
    account_holder = accounts[account_number]['name']
    # print(account_holder)
    print(f'Hey {account_holder}, your current balance is ${balance}')

#2. deposit money fucntion:

def deposit_money(accounts,account_number):
    deposit_amount = int(input('Enter your deposit amount: '))
    if deposit_amount < 10 or deposit_amount > 5000:
        print('Error: Deposit amount must be in range b/w $10-$5000')
        return False
    deposit_amount += accounts[account_number]['balance']
    print(f'Your new balance is {deposit_amount}')
    return True

#3. withdraw function:   
per_day_limit = 1000
def withdraw_money(accounts,account_number):
    global per_day_limit
    withdraw_amount = int(input('Enter your withdraw amount: '))
    # if withdraw_amount < 20 or withdraw_amount > 500:
    #     print('Error: Withdrawal amount should be in range b/w $20-$500')
    #     return False
    if withdraw_amount >= accounts[account_number]['balance']:
        print('Error: You don\'t have sufficient balance')
        return False
    if withdraw_amount % 20 != 0:
        print('Error: Amount must be multiple of 20')
        return False
    if withdraw_amount > per_day_limit:
        print('Error: Per day withdrawal limit is 1000')
        return False
    accounts[account_number]['balance'] -= withdraw_amount
    per_day_limit -= withdraw_amount
    print(f'Your per day limit left ${per_day_limit}')
    print(f'Your new balance is ${accounts[account_number]['balance']}')
    return True

#4. transfer money function:

def transfer_money(accounts,account_number):
    rec_account = input('Enter Recipient Account Number: ')
    if rec_account not in accounts: 
        print('Error: Account not exist')
        return False
    if accounts[rec_account] == accounts[account_number]:
        print('Error: You can\'t tranfer to your own account')
        return False
    else:
        trans_amount = float(input('Enter Transfer Amount: '))
        if trans_amount > accounts[account_number]['balance']:
            print('Error: Insufficient balance')
            return False
        if trans_amount < 10 or trans_amount > 2000:
            print('Error: You can\'t tranfer in range between $10-$2000')
            return False  
        accounts[rec_account]['balance'] += trans_amount
        # print(f'Your new balance is ${accounts[rec_account]['balance']}')
        accounts[account_number]['balance'] -= trans_amount
        print(accounts[account_number]['balance'])
        print('Successfully Transferred')
        return True
    

# 5. CHANGE PIN FUNCTION:

def change_pin(account,account_number):
    curr_pin = input('Enter Your current PIN: ')
    if curr_pin != accounts[account_number]['pin']:
        print('Error: Invalid PIN')
        return False
    new_pin = input('Enter Your new PIN: ')
    if len(new_pin) != 4:
        print('Error: PIN must be 4 digit')
        return False
    if new_pin == curr_pin:
        print('Error: Type New PIN')
        return False            
    verify_pin = input('COnfirm your new PIN: ')
    if verify_pin != new_pin:
        print('Error: Your PIN not match')
        return False
    else:
        accounts[account_number]['pin'] = new_pin       
        print('PIN Changed')
        return True

    
    
    

#main menu function:

def main_menu():
    user_login = login(accounts)
    while True:
        choice = display_menu()
        if choice == 1:
            check_balance(accounts,user_login)
        elif choice == 2:
            deposit_money(accounts,user_login)
        elif choice == 3:
            withdraw_money(accounts,user_login)
        elif choice == 4:
            transfer_money(accounts,user_login)
        elif choice == 5:
            change_pin(accounts,user_login)
        elif choice == 6:
            print('Session End')
            break
        else:
            print('Error: Invalid Choice')   
main_menu()

