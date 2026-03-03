import random


def dobbel():
    rol1 = random.randint(1, 6)
    rol2 = random.randint(1, 6)
    if rol1 == rol2:
        print(f"Gewonnen! Je hebt 2x {rol1} gerold.")
    else:
        print(f"Verloren, Je hebt een {rol1} en een {rol2} gerold.")