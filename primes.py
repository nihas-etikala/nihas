number = int(input('number: '))
initial_list = []
for p in range(2, number + 1):
    initial_list.append(p)
for numbers in range(2, number + 1):
    for divisors in range(2, int((numbers ** (1 / 2) + 1))):
        if numbers % divisors == 0 and numbers / divisors != 1:
            try:
                initial_list.remove(numbers)
            except ValueError:
                None
print(initial_list)
