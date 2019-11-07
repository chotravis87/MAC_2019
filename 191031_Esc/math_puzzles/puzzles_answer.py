import os
from time import sleep
from socket import *

clear = lambda : os.system('clear') #Clear Function

#Initialized with clearing screen
clear()
leftatt = 3 #도전 횟수
userans = "0" #사용자의 정답
ans1 = "24" #문제 정답
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8081))

while(1):
    print("Question 4")
    print("Enter the answer(LIFE : {})\n".format(leftatt))
    x=input("Answer : ")
    try:
        if (int(x) == int(ans1)):
          print("\nChecking the answer...please wait")
          sleep(2)
          print("\nYou are right!")
          break

        else:
          print("\nChecking the answer...please wait")
          sleep(2)
          print("\nYou are wrong")
          sleep(2)
          leftatt -= 1
          clear()
          if (leftatt == 0):
            break
          continue
    except Exception:
        sleep(2)
        print("\nYou can only write numbers. Please try again")
        sleep(2)
        clear()
        continue
    

if (leftatt == 0):
    print("GAME OVER")
else:
    ans = 'r4 1'
    clientSock.send(ans.encode('utf-8'))
    print("\nPlease go to the next stage")
