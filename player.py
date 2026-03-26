class Player:
    def __init__(self):
        self.x = 2
        self.y = 2
        self.hp = 100
        self.attack = 20

    def move(self, dx, dy, map):
        new_x = self.x + dx
        new_y = self.y + dy

        if map[new_x][new_y] == "#":
            return

        self.x = new_x
        self.y = new_y

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0
