from prompt import prompt


def movement(directions):
    """Movement things!"""

    if type(directions) != str:
        print("Error: ment() was passed an invalid argument (not a str).")
        exit(0)

    north = ['North', 'north', 'Up', 'up', 'N', 'n', 'U', 'u']
    south = ['South', 'south', 'Down', 'down', 'S', 's', 'D', 'd']
    east = ['East', 'east', 'Right', 'right', 'E', 'e', 'R', 'r']
    west = ['West', 'west', 'Left', 'left', 'W', 'w', 'L', 'l']

    while True:

        answer = prompt('feedback')

        if 'n' in directions and answer in north:
            aim = 'n'
            break
                
        elif 's' in directions and answer in south:
            aim = 's'
            break
                    
        elif 'e' in directions and answer in east:
            aim = 'e'
            break
                
        elif 'w' in directions and answer in west:
            aim = 'w'
            break
                
        else:
            print("\n\tYou can't go that way...\n")
        
    return aim