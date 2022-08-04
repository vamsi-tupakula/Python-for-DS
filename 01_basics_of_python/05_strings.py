car_name = "bob's car" # no esc char needed
bike_name = 'steve\'s bike' # \ is the esc char and it is important

# accessing string elements
lang = "Python_Programming"
print(lang[1])
print(lang[6])

# accessing certain parts of the string
print(lang[0:6])
print(lang[7:]) # starts with 7 and goes till end
print(lang[0:6:2]) # takes 2 steps

# string methods
print(lang.lower())
print(lang.upper())
print(lang.count('P')) # counts no of P's { case-sensitive }
print(lang.find('_')) # finds the index of _, returns -1 if not exist
code = lang.replace('Programming','Code')
print(code)

# formating strings
name = "Brad"
greeting = "Hello"
message = "{}, {}".format(greeting, name)
print(message)

new_message = f'{greeting}, {name}'
print(new_message)

# see all the methods and attributes related to a variable
print(dir(name))