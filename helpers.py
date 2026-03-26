import os
import time


# clear the battle screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def wait():
    time.sleep(2)
