# list comprehension

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