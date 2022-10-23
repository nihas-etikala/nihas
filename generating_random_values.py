import random

for i in range(3):
    print(random.random())
    print(random.randint(1, 100))
members = ['nihas', 'pandu', 'tarun']
leader = random.choice(members)
print(leader)