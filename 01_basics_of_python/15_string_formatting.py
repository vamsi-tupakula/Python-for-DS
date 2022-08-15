person = {
    'name': 'John Wick',
    'age': 33
}

sentence = 'I am {}, i"m {}'.format(person['name'],person['age'])
print(sentence)

sentence = 'I am {0}, i"m {1}'.format(person['name'],person['age'])
print(sentence)

sentence = 'I am {name}, i"m {age}'.format(name="Jack",age=22)
print(sentence)

sentence = 'I am {name}, i"m {age}'.format(**person)
print(sentence)

pi = 3.14159265
sentence = "pi is equal to {}".format(pi)
print(sentence)

sentence = "pi is equal to {:.2f}".format(pi)
print(sentence)

sentence = "{} has 6 zeros".format(1000**2)
print(sentence)

sentence = "{:,} has 6 zeros".format(1000**2)
print(sentence)