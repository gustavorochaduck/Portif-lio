import random

userAntwort = input('Wählen Sie eine Zahl bis 100: ')
programAntwort = int(random.uniform(1,100))
print('-=-'*20)

if programAntwort == userAntwort:
    print(f'\nRichtige Antwort!!!\nAntwort: {programAntwort}')

if programAntwort != userAntwort:
    print(f'Falsche Antwort!!!\nAntwort: {programAntwort}')

else:
    print('ERROR!!!')