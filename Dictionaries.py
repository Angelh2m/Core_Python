user_info = {"name": "Blue", "age": 10, "email": "blue@gmail.com"}

print(user_info)

print(user_info["email"])

newuser = dict(name="PORK")
# print(newuser)

# --------------------------
#  .values()
#  .keys()
#  .items()
#  for k, v in instructor.items(): // KEY and VALUE
#    print(f"Key name is {k} and value is {v} ")
# .copy
#
# --------------------------

instructor = {
    "name": 'Angel',
    "owns dogs": True,
    "Favorite language": "Python",
    "is hilarious": False,
    "My favorite number": 8,
}

results = instructor.values()
print(results)
print('===============================')
for v in instructor.values():
    print(v)

print('===============================')

for v in instructor.keys():
    print(v)

print('===============================')

for v in instructor.items():
    print(v)

# for k, v in instructor.items():
#     print(f"Key name is {k} and value is {v} ")

# --------------------------
#  METHODS
#
# - .pop()
# - .popItem
# - person.update(instructor)
# --------------------------

instructor = {
    "name": 'MArk',
    "owns dogs": True,
    "Favorite language": "Python",
    "is hilarious": False,
    "My favorite number": 8,
}

instructor.pop("name")


print('===============================')

instructor = {
    "name": 'Colt',
    "num courses": 4,
    "Favorite language": "Python",
}
person = {'city': 'Antigua'}
person.update(instructor)
print(person)


print('===============================')

playlist = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': [
            'kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
    ]
}
total_length = 0

for song in playlist['songs']:
    total_length += song['duration']
    print(song['duration'])
print('DURATION')
print(total_length)
