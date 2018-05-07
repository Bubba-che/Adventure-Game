from room import Room

one = Room('se', coord=[2,0], desc= 
"""
You are in room C1.\n""")

two = Room('new', coord=[2,1], monsters=2, desc=           #  Tiny monsters
"""
You are in room C2.\n""")

three = Room('s', coord=[2,2], items=1, puzzles=1, desc=     #  Puzzle-protected item
"""
You are in room C3.\n""")

four = Room('ns', coord=[2,3], monsters=1, desc=            #  North is monster-protected
"""
You are in room C4.\n""")

five = Room('nsew', coord=[2,4], desc=                      #  West is secret
"""
You are in room C5.\n""")

six = Room('n', coord=[2,5], monsters=1, desc=             #  Small monster
"""
You are in room C6.\n""")