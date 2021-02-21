import sqlite3
from tabulate import tabulate
import string
import secrets
import pyperclip
import os
import pyAesCrypt
import base64
import time
import subprocess
from getpass import getpass

def clearscreen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


clearscreen()

buffersize = 64 * 1024
coded_str = "Your Master Password Goes here"
z = base64.b64decode(coded_str).decode('utf-8')
print("""

 _____ _           _        _____                             _    _____                              .-""-_
|   __|_|_____ ___| |___   |  _  |___ ___ ___ _ _ _ ___ ___ _| |  |     |___ ___ ___ ___ ___ ___     / .--...}
|__   | |     | . | | -_|  |   __| .'|_ -|_ -| | | | . |  _| . |  | | | | .'|   | .'| . | -_|  _|   / /    |.|
|_____|_|_|_|_|  _|_|___|  |__|  |__,|___|___|_____|___|_| |___|  |_|_|_|__,|_|_|__,|_  |___|_|     | |    | |
              |_|                                                                   |___|           | |.-""-.|
    Version 1.0                                                                                    ///`.::::. `.
    Developed by:                                                                                 ||| ::/  \::;|
    Amit Padmakar Kadam                                                                           |||;::\__/::;|
                                                                                                   ||  '::::' ./
--------------------------------------------------------------------------------------------         `=':-..-'`   
""")
x = getpass("\n \t\t\t--------------------ENTER MASTER PASSWORD--------------------\n[*]")
while x != z:
    clearscreen()
    x = getpass("\n \t\t\t--------------------WRONG PASSWORD,TRY AGAIN--------------------\n[*]")
else:
    try:
        pyAesCrypt.decryptFile("data1.db.aes", "data1.db", z, buffersize)
        os.remove("data1.db.aes")
        conn = sqlite3.connect('data1.db')
        print("\n \t[*] LOGIN SUCCESSFUL"
              "\n \t[*] DATABASE CONNECTION SUCCESSFUL")
        try:
            cmd1 = "Processchecker.exe"
            subprocess.Popen(cmd1)
            cmd2 = "timechecker.exe"
            subprocess.Popen(cmd2)
        except:
            print("\n \t[*] Processchecker.exe or timechecker is MISSING")
            time.sleep(5)
            exit()
        time.sleep(0.5)
    except:
        try:
            print("\n\n \t[*] Searching Database")
            pyAesCrypt.encryptFile("data1.db", "data1.db.aes", z, buffersize)
            os.remove("data1.db")
            print("[*](Database Found) & was left UnEncrypted ")
            time.sleep(1)
            print("\n[*]Please use (EXIT option only!), to quit the program")
            time.sleep(2)
            print("\n[*]Please Relaunch program")
            time.sleep(2)
            quit()
        except:
            print("\n[*]Database not found. Ignore this message if (DATABASE FOUND) message is displayed earlier")
            input("\n[*]Press any key to QUIT\n")
            quit()

    clearscreen()
    print("""

 _____ _           _        _____                             _    _____                              .-""-_
|   __|_|_____ ___| |___   |  _  |___ ___ ___ _ _ _ ___ ___ _| |  |     |___ ___ ___ ___ ___ ___     / .--...}
|__   | |     | . | | -_|  |   __| .'|_ -|_ -| | | | . |  _| . |  | | | | .'|   | .'| . | -_|  _|   / /    |.|
|_____|_|_|_|_|  _|_|___|  |__|  |__,|___|___|_____|___|_| |___|  |_|_|_|__,|_|_|__,|_  |___|_|     | |    | |
              |_|                                                                   |___|           | |.-""-.|
    Version 1.0                                                                                    ///`.::::. `.
    Developed by:                                                                                 ||| ::/  \::;|
    Amit Padmakar Kadam                                                                           |||;::\__/::;|
                                                                                                   ||  '::::' ./
--------------------------------------------------------------------------------------------         `=':-..-'`   
""")


