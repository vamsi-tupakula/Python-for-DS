from PIL import Image
import os

image1 = Image.open('puppy_1.jpg')
# image1.show() # to view

# to save the image
# image1.save('new_assets/puppy_1.png')

for img in os.listdir('.'):
    if img.endswith('.jpg'):
        print(img)