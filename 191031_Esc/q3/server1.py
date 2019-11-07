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
    temp = connectionSock.recv(1024)
    temp1 = temp.decode('utf-8')
    b = int(temp1[0]) + int(temp1[1]) + int(temp1[2])
    f = int(temp1[0]) * int(temp1[1]) * int(temp1[2])
    ans = str(f) + str(b)
    print("Answer: " + ans)
    print()
    time.sleep(1.5)
