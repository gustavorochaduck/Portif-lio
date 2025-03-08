import os
import time

os.system('cls' if os.name == "nt" else "clear")
print('Options:')
print('\n[+] - 1')
print('[-] - 2')
print('[*] - 3')
print('[/] - 4')
print('\nEXIT - 9')
print('-=-'*20)
userSelect = int(input('Select: '))
os.system('cls' if os.name == "nt" else "clear")

userNum1 = float(input('First Number: '))
userNum2 = float(input('Second Number: '))
os.system('cls' if os.name == "nt" else "clear")

if userSelect == 1:
    print(f'The Anwser is: {userNum1+userNum2}')

elif userSelect == 2:
    print(f'The Awnser is: {userNum1-userNum2}')

elif userSelect == 3:
    print(f'The Awnser is: {userNum1*userNum2}')

elif userSelect == 4:
    print(f'The Awnser is: {float(userNum1/userNum2)}')

else:
    print('ERROR!!!')

input('Type Enter to Close the Program: ')
os.system('cls' if os.name == "nt" else "clear")
