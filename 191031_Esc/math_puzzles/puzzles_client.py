from socket import *
import time
import os

clear = lambda: os.system('clear') #Clear function (Erase command line)

#Game Initialized with clearing Screen and printing Welcome
clear() 
print('''Welcome\n\n\n''')


#Connect to Game server
clientSock = socket(AF_INET, SOCK_STREAM) #Used in TCP
clientSock.connect(('127.0.0.1', 8080)) #Connect to Local IP

#Infinite loop
while True:
    try: 
        #To prevent Error, Use try
        print('''\
                11 ? 21 = 6
                13 ? 51 = 24
                21 ? 25 = 21
                (First)21 ? (Second)35 = Answer
                Answer ?''') #Questions
        ans1 = input('''Enter First Two Digits Number: ''') #Getting Input
        temp = int(ans1) #Casting to int type
        if not len(ans1) == 2: #Digit checking
            print("Only Two Digits Number")
            print()
            time.sleep(1.5)
            continue
    except ValueError: #Exception 
        print("Only Integer Accepted")
        time.sleep(1.5)
        continue
    else: #If everything works fine, send message to server
        clientSock.send(ans1.encode('utf-8'))
    
    try: 
        #Same as before
        ans2 = input('''Enter Second Two Digits Number: ''')
        temp1 = int(ans2)
        if not len(ans2) == 2:
            print("Only Two Digits Number")
            print()
            time.sleep(1.5)
            continue
    except ValueError:
        print("Only Integer Accepted")
        time.sleep(1.5)
        continue
    else:
        clientSock.send(ans2.encode('utf-8'))
    
    #If user tries to enter the answer
    if (ans1 == '21' and ans2 == '35') or (ans1 == '35' and ans2 == '21') :
        print()
        print("NO CHEATING!")
        print()
        continue
    print(ans1 + ' ? ' + ans2 + ' =')
    print("Sent")
    print()
    time.sleep(1.5)


