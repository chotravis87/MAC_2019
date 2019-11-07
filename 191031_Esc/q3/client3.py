from socket import *
import time
import os

clear = lambda: os.system('clear')
clear()
print('''Welcome\n\n\n''')

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

while True:
    try:
        ans1 = input('''Enter First Two Digits Number: ''')
        temp = int(ans1)
        if not len(ans1) == 2:
            print("Only Two Digits Number")
            print()
            time.sleep(1.5)
            continue
    except ValueError:
        print("Only Integer Accepted")
        time.sleep(1.5)
        continue
    else:
        clientSock.send(ans1.encode('utf-8'))
    
    try:
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
    
    if (ans1 == '21' and ans2 == '35') or (ans1 == '35' and ans2 == '21') :
        print()
        print("NO CHEATING!")
        print()
        continue
    print(ans1 + ' ? ' + ans2 + ' =')
    print("Sent")
    print()
    time.sleep(1.5)


