from art import *
import os, sys
#libraries, os, requests, colorama, art 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

def prCyan(skk): print("\033 {}\033" .format(skk))
tprint(" KOBO PINE")
print("                /\ \n               /  \ \n              /    \ \n             /      \ \n             ⎺/    \⎺ \n             /      \ \n            /        \ \n           /          \ \n           ⎺⎺/      \⎺⎺ \n            /        \ \n           /          \ \n          /            \ \n          ⎺⎺⎺⎺⎺|__|⎺⎺⎺⎺⎺ \n\n")
print("     > welcome To Kobo Pine manga donwloader for Ebook and other uses")
print("     > would you like to (1) download a single manga or (2) download manga using a mangadex list")
print("     > mangadex lists may take up to an hour to update after created or edited")
ans = input("{}" .format("    > "))
if ans == "1":
    filename = os.path.join(os.path.dirname(sys.executable), 'manga_dld.py')
    exec(open(filename).read())
elif ans == "2":
    filename = os.path.join(os.path.dirname(sys.executable), 'manga_list_dld.py')
    exec(open(filename).read())
