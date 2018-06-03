result = {num: num ** 2 for num in [1, 2, 3, 4, 5, 6]}
print(result)

instructor = {
    'name': 'colt',
    'city': 'San francisco',
    'color': 'purple'
}

yelling_instructor = {k.upper(): v.upper() for k, v in instructor.items()}

print(yelling_instructor)


num_list = [1, 2, 3, 4]

result = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(result)
