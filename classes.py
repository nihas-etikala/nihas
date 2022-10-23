class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


bddhdh = Point()
bddhdh.x = 10
bddhdh.y = 20
bddhdh.draw()
point2 = Point()
point2.x = 1
point2.y = 2
print(bddhdh)
print(point2)
print(bddhdh.x)
print(bddhdh.y)
print(point2.x)
print(point2.y)
print(type(point2.x))
