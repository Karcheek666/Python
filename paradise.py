from time import sleep
from colorama import init, Fore
import os as os

os.system("mode con cols=1920 lines=1080")
init()

x = int(input('Enter the PIN: '))
y = 1
time_int = 0.14
try:
    if x >= 100:
        for r in range(x):
            # print("\033\n")
            stroll = str(y*(' 1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0'))
            troll = str(y*(' 0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1'))
            print(Fore.GREEN, stroll)
            sleep(time_int)
            print(Fore.GREEN, troll)
            sleep(time_int)
    else:
        print('Wrong PIN, try again! \nHint: Atleast a three digit one...')
except ValueError as ve:
    print("It's a PIN! You nuts?!")

finally:
    print('\nCREDITS: CannedShroud -->    github.com/v0iid')
