"""Iterators vs Iterables"""
'''
List is an iterable but not iterator :-)
'''

ls = [1,2,3]

iter_ls = iter(ls)

while True:
    try:
        item = next(iter_ls)
        print(item)
    except StopIteration:
        break

# for loop automatically handles the StopIteration Exception