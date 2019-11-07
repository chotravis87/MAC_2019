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
    ans = int(temp1) % 7
    print("Answer: " + str(ans))
    print()
    time.sleep(1.5)
