'''
    Loops are used when we need to repeat same thing several number of times
    1. for loop
    2. while loop
'''

# for loop
print("for loop : ")
for i in range(5):
    print(i+1)

# while loop
print("while loop")

i = 5
while(i > 0):
    print(i)
    i = i - 1

cars = ['Koenigsegg CCXR Trevita', 'Lamborghini Veneno', 'W Motors Lykan Hypersport', 'Mansory Vivere Bugatti Veyron', 'Ferrari F60 America']

for car in cars:
    print(car)
else:
    print('In the else block :-)')