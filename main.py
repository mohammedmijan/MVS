def services():
    exit()

def password_check(x):
    dict2 = { line.split()[0] : line.split()[1] for line in open("Client_Password.txt") }
    print("\tNote:You just have one chance.\n \tPlease, enter accurate password.")
    print(dict2)
    password_Check = str(input("Password:"))
    x = str(x)
    if dict2[x] == password_Check:
        services()
    elif dict2[x] != password_Check:
        print("Password again.")
        print("If you forget your password.We are sorry.PLease open new account.")
        client_Information(list1)


def client_Information(list1):
    print("[Open an account]") 
    Input_Name = str(input("Input your nick name only:"))
    Input_PhoneNumber = int(input("Phone number:"))
    Input_address = str(input("Mail address:"))
    x = len(list1) + 1
    i = 1
    while True:
        passwordCheck = str(input("This password is fixed.\n \tYou have to write it in your hand notebook.\n \tYou can never change it.\n \tPassword:"))
        if len(passwordCheck) > 5:
            op2 = open("Client_Password.txt", 'a')
            op2.write(f'\n{x} {passwordCheck}')
            op2.close()
            break
        else:
            i+=1
    print("Your ID Number is:",x)
    op1 = open("Client_Address.txt", 'a')
    op1.write(f"\n{x} {Input_Name} +880{Input_PhoneNumber} {Input_address}")
    op1.close()
    with open("ClientID.txt" , 'a') as op:
        op.write(f"\n{x}")
    op.close()
    password_check(x)

def file_readings():# take data from ClientID file and check account
    Input_ID = str(input("Please input your ID No:"))
    for item in list1:
        if Input_ID == item:
            print("You have an account.")
            password_check(Input_ID)
    for item in list1:
        if Input_ID != item:
            print("You have no account.")
            client_Information(list1)

def account():
    i=1
    while True:
        question= str(input("Do you have an account?\n\t>>press 1 for yes\n\t>>press 0 for no \n\t "))
        if question == "1":
                #print(list1)
            file_readings()
        elif question == "0":
            client_Information(list1)

        else:
            print("Enter a valid press....")
            i+=1



with open("ClientID.txt" , 'r') as op:
    list1 = [ma.rstrip() for ma in op.readlines()]
account()
op.close()