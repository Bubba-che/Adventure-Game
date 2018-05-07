from room import Room

one = Room('sw', coord=[1,0], desc=                     #  Room 1
"""
You are in room B1.\n""")

two = Room('nse', coord=[1,1], monsters=2, desc=        #  Tiny monsters; Room 1
"""
You are in room B2.\n""")

three = Room('nsw', coord=[1,2], monsters=2, desc=        #  Tiny monsters; Room 1
"""
You are in room B3.\n""")

four = Room('ns', coord=[1,3], monsters=1, desc=         #  Tiny monster
"""
You are in room B4.\n""")

five = Room('nsew', coord=[1,4], desc=                   #  East is secret; Room 2        
"""
You are in room B5.\n""")

six = Room('nw', coord=[1,5], monsters=1, desc=         #  Medium monster; Room 2
"""
You are in room B6.\n""")