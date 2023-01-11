class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7


def fight(fighter1, fighter2):
    while True:
        fighter2.health -= fighter1.attack
        if fighter2.health <= 0:
            fighter2.is_alive = False
            return (True)
        fighter1.health -= fighter2.attack
        if fighter1.health <= 0:
            fighter1.is_alive = False
            return (False)


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()