##creating tables

#accounts_table = {account : passwword}
#users_table = {account : [amount, Name, Email]}

accounts_table = {1234 : 456, 12345 : 457}

users_table = {1234 : [1000, 'Puji', 'xyz123@gmail.com'],
               12345 : [500, 'pujitha', 'puji123@gmail.com']}


#functions

#login function

def login(username : int, password : int):
    #print("Login Page")
    if username in accounts_table:   #checking the account number is exists in accounts table or not
        if password == accounts_table[username]: #checking the password
            print("Login Successful")
            return True
        else:
            print("Check with credentials")
            return False
    else:
        print("User Not Found")
        return False


#withdraw function

def withdraw(account : int, withdraw_amount : int):
    #checking account in users table
    if account in users_table:
        amount = users_table[account][0]
        #checking amount is sufficent or not
        if amount >= withdraw_amount:
            users_table[account][0] -= withdraw_amount
            print(f"{withdraw_amount} withdraw successful and \
                   current balance is : {users_table[account][0]}")
        else:
            print("Insufficient amount in your account")
    else:
        print("user not Found")




#deposit function

def deposite(account : int, deposite_amount : int):
    if account in users_table:
        #validation amount
        if deposite_amount >= 0:
            users_table[account][0] += deposite_amount
            print(f"{deposite_amount} deposite sucessful and \
                  current balance is :{users_table[account][0]}")
        else:
            print("check with your deposite amount")
    else:
        print("User not Found")


#trasfer function

def transfer(sender : int, reciever : int, transfer_amount : int):
    if sender in users_table:
        amount = users_table[sender][0]
        if reciever in users_table:
            if amount >= transfer_amount:
                users_table[sender][0] -= transfer_amount
                users_table[reciever][0] += transfer_amount
                print(f"{transfer_amount} Transfer successful and \
                      current balance is : {users_table[sender][0]}")
            else:
                print("Insufficient amount in your amount")
        else:
            print("Reciever amount is not found")
    else:
        print("User not found")

#ministatement functionc
def ministatement(account : int):
    print("Ministatement Page development under processing")

#balance enquiry function defination
def balance_enquiry(account : int):
    if account in users_table:
        print(f"current balance is: {users_table[account][0]}")
    else:
        print("User not found")

#logout function

def logout():
    print("Logout Successfully")
    exit()

#main

if __name__ == "__main__":
    print("Welcome to Codegnan Bank Application")
    username = int(input("Enter your account number:"))
    password = int(input("Enter your password:"))
    login_val = login(username = username, password = password)
    while login_val:
        operations = ("1. Withdraw \n",
                      "2. Deposit \n",
                      "3. Transfer \n",
                      "4. Mini statement \n",
                      "5. Balance Amount \n",
                      "6. Logout")
        print(*operations)
        choice = int(input("Select your operations:"))
        if choice == 1:
            amount = int(input("Ener your withdraw amount:"))
            withdraw(account = username, withdraw_amount = amount)
        elif choice == 2:
            amount = int(input("Enter your deposite amount:"))
            deposite(account = username, deposite_amount = amount)
        elif choice == 3:
            account = int(input("Enter reciever account number:"))
            amount = int(input("Enter your transfer amount:"))
            transfer(sender = username, reciever = 1234, transfer_amount = amount)
        elif choice == 4:
            ministatement(account = username)
        elif choice == 5:
            balance_enquiry(account = username)
        elif choice == 6:
            logout()
        else:
            print("Select operation in between 1 to 6")