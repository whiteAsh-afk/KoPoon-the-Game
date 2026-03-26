import random


# Enemy class
class Enemy:
    def __init__(self, name, hp, attack, exp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.exp = exp

    def reset(self):
        self.hp = self.max_hp

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0


enemy_list = [
    ("Slime", 20, 5, 5),
    ("Goblin", 35, 10, 10),
    ("Wolf", 50, 15, 20),
]


def random_enemy():
    enemy = random.choice(enemy_list)
    return Enemy(*enemy)
