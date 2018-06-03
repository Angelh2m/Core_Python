
def square(num): return num * num


# print(square(3))

nums = [1, 2, 3, 4, 5, 6]

doubles = map(lambda x: x * 2, nums)

# print(doubles)

evens = list(filter(lambda x: x % 2 == 0, nums))

# print(evens)

users = [
    {"username": "samuel", "tweets": [
        "I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
# extract inact

# inactive_users = list(filter(lambda u: len(u['tweets']) == 0, users))

# print(inactive_users)

inactive_users2 = [user for user in users if not user['tweets']]
print(inactive_users2)
