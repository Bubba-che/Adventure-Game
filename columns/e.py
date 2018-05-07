from room import Room

one = Room('s', coord=[4,0], items=1, desc= 
"""
You are in room E1.\n""")

two = Room('new', coord=[4,1], desc= 
"""
You are in room E2.\n""")

three = Room('sew', coord=[4,2], puzzles=1, desc=    #  West is a puzzle-protected secret
"""
You are in room E3.\n""")

four = Room('nse', coord=[4,3], desc= 
"""
You are in room E4.\n""")

five = Room('nse', coord=[4,4], desc= 
"""
You are in room E5.\n""")

six = Room('new', coord=[4,5], items=1, desc= 
"""
You are in room E6.\n""")