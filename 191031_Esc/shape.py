import os
from time import sleep
from socket import *
clear = lambda : os.system('clear')

clear()
leftatt = 3 #도전 횟수
userans = "0" #사용자의 정답
ans1 = "10" #문제 정답
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8081))

while(1):
    print("Question 1")
    print("""\
1. 정삼각형
2. 직각삼각형
3. 정사각형
4. 정오각형
5. 정육각형
6. 직사각형
7. 원
8. 사다리꼴
9. 타원
10. 별
11. 평행사변형
12. 마름모
13. 다이아몬드 모양
14. 나비넥타이
15. ㅗ 모양
16. ┌┐모양
17. ╊ 모양
18. 달 모양
19. 화살표모양
20. 하트모양\n""")
    print("Enter the answer(LIFE : {})\n".format(leftatt))
    x = input("Answer : ")
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
    ans = 'r3 1'
    clientSock.send(ans.encode('utf-8'))
    print("\nPlease go to the next stage")
