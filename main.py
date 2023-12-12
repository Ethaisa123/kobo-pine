from colorama import Fore, Back, Style
from art import *
#libraries, os, requests, colorama, art 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
tprint("> KOBO PINE")
print(Fore.GREEN +"                /\ \n               /  \ \n              /    \ \n             /      \ \n             ⎺/    \⎺ \n             /      \ \n            /        \ \n           /          \ \n           ⎺⎺/      \⎺⎺ \n            /        \ \n           /          \ \n          /            \ \n          ⎺⎺⎺⎺⎺|__|⎺⎺⎺⎺⎺ \n\n")
prCyan("     > welcome To Kobo Pine manga donwloader for Ebook and other uses")
prCyan("     > would you like to (1) download a single manga or (2) download manga using a mangadex list")
print(Fore.RED + "      > mangadex lists may take up to an hour to update after created or edited")
ans = input("\033[96m {}\033[00m" .format("     > "))

if ans == "1":
    exec(open("./manga_dld.py").read())
elif ans == "2":
    exec(open("./manga_list_dld.py").read())
