"""
    Sets can be considered as a the sets which we have seen in our high-school mathematics, they don't have duplicate values, they cannot be indexed and they are unordered.
"""

set_1 = {1,2,3,4,5,3}
print(set_1)
# it will remove duplicates automatically

# sets methods
# adds element at end
set_1.add(6)
print(set_1)

# removes 4 from the set
set_1.remove(4)
print(set_1)

# discard is similar to remove but if elem is not exist in list remove will give us error but discard does nothing
set_1.discard(7)
print(set_1)

even_nums = {2,4,6,8,10}
prime_nums = {2,3,5,7,11}
odd_nums = {1,3,5,7,9}

# intersection of two-sets
print(set.intersection(even_nums, prime_nums))
print(odd_nums.intersection(prime_nums))

# difference of two sets
print(odd_nums.difference(prime_nums)) # gives elements which are present only in odd_nums but not in prime_nums
print(prime_nums.difference(even_nums)) # gives elements which are present only in prime_nums but not in even_nums

# union
print(odd_nums.union(even_nums))

# how to create empty set
empty_set = {}
print(type(empty_set)) # type will be dictionary
empty_set = set()
print(type(empty_set)) # type will be set