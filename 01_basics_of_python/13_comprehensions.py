"""list comprehension"""

# code-block 1
my_list = [n*n for n in range(11)]
print(my_list)

# code-block 2
my_list = [n for n in range(11) if (n%2 == 0)]
print(my_list)

# code-block 3 (map + lambda)
my_list = map(lambda x : x*x, range(11))
print(list(my_list))

# code-block 4 (filter + lambda)
my_list = filter(lambda x: x%2 == 0, range(11))
print(list(my_list))

# code-block 5
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

# code-block 6 (zip function for lists)
names = ['john wick','jack sparrow','bruce banner','tony stark']
ages = [28,29,32,35]

pairs = zip(names, ages)
print(list(pairs))

# code-block 7 (zip function for dictionary)
my_dict = {name: age for name,age in zip(names,ages)}
print(my_dict)

"""Set Comprehensions"""

# code-block 8 
new_list = [1,1,1,2,3,2,3,2,3,2]
my_set = {x for x in new_list}
print(my_set)