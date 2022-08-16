import os

# to get help about this module
# print(dir(os))

# get current working directory
# print(os.getcwd())

# change working directory
# os.chdir('C:\\Users\HP\\Videos\\Programming\\Python\\python-for-ds\\')
# print(os.getcwd())

# list directory
# print(os.listdir())

# create directory
os.mkdir('demo')

# remove directory
os.rmdir('demo')

# get home directory
print(os.environ.get('HOME'))

file_name = os.path.join(os.environ.get('HOME'), 'test_file.py')
print(file_name)