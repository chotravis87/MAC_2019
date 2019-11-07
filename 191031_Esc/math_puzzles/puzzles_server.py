from socket import *
import time
import os
clear = lambda: os.system('clear')

clear()
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)
print("Waiting")
connectionSock, addr = serverSock.accept()

while True:
    print("Waiting")
    tmp = connectionSock.recv(1024)
    temp1 = tmp.decode('utf-8')
    tmp2 = connectionSock.recv(1024)
    temp2= tmp2.decode('utf-8')
    if (temp1 == '21' and temp2 == '35') or (temp1 == '35' and temp2 == '21'):
        print('''NO CHEATING!''')
        print()
        continue
    if (temp1 == '24' and temp2 == '24') or (temp1 == '24' and temp2 == '24'):
        break
    ans1 = int(temp1[0]) + int(temp1[1])
    ans2 = int(temp2[0]) + int(temp2[1])
    ans = ans1 * ans2
    print(ans)
    print()
    time.sleep(1.5)

print("PASS!")
serverSock.connect(('127.0.0.1', 8081))
a = 'r4 1'
serverSock.send(a.encode('utf-8'))
