
#pip install mysql-connector-python

import mysql.connector
import time as t


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="atm"

    )


def init_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS users(
                id INT AUTO_INCREMENT PRIMARY KEY,
                card_number VARCHAR(20) UNIQUE,
                pin INT,
                balance DOUBLE DEFAULT 0
                
                ) """)
    conn.commit()
    conn.close()


def register_user():
    conn = connect_db()
    cur = conn.cursor()
    card_number = input("Enter a New Card Number...")
    pin = int(input("Set a 4-digit PIN..."))
    balance =  float(input("Enter Initial deposit amount.."))

    try:
        cur.execute("INSERT INTO users (card_number, pin, balance) VALUES (%s, %s, %s)",
                    (card_number, pin, balance))
        conn.commit()
        print("✅Account Created Successfully...\n")

    except mysql.connector.IntegrityError:
        print("❌ Card number already exists. Try again.\n")
    conn.close()


def login_user():
    conn = connect_db()
    cur = conn.cursor()
    card_number = input("Enter your card number: ")
    pin = int(input("Enter your 4-digit PIN: "))

    cur.execute("SELECT * FROM users WHERE card_number=%s AND pin=%s", (card_number, pin))
    user = cur.fetchone()
    conn.close()

    if user:
        print("\n✅ Login SuccessFull")
        return user
    else:
        print("❌Invalid card number or PIN.\n")
        return None




def main_menu(user):
    while True:

        print("\t0 Logout or Exit")

        print("\t1 View Account Balance")
        print("\t2 Withdrawn Amount")
        print("\t3 Deposit Amount")
        print("\t4 PIN Change")
        print("\t5 Return Card")
        

        choice = int(input("Enter a Number to Proceed...😎"))
        print("\n")

        if choice == 0:
            print("Exiting....")
            t.sleep(2)
            print("You Have Been Logged Out...😒")
            print("\n")
            print("\n")
            break

       
        if choice == 1:
            Account_Balance(user)
        elif choice == 2:
            Withdrawn_Amount(user)
        elif choice == 3:
            Deposit_Amount(user)
        elif choice == 4:
            Pin_change(user)
        elif choice == 5:
            Return_Card()
        else:
            print("Invalid Input...")





def Account_Balance(user):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT balance FROM users where id=%s", (user[0],))
    balance = cur.fetchone()[0]

    print("Loading Account Balance")
    t.sleep(2)
    print(f"Your Account Balance is {balance}")
    print("\n")

def Withdrawn_Amount(user):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT balance FROM users where id=%s", (user[0],))
    balance = cur.fetchone()[0]

    print("Loading Withdrawn Amount..")
    t.sleep(2)
    
   
    with_amount = float(input("Enter a amount to withdrawn..."))
    # allow withdrawing up to the current balance
    if with_amount > balance:
        print("❌Insufficeient Balance\n")
    else:
        confirm = input("Confirm Y/N..")
        if confirm in ('Y', 'y'):
            new_balance = balance - with_amount
            # removed stray comma before WHERE
            cur.execute("UPDATE users SET balance=%s WHERE id=%s", (new_balance, user[0]))
            conn.commit()
            print(f"✅ Withdrawn ₹{with_amount}. Remaining balance: ₹{new_balance}\n")
        else:
            print("Transcation Cancelled..\n")
    conn.close()




def Deposit_Amount(user):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT balance FROM users WHERE id=%s", (user[0],))
    balance = cur.fetchone()[0]

    print("Loading Depsoit Amount")
    t.sleep(2)
    dept_amount = int(input("Enter a Amount to Deposit....😎😎"))
    print("Depositing Amount...")
    t.sleep(2)
    confirm = input("Confirm Y/N..")
    if confirm in ('Y', 'y'):
        new_balance = balance + dept_amount
        cur.execute("UPDATE users SET balance=%s WHERE id=%s", (new_balance, user[0]))
        conn.commit()
        print(f"✅ Deposited ₹{dept_amount}. New balance: ₹{new_balance}\n")
    else:
        print("Transaction Cancelled.\n")
    conn.close()

    

    
    

def Pin_change(user):
    conn = connect_db()
    cur = conn.cursor()
    print("Loading Pin change")
    t.sleep(2)

    new_pin = int(input("Enter a New PIN.."))
    print(f"Changing Pin to {new_pin}")
    confirm = input("Confirm Y/N..")
    if confirm in ('Y', 'y'):
       cur.execute("UPDATE users SET pin=%s WHERE id=%s", (new_pin, user[0]))
       conn.commit()
       print("✅ PIN changed successfully.\n")
       conn.close()
    else:
        print("Cancelling Transcation...😒😒")
        t.sleep(2)
        print("Transcation Cancelled..")
        print("\n")
    


def Return_Card():
    print("Loading Return Card")
    t.sleep(2)

    print("Returning Your ATM Card")

    confirm = input("Confirm Y/N..")
    if confirm in ('Y', 'y'):
        print("Card Returned Successfully...")
        t.sleep(2)
        print("Thank You")
        print("\n")
    else:
        print("Cancelling Transcation...😒😒")
        t.sleep(2)
        print("Transcation Cancelled..")
        print("\n")




def main():
    init_db()

    while True:
        print("=======ATM APPLICATION=======")
        print("1. Register New User")
        print("2. Login to Existing User")
        print("0. Exit")
        print("================")


        try:
            option = int(input("Enter an option..."))
        except ValueError:
            print("Invalid Input. Please ente a number..\n")
            continue
            
        if option == 1:
            register_user()
        elif option == 2:
            user = login_user()
            if user:
                main_menu(user)
        elif option == 0:
            break
        else:
            print("Invalid Input")


main()