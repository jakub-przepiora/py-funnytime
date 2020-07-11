#===========================#
#======= First program =====#
#===========================#

#from random import seed
#from random import random
#from random import randint

#print( random() )


#value = randint(0, 10)
#print(value)
#print("Liczba zostala wylosowana dla Ciebie, sprobuj trafic: ")


#i = 0
#while i != 4:
#    odp = input()
#    if value == int(odp):
#        print( "niece" )
#        exit()
#    i = i + 1
#print("nie udalo sie")

#==========================#
#======= ASCII ART ========#
#==========================#

#import sys
#from colorama import init
#init (strip=not sys.stdout.isatty())
#from termcolor import cprint
#from pyfiglet import figlet_format

#cprint(figlet_format('missile!', font='starwars' ), 'yellow', 'on_red', attrs=['bold'])

print("Otwieranie pliku ...")
#afile = open("plik.txt",'r')

with open("plik.txt", 'r') as afile:
    #afile.read()
    print(afile.read(30))
    

afile.close()
