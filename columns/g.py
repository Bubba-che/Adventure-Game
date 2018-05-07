from room import Room

one = Room('ew', coord=[6,0], items=6, desc=          #  3 pairs of items, choose one each
"""
You are in room G1.\n""")

two = Room('ew', coord=[6,1], monsters=1, desc=       #  West is large monster protected
"""
You are in room G2.\n""")

three = Room('w', coord=[6,2], monsters=1, desc=        #  Medium monster
"""
You are in room G3.\n""")

four = Room('w', coord=[6,3], special=1, desc= 
"""
You are in room G4.\n""")

five = Room('s', coord=[6,4], items=1, desc= 
"""
You are in room G5.\n""")

six = Room('new', coord=[6,5], monsters=1, desc=      #  North is small monster protected
"""
You are in room G6.\n""")