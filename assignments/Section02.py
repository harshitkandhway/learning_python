# Assignment 1
my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
print(my_list[0]["Bill"])
print(my_list[0].get("Bill"))

# Assignment 2
"""
Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""
my_list = [{'Tom': {'salary': 20000, 'age': 22, 'owns': ['jacket', 'car', 'TV']}},
           {'Mike': {'salary': 24000, 'age': 27, 'owns': ['bike', 'laptop', 'boat']}}]
print(my_list)

# Assignment 3
original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]
num1 = original_list[3][0]
num2 = original_list[3][1]
num3 = original_list[3][2]
new_list = [num1, num2, num3]
new_list.sort()
new_tuple = (new_list[0], new_list[1], new_list[2])
new_list = [original_list[0], original_list[1], original_list[2], new_tuple]

print(new_list)

# Assignment 4
my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]
my_list[2][0][3] = 'x'
my_list[3] = 'Television'
print(my_list)