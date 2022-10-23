def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome')


print('start')
greet_user('john', "smith")
greet_user('smith', "john")
greet_user("mary", '')
print("stop")

print('start')
greet_user(last_name='smith', first_name='john')
greet_user(first_name='john', last_name='smith')
# in line 7,8,9 the strings are called positional arguments. Which implies their position matters as 7,8 gives different output
# in line 13, 14 (last_name='smith') and (first_name= 'john') are called key word argument. which implies their position doesnt mattter as 13 and 14 gives same result.
# key word arguments are used to make the code more readable , mostly when the function is in numbers
# positional argument cant be after key word argument:
# greet_user(first_name='john', 'smith')
# the above line gives error while the below line doesnt
greet_user('smith', last_name='john')
# when we use positional arguement and key word arguement at the same time the positional arguement will still have significance to its position
# greet_user('smith', first_name= 'john')
# in the above code the presence of key word argument(first_name) doesnt imply the positional argument is other parameter(last_name),instead gives an error