from time import sleep

from movement import movement


class Room(object):
    """Contains information regarding rooms"""


    def __init__(self, exits, coord, monsters = 0, items = 0, puzzles = 0,
                 special = 0, desc = "YOU FORGOT TO ADD A DESCRIPTION"):
        
        self.desc = desc
        self.exits = exits
        self.coord = coord
        self.monsters = monsters
        self.items = items
        self.puzzles = puzzles
        self.special = special
        self.counter = 0 # The number of times the player has been in this room



    def enter(self):         # Create an if statement for items, monsters, etc.
        for i in range(0, len(self.desc)):
            print(self.desc[i], end='', flush=True)
            sleep(.03)
        self.inc_counter()
        self.move()      

    def inc_counter(self):
        self.counter += 1

    def move(self):
        from grid import grid

        self.direction = movement(self.exits)
        if self.direction == 'n':
           grid([self.coord[0], self.coord[1] - 1]).enter()
        elif self.direction == 's':
           grid([self.coord[0], self.coord[1] + 1]).enter()
        elif self.direction == 'e':
           grid([self.coord[0] + 1, self.coord[1]]).enter()
        elif self.direction == 'w':
           grid([self.coord[0] - 1, self.coord[1]]).enter()
        else:
            print("Error: Room.move() was passed an invalid argument.")
            exit(0)


    def get_desc(self):
        return self.desc

    def get_exits(self):
        return self.exits

    def get_coord(self):
        return self.coord

    def get_monsters(self):
        return self.monsters

    def get_items(self):
        return self.items    

    def get_puzzles(self):
        return self.puzzles

    def get_special(self):
        return self.special

    def get_counter(self):
        return self.counter


    
    def change_desc(self, str):
        self.desc = str
    
    def change_exits(self, str):
        self.exits = str
    
    def change_monsters(self, int):
        self.monsters = int
    
    def change_items(self, int):
        self.items = int
    
    def change_puzzles(self, int):
        self.puzzles = int
    
    def change_special(self, int):
        self.special = int

    

