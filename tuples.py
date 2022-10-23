# tuples = un changeable lists
numbers = (1, 2, 3)
print(numbers.count(2))
print(numbers.index(2))
# UNPACKING:
coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#  the above 3 lines can be written in a single line(this is valid even for lists):
x, y, z = coordinates
print(x)

