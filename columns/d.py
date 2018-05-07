from room import Room

one = Room('w', coord=[3,0], puzzles=1, special=1, desc=    #  Puzzle-protected special
"""
You are in room D1.\n""")

two = Room('sew', coord=[3,1], monsters=1, desc=            #  Small monster
"""
You are in room D2.\n""")

three = Room('nse', coord=[3,2], puzzles=1, desc =          #  E is a puzzle-protected secret
"""        
You are in room D3.\n""")

four = Room('ns', coord=[3,3], desc= 
"""
You are in room D4.\n""")

five = Room('nsw', coord=[3,4], items=1, desc= 
"""
    You are surrounded by cock and balls
    of every skin tone. You rub your eyes
    and blink. Your vision focuses on a
    girthy, gleaming, black dildo. Imprinted
    on the side of the didlo is:

    STEELY DAN

    Would you like to pick it up?\n\n""")

six = Room('ne', coord=[3,5], desc=                        #  Entrance
    """
    As soon as you enter the room, you are hit
    with the overwhelming pungence of death.
    You find yourself in a hallway that stretches north.
    There is a door to the east. Where would you like to go?\n\n""")

