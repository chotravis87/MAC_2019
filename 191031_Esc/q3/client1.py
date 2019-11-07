from socket import *
import time
import os

clear = lambda: os.system('clear')
clear()
print('''Welcome\n\n\n''')

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

while True:
    ans = input('''Enter Three Digits Number: ''')
    try:
        temp = int(ans)
    except ValueError:
        print("Only Integer Accepted")
        time.sleep(1.5)
    if ans == '123':
        print()
        print("NO CHEATING!")
        print()
        continue
    if not len(ans) == 3:
        print()
        print("Only Three Digits Number")
        print()
        time.sleep(1.5)
        continue
    clientSock.send(ans.encode('utf-8'))
    print("Sent")
    print()
    time.sleep(1.5)


