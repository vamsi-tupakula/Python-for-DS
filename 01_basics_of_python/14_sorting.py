# sorting in lists

my_list = [9,1,8,2,7,3,6,4,5]
sorted_list = sorted(my_list) # returns a new sorted list
print(sorted_list)
print(my_list)
my_list.sort() # sorts the original list
print(my_list)

my_list.sort(reverse=True)
print(my_list)