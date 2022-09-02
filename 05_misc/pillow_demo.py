from PIL import Image
import os

image1 = Image.open('puppy_1.jpg')
# image1.show() # to view

# to save the image
# image1.save('new_assets/puppy_1.png')

for img in os.listdir('.'):
    if img.endswith('.jpg'):
        image = Image.open(img)
        f_name, f_ext = os.path.splitext(img)
        image.save('pngs/{}.png'.format(f_name))