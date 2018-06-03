from random import random


def say_hi():
    print('hi')


# say_hi()


def coin_flip():
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return"tails"


# print(coin_flip())


def square(square):
    return square * square


# print(square(8))


def divide(num1, num2):
    return num1 / num2


# print(divide(6, 3))

# --------------------------
#  METHODS
#
# - *args
# --------------------------

# Dynamic arguments
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_nums(1, 23, 3, 34, 5))

# Get Dictionary


def fav_colors(**kwars):
    print(kwars)


fav_colors(colt="purple", ruby="REd", ethel="green")
