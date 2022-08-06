"""
    Lists are used to store multiple items in a single variable. Lists are one of the 4 in-built data structures, other three are sets, dictionary, and tuples
"""
from operator import index


languages = ['python','java','c++','carbon']

# printing entire list
print(languages)

# accessing individual elements
print(languages[0])

# length of the list
print(len(languages))

# -ve indexing starts from last of the list
print(languages[-1])
print(languages[-4])

# accessing a range of values in list
print(languages[0:2])
print(languages[2:])

# list methods
languages.append('kotlin')
print(languages)

# list can also have duplicate values
languages.append('java')
print(languages)

# remove function will remove the first occurence of the parameter
languages.remove('java')
print(languages)

# inserting a certain position
languages.insert(3,'flutter')
print(languages)

# append vs extend
languages.append(['react','react-native'])
print(languages)

languages.extend(['html','css','javascript'])
print(languages)

# remove last element
popped = languages.pop()
print(languages)
print("popped : " + popped)

# find index of first occurence of element
print(languages.index('java'))

# reversing the list
languages.reverse()
print(languages)

# removing sub-list to do sorting
languages.remove(['react', 'react-native'])

# sorting
nums = [1,23,5,12,10]
nums.sort()
languages.sort()
print(nums)
print(languages)

nums.sort(reverse=True)
print(nums)

# make changes without altering the original
sorted_list = sorted(languages, reverse=True)
print(sorted_list)
print(languages)

reversed_list = reversed(languages)
print(list(reversed_list))

# some useful functions
print(min(nums))
print(max(nums))
print(sum(nums))

# looping over lists
for lang in languages:
    print(lang)

# prints the index and lang
# ! we can pass start argument if we dont want to start indexing at 0
for index, lang in enumerate(languages):
    print(index, lang)