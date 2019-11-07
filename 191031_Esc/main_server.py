from socket import *
import time
import os
clear = lambda: os.system('clear')

r2 = False
r3 = False
r4 = False
r5 = False

def status():
    clear()
    print("""\
            Room 2, Password = {}
            Room 3, Shape = {}
            Room 4, Math Quiz = {}
            Room 5, Rush Hour = {}\
                """.format(r2, r3, r4, r5))
    print("Listening")
   
status()

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8081))
serverSock.listen(1)


    

    

def soc():
    connectionSock, addr = serverSock.accept()
    ans = connectionSock.recv(1024)
    a = ans.decode('utf-8')
    a = a.split(' ')
    print(a)
    if a[0] == 'r2' and a[1] == '1':
        return True
    if a[0] == 'r3' and a[1] == '1':
        return True
    if a[0] == 'r4' and a[1] == '1':
        return True
    if a[0] == 'r5' and a[1] == '1':
        return True
    
while 1:
    status()
    r2 = soc()
    status()
    r3 = soc()
    status()
    r4 = soc()
    status()
    r5 = soc()
    
    
        

