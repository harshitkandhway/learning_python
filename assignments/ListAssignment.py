my_list = ['a', 'g', 'd', 'h', 'b']
another_list = [1, 9, 2, 3, 7, 4, 5]

my_list.sort()
my_list.reverse()
another_list.sort()
another_list.reverse()

result = my_list[-3:]+another_list[-3:]
print(result)