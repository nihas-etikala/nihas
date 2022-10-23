import random


class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


a = 0
number_of_rolls = int(input('number of rolls: '))

while a < number_of_rolls:
    dice1 = Dice()
    a += 1
    print(dice1.roll())