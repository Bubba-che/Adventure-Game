from room import Room

one = Room('sw', coord=[7,0], desc= 
"""
You are in room H1.\n""")

two = Room('nsw', coord=[7,1], desc=       #  North is locked; south is secret
"""
You are in room H2.\n""")

three = Room('ns', coord=[7,2], desc=        #  North is secret
"""
You are in room H3.\n""")

four = Room('ns', coord=[7,3], desc= 
"""
You are in room H4.\n""")

five = Room('ns', coord=[7,4], desc= 
"""
You are in room H5.\n""")

six = Room('nw', coord=[7,5], desc= 
"""
You are in room H6.\n""")