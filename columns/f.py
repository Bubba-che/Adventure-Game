from room import Room

one = Room('e', coord=[5,0], monsters=1, desc=         # Final Boss
"""
You are in room F1.\n""")

two = Room('ew', coord=[5,1], desc= 
"""
You are in room F2.\n""")

three = Room('ew', coord=[5,2], monsters=1, desc=        #  West is small monster-protected
"""
You are in room F3.\n""")

four = Room('ew', coord=[5,3], desc= 
"""
You are in room F4.\n""")

five = Room('w', coord=[5,4], monsters=1, desc=         #  Small monster
"""
You are in room F5.\n""")

six = Room('ew', coord=[5,5], desc= 
"""
You are in room F6.\n""")