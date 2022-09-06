"""What is the difference between == and is ?"""
"""
== -> checks for equality, checks if values are equal
is -> checks for their identity, checks if the values are identical in terms of being the same object in the memory.
"""

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

# checking with ==
if l1 == l2:
    print('== ->', True)
else:
    print('== ->', False)

# checking with is
if l1 is l2:
    print('is ->', True)
else:
    print('is ->', False)

l3 = l1

if l1 is l3:
    print('is ->', True)
else:
    print('is ->', False)

"""
What is keyword actually do?
id(l1) == id(l2)
"""

print(id(l1))
print(id(l2))
print(id(l3))