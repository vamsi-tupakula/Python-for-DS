import random

value = random.random() # gives random value between 0 and 1
print(value)

value = random.uniform(1,10) # gives random float between 1 and 10
print(value)

value = random.randint(1,10) # random value between 1 and 10 including both
print(value)

names = ['tony','steve','banner','wanda','stephen']
name = random.choice(names)
print(name)