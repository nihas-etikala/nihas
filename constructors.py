class Point:
    def __init__(self, x, y):
        self.dfhdh = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point = Point(10, 20)
print(point.dfhdh)

# ----------------------------------------------------------------------
class Person:
    def __init__(self, name,):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')

nihas = Person("pandu")
nihas.talk()
print(nihas.name)


