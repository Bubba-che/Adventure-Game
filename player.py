class Player(object):

    def __init__(self, position, inventory, hp, lck, atk, xp, lvl):
        
        self.position = position
        self.inventory = ["dead cell chone", "pocket lint", "a five dollar bill"]
        self.hp = hp
        self.lck = lck
        self.atk = atk
        self.xp = xp
        self.lvl = lvl  #  Levels are meaningless (social experiment)
