
tasks = ['Install python', 'learn python', 'take a break']

for task in tasks:
    print(task)


# --------------------------
#  POP remove the las in the array
# --------------------------

tasks.pop()

# print(tasks)


# --------------------------
#  METHODS
#
# - .remove()
# - .clear()
# - .reverse()
# - .sort()
# - .join()
# --------------------------

names = ['John', "Martin", "Albert", "Maria", "Mark"]

friends = ', '.join(names)

# print(friends)

# --------------------------
#  METHODS
#
# - colors[1] => orange
# - colors[-2:] END
# - colors[:2] Slice from start
#  result = "red" in colors // Check if it exist or not
# --------------------------

colors = ['red', 'orange', 'purple', 'blue', 'green', 'violet']

result = "red" in colors
print("THERE IS A COLOR ???")
print(result)

# print(colors[-2:])

# print(colors)


# --------------------------
#  List comprenhension
# --------------------------

nums = [1, 2, 3]

nums_2 = [x * 10 for x in nums]

print(nums_2)

# --------------------------

friends = ['Ashley', 'Matt', 'michiel']

result = [friends[0].upper() for friend in friends]
print(result)

print(bool(''))


color = ['Blue', 'Green', 'Orange']

result2 = [color.upper() for color in colors]
# print(result2)

coords = [[10.122, 9.123], [43.234, -12.123], [12.123, 89.097]]

for location in coords:
    for coord in location:
        print(coord)
