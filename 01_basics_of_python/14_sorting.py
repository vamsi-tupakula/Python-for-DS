# sorting in lists

my_list = [9,1,8,2,7,3,6,4,5]
sorted_list = sorted(my_list) # returns a new sorted list
print(sorted_list)
print(my_list)
my_list.sort() # sorts the original list
print(my_list)

my_list.sort(reverse=True)
print(my_list)

# sorting in tuples
# tuples does not have sort method so we need to use sorted function
my_tuple = (9,1,8,2,7,3,6,4,5)
sorted_tuple = sorted(my_tuple,reverse=True) 
# by default sorted function will always returns list
print(tuple(sorted_tuple))