class Player:
    def __init__(self):
        self.x = 2
        self.y = 2

        self.lvl = 1
        self.exp = 0
        self.exp_to_next = 10

        self.max_hp = 100
        self.hp = self.max_hp
        self.power = 20

    # handle the player movement
    def move(self, dx, dy, map):
        new_x = self.x + dx
        new_y = self.y + dy

        # check for collision
        if map[new_y][new_x] == "#":
            return False
        self.x = new_x
        self.y = new_y
        return True

    # exp gain
    def gain_exp(self, amount):
        self.exp += amount
        while self.exp >= self.exp_to_next:
            self.lvl_up()

    # leveling system
    def lvl_up(self):
        self.lvl += 1
        self.exp -= self.exp_to_next
        self.exp_to_next = int(self.exp_to_next * 1.5)

        self.max_hp += 5
        self.power += 1

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0
