from time import sleep
from random import randint

file = open("prompts.txt")
txt = file.read()
quips = txt.split(sep='\n')

def prompt(use):
    
    if use == 'feedback':
        return input(f"|{quips[randint(1,len(quips)) - 1]}|› ")     
    elif use == 'enter':
        input("\n\t...\n")
    elif use == 'wait':
        for i in range(0, 6):
            for i in ['/', '-', '\\', '|']:
                print(' ', '%s\r' % i, end = '')
                sleep(0.08)
    else:
        print("Error. Improper or missing value for prompt().")
        exit(0)