# If statements

name = 'john'
if name == 'mark':
    print('mark')
elif name == 'john':
    print('You know john')
else:
    print("Carry on")


# "Or" lofical operator

city = input('Where do you live? ')

if city == "LA" or city == "SF":
    print('You live in CA')
else:
    print('You live somewhere else')

#  "not" logical operator
age = 21

if not((age >= 2 and age <= 8) or age >= 65):
    print('You pay 10 dollars and are not a child o senior')
