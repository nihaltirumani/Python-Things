from math import sin, degrees
from random import choice
from time import sleep
from colorama import Fore, Style, Back

x=0

while True:
    if x % 2 ==0.00:
        fore = choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.BLACK])

    x += 0.01
    
    print(Style.BRIGHT + fore + Back.LIGHTWHITE_EX + "█" * abs(int(degrees(sin(x)))))
    sleep(0.01)