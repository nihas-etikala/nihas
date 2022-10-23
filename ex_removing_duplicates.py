numbers = [6, 5, 9, 7, 6, 5, 7, 8, 9, 6, 5]
b = numbers.copy()
for a in numbers:
    if numbers.count(a) != 1:
        b.remove(a)
        numbers = b

print(b)

# print(list(set(numbers)))