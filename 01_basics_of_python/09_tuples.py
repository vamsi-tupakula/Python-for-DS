'''
    Tuples unlike lists are immutables means we cannot make changes after creating a tuple
'''

names = ('steve','smith','corey','depp','steve','smith')
print(names)

# tuple methods
# ! tuple can also have duplicate values
# count returns the number of occurences of a value
print(names.count('steve'))

# returns the index of first appearence of a value
print(names.index('smith'))