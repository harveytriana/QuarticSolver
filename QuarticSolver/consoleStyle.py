#===================================
# harveytriana@gmail.com
# Twitter: @__harveyCS__
#===================================
import os

clear = lambda: os.system('cls')

from colorama import init, Fore, Style
init(autoreset = True, convert = True)

clear()

def Gray(text): print(text)

def Green(text): print(Fore.GREEN + text)

def Red(text): print(Fore.RED + Style.BRIGHT + text)

def Yellow(text): print(Fore.YELLOW + Style.BRIGHT + text)
 