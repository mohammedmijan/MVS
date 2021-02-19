import re
from PIL import Image
from pytesseract import *


def services():
    exit()


def password_check(x):#checking password
    dict2 = { line.split()[0] : line.split()[1] for line in open("Shop_Owner_Password.txt") }
    print("\tNote:You just have one chance.\n \tPlease, enter accurate password.")
    #print(dict2)
    password_Check = str(input("Password:"))
    x = str(x)
    if dict2[x] == password_Check:
        services()
    elif dict2[x] != password_Check:
        print("Password again.")
        print("If you forget your password.We are sorry.PLease open new account.")
        client_Information(list1)

def client_Information(list1):#take information
    print("[Open an account]") 
    Input_Name = str(input("Input your nick name only:"))
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ima = Image.open(f"{Input_Name.lower()}cardpic.jpg")
    txt1 = image_to_string(ima)
    txt1_1 = f'"""{txt1}"""'
    txt_phone = re.findall(r"[+]+88-+01[0-9]+-+[0-9]+",txt1_1)
    txt_email = re.findall(r"[a-z._0-9A-Z]+@[a-zA-Z.]+[a-zA-Z]",txt1_1)
    Input_PhoneNumber = txt_phone[0]
    Input_address = txt_email[0]
    x = len(list1) + 1
    i = 1
    while True:
        passwordCheck = str(input("This password is fixed.\n \tYou have to write it in your hand notebook.\n \tYou can never change it.\n \tPassword:"))
        if len(passwordCheck) > 5:
            op2 = open("Shop_Owner_Password.txt", 'a')
            op2.write(f'\n{x} {passwordCheck}')
            op2.close()
            break
        else:
            i+=1
    print("Your ID Number is:",x)
    op1 = open("Shop_Owner_Address.txt", 'a')
    op1.write(f"\n{x} {Input_Name} +880{Input_PhoneNumber} {Input_address}")
    op1.close()
    with open("Shop_Owner_ID.txt" , 'a') as op:
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

def account():#account have or not
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
with open("Shop_Owner_ID.txt" , 'r') as op:
    list1 = [ma.rstrip() for ma in op.readlines()]
account()