# f = open('test.txt', 'r')

# print(f.name)
# print(f.mode)

# above code is same as below
with open('test.txt', 'r') as f:
    # print(f.name)
    # print(f.mode)

    # f_contents = f.read()
    # print(f_contents)

    for line in f:
        print(line, end='')


with open('test2.txt', 'w') as f:
    f.write('New Test File....')