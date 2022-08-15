# list comprehension

# code-block 1
my_list = [n*n for n in range(11)]
print(my_list)

# code-block 2
my_list = [n for n in range(11) if (n%2 == 0)]
print(my_list)