def mainmenu():
    print("\n\t\t[*]  SIMPLE PASSWORD MANAGER v1.0 BETA \n\t\t[*]  Developed by Amit Padmakar Kadam")
    print("\n[*] SELECT AN OPTION TO PROCEED")
    option = (input("\n\t[1] Show all entries "
                    "\n\t[2] Search by Site Name "
                    "\n\t[3] Perform Create,Update,Delete operations "
                    "\n\t[4] Create a complex password "
                    "\n\t[5] Perform manual database encryption  "
                    "\n\t[6] Exit \n [~]: "))

    if option == '1':
        selectall()
        back = input("\n [0] Go Back \n[*] ")
        if back == '0':
            mainmenu()
        else:
            clearscreen()
            print(
                "\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
            mainmenu()
    elif option == '2':
        searchsite()
    elif option == '3':
        clearscreen()
        CRUD()
    elif option == '4':
        complexpassword()
    elif option == '5':
        try:
            conn.close()
            pyAesCrypt.encryptFile("data1.db", "data1.db.aes", z, buffersize)
            os.remove("data1.db")
        except:
            print("Database not found")
    elif option == '6':
        exit()

    else:
        clearscreen()
        print("\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()


def selectall():
    print("option")
    c = conn.cursor()
    c.execute("""select ID,site,username from passwords;""")
    data = (c.fetchall())
    header = ['ID', 'SITE', 'USERNAME']
    print(tabulate(data, headers=header, tablefmt='psql'))
    x = str(input("[1] Copy Pass: \n"
                  "[0] Go Back: \n[*] "))

    if x == '0':
        clearscreen()
        mainmenu()
    elif x == '1':
        copypass()
    else:
        clearscreen()
        print("\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()


def copypass():
    c = conn.cursor()
    try:
        search = input("[*] Enter ID : ")
        c.execute("""select password from passwords where ID is ?""",(search))
        pyperclip.copy((c.fetchone()[0]))
        print("\n[*] Password has been copied to clipboard")
        conn.commit()
    except:
        print("\n[*] INVALID INPUT")
    x = str(input("[0] Go Back: \n[*] "))
    if x == '0':
        mainmenu()
    else:
        clearscreen()
        print("\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()


def searchsite():
    search = input("Enter site name : ")
    c = conn.cursor()
    c.execute("""select * from passwords where site like ?""",(search))
    query = (c.fetchall())
    header = ['ID', 'SITE', 'USER NAME']
    print(tabulate(query, headers=header, tablefmt='psql'))
    conn.commit()
    x = str(input("[1] Copy Pass: "
                  "[0] Go Back: \n[*] "))
    if x == '0':
        mainmenu()
    elif x == '1':
        copypass()
    else:
        clearscreen()
        print("\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()


def create():
    try:
        sitename = input("Enter site name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        c = conn.cursor()
        c.execute("insert into passwords ('site','username','password') values(?, ?, ?);",(sitename, username, password))
        c.execute("""select * from passwords where site is ? AND username is ? AND password is ?;""",(sitename,username,password))
        query = (c.fetchall())
        clearscreen()
        header = ['ID', 'SITE', 'USER NAME', 'PASSWORD']
        print(tabulate(query, headers=header, tablefmt='psql'))
        conn.commit()
    except:
        clearscreen()
        print("\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()
    x = str(input("[0] Go Back:\n[*]  "))
    if x == '0':
        clearscreen()
        mainmenu()
    else:
        clearscreen()
        print(
            "\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()


def update():
    try:
        c = conn.cursor()
        c.execute("""select ID,site,username from passwords;""")
        query = (c.fetchall())
        header = ['ID', 'SITE', 'USER NAME']
        print(tabulate(query, headers=header, tablefmt='psql'))
        conn.commit()
        selectid = input("Select ID : ")
        sitename = input("Enter site name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        c.execute(
            """update passwords set site = ?, username = ?, password = ? where ID = ? ;""",(sitename,
                                                                                                            username,
                                                                                                            password,
                                                                                                            selectid))
        c.execute(
            """select * from passwords where site is ? AND username is ? AND password is ?;""",(sitename,
                                                                                                               username,
                                                                                                               password))
        query = (c.fetchall())
        header = ['ID', 'SITE', 'USER NAME', 'PASSWORD']
        print(tabulate(query, headers=header, tablefmt='psql'))
        conn.commit()

    except:
        clearscreen()
        print("\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()
    x = str(input("[0] Go Back:\n[*]  "))
    if x == '0':
        clearscreen()
        mainmenu()
    else:
        clearscreen()
        print(
            "\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()

def delete():
    try:
        c = conn.cursor()
        c.execute("""select ID,site,username from passwords;""")
        query = (c.fetchall())
        header = ['ID', 'SITE', 'USER NAME']
        print(tabulate(query, headers=header, tablefmt='psql'))
        selectid = input("Select ID : ")
        c.execute("""delete from passwords where ID = ?;""",(selectid, ))
        print("\n\tRECORD DELETED")
        conn.commit()


    except:
        clearscreen()
        print("\n\t\t\t[*] --------------------------------------INVALID INPUT------------------------------------------")
        mainmenu()
    x = str(input("[0] Go Back: \n[1] Delete another record\n[*] "))
    if x == '0':
        clearscreen()
        mainmenu()
    else:
        clearscreen()

        delete()


def CRUD():
    CrudOption = input("\n\tSELECT AN OPTION TO PROCEED"
                       "\n\t[1] Create a new record"
                       "\n\t[2] Update a record"
                       "\n\t[3] Delete a record"
                       "\n\t[4] Go Back "
                       "\n [~]: ")
    if CrudOption == "1":
        create()
    elif CrudOption == "2":
        update()
    elif CrudOption == "3":
        delete()
    elif CrudOption == "4":
        if CrudOption == 0:
            mainmenu()
        else:
            clearscreen()
            print(
                "\n[*]--------------------------------------INVALID INPUT------------------------------------------")
            mainmenu()


def complexpassword():
    while True:
        try:
            length = int(input("[*] Please Enter The Length Of Your Password :  "))
            special_char = ("!#$%&'*+,-./:;<=>?@[\]^_`{|}~")
            char = string.ascii_letters + string.digits + special_char
            password = "".join(secrets.choice(char) for i in range(length))
            print("[*] Password : " + password + " Has been copied to clipboard")
            pyperclip.copy(password)
            break
        except:
            print(
                "\n[*]-------------------------------------- INVALID ENTRY ------------------------------------------")
            mainmenu()
    back = input("[0] Go Back: \n[*] ")
    if back == 0:
        mainmenu()
    elif back == '0':
        mainmenu()


def exit():
    try:
        c = conn.cursor()
        c.close()
        conn.close()
        pyAesCrypt.encryptFile("data1.db", "data1.db.aes", z, buffersize)
        os.remove("data1.db")
    except:
        print("Database already encrypted")
        time.sleep(2)

    print("\n[*]----------------------------------------------QUITING--------------------------------------------------")
    time.sleep(0.4)
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
    quit()



# MAIN ROUTINE

mainmenu()
