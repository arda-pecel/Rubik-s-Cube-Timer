////////////////////////////////////////
/*
   Author: Arda Peçel
   Project: Rubik's Cube timer
   Date: 01.03.2019
   Version: v0.2
*/
////////////////////////////////////////

import random
from timeit import default_timer as timer

while 1:
    try:
        customer_file = open('users.txt', 'r')
    except:
        print("Account can not found!")

    print("Login or Sign-up!")
    login = input()
    userlist = []
    usernames = []
    userid = []
    userpass = []

    data = customer_file.read()
    userlist = data.split(";")
    userlist.pop(-1)
    for veri in userlist:
        usernames.append(veri.split("&"))
    for veri in usernames:
        userid.append(veri[0])
    for veri in usernames:
        userpass.append(veri[1])

    if login.lower() == "login":
        isim = input("Enter your name= ")
        if isim in userid:
            password = input("Enter yor password= ")
            sirano = userid.index(isim)
            if userpass[sirano] == password:
                print("Login Successful " + isim)
                devam = input("Start or delete account? ").lower()
                while devam not in ["delete", "start"]:
                    devam = input("Choose one of them!").lower()
                if devam == "delete":
                    hedef_id = userid.index(isim)
                    userlist.pop(hedef_id)
                    userlist_str = ";".join(userlist)
                    userlist_str += ";"
                    try:
                        customer_file = open('users.txt', 'w+')
                    except:
                        print("Account can not found!")

                    customer_file.write(userlist_str)
                    customer_file.close()
                    print("Your account has been deleted!")
                    continue

            else:
                print("Wrong password!")
                continue
        else:
            print("Check your name or Sign-up!")
            continue

    elif login.lower() == "signup":
        try:
            customer_file = open('users.txt', 'a')
        except:
            print("Account can not found!")
        name = input("Your name= ")
        if name in userid:
            print("This name is usen already!")
            continue
        else:
            sifre = input("Choose your password= ")
            print("Your account has been created!")
            data = str(name + "&" + sifre + ";")
            customer_file.write(data)
            customer_file.close()

    else:
        print("Choose one of them!")
        continue

    while(1):
        c = int(input('Number of solutions='))
        lenght = int(input("lenght of scrambles="))
        print('****************')

        a = []
        i = 0
        b = []
        for i in range(c):

            scramble = ""
            d = {'F': 'F', 'R': 'R', 'U': 'U', 'B': 'B', 'L': 'L', 'D': 'D',
                 'F\'': 'F\'', 'R\'': 'R\'', 'U\'': 'U\'', 'B\'': 'B\'', 'L\'': 'L\'', 'D\'': 'D\''}
            for c in range(lenght):
                scramble += random.choice(list(d.keys()))
            print('Scramble= ' + scramble)
            input("Click for start the timer=")
            start = timer()

            int(input("Click for stop the timer="))

            end = timer()

            b.append(end - start)
            print(i + 1, ". time is=", b[i])
            print("------------------")
        for index, deger in enumerate(b):
            print(index + 1, ". time is=", deger)

        print(isim + "\'s average of", len(b), "is:")
        print((sum(b) - max(b) - min(b)) / (len(b) - 2))
        last = input("Restart or Log out!")
        if last.lower() == "restart":
            continue

        elif last.lower() == "logout":
            exit()
