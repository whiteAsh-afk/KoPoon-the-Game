import random


# Enemy class
class Enemy:
    def __init__(self, name, hp, power, exp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power
        self.exp = exp

    def reset(self):
        self.hp = self.max_hp


enemy_list = [
    ("Slime", 20, 5, 5),
    ("Goblin", 35, 10, 10),
    ("Wolf", 50, 15, 20),
]


def random_enemy():
    enemy = random.choice(enemy_list)
    return Enemy(*enemy)
