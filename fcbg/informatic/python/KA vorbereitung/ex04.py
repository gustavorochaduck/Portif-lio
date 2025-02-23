n1 = int(input('Erste Zahl: '))
n2 = int(input('Zweite Zahl: '))
print('-=-'*20)
if n1 == 0:
    print('\nDie Zahlen sind gleich!!!')

elif n1 >= 0:
    print(f'\n{n1} ist größer als {n2}')

elif n1 <= 0:
    print(f'\n{n2} ist größer als {n1}')

else:
    print('ERROR!!!')
