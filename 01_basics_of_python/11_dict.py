'''
    a dictionary is a collection which is ordered, changable and does not allow duplicate values. dictionaries are used to store data in the form of key-value pair. key must be a unique value :-)
'''

# creates a empty dictionary
dict_1 = {}
print(type(dict_1))

# student dictionary
student = {'name': 'Jhonny Depp', 'age': 22,'courses': ['Math','Physics','Chemistry']}
print(student)
print("name : " + student['name'])

# indexing the key which does not exist in the dict will give us error so we use get method which returns None when something is not present
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

# adding new key-value pair
student['phone'] = 1234567890
print(student)

# changing existing one
student['name'] = 'Jack Sparrow'
print(student)

# update method
student.update({'name': 'Jhonny', 'phone': '0987654321'})
print(student)

# removes element
phone = student.pop('phone')
print(phone)
print(student)

# keys values items in dict
print(student.keys())
print(student.values())
print(student.items())