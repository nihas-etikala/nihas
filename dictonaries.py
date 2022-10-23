customer = {
    "name": "john Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get('gender'))
# .get wont say error it just shows none if the string is absent
customer["birthdate"] = "dec 1 2004"
print(customer)


# exercise:number to numbers in words
phone = input("phone: ")
numbers = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}
output = ""
for key in phone:
    output += numbers.get(key) + ' '
print(output)


