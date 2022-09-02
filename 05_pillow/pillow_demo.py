from PIL import Image
import os

image1 = Image.open('puppy_1.jpg')
# image1.show() # to view

# to save the image
# image1.save('new_assets/puppy_1.png')

# changing extensions
# for img in os.listdir('.'):
#     if img.endswith('.jpg'):
#         image = Image.open(img)
#         f_name, f_ext = os.path.splitext(img)
#         image.save('pngs/{}.png'.format(f_name))

# changing aspect ratio

size_300 = (300,300)

for img in os.listdir('.'):
    if img.endswith('.jpg'):
        image = Image.open(img)
        f_name, f_ext = os.path.splitext(img)
        image.thumbnail(size_300)
        image.save('300/{}_300{}'.format(f_name,f_ext))