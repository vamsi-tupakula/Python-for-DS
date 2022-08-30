from collections import namedtuple

Color = namedtuple('Color', ['red','blue','green'])

color = Color(55,100,106)
print(color.red)