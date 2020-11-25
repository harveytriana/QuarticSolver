# ===================================
# harveytriana@gmail.com
# Twitter: @__harveyt__
# ===================================
from colorama import init, Fore, Style
import os


def clear(): return os.system('cls')


init(autoreset=True, convert=True)

clear()


def Gray(text): print(text)


def Green(text): print(Fore.GREEN + text)


def Red(text): print(Fore.RED + Style.BRIGHT + text)


def Yellow(text): print(Fore.YELLOW + Style.BRIGHT + text)
