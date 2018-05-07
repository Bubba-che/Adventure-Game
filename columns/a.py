from room import Room

one = Room('se', coord=[0,0], puzzles=2, items=1, desc=   #  Puzzle-protected item; Room 1
"""                         
You are in room A1.\n""")

two = Room('ns', coord=[0,1], monsters=2, desc=           #  Tiny monsters; Room 1
"""
You are in room A2.\n""")

three = Room('ne', coord=[0,2], special=1, desc=          #  Room 1
"""
You are in room A3.\n""")

four = Room('s', coord=[0,3], items=1, desc=              #  Key
"""
You are in room A4.\n""")

five = Room('nse', coord=[0,4], puzzles=1, desc=          # Puzzle-protected North; Room 2
"""
You are in room A5.\n""")

six = Room('ne', coord=[0,5], monsters=1, desc=           # Medium monster; Room 2
"""
You are in room A6.\n""")