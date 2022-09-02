from PIL import Image, ImageFilter
import os

# image1 = Image.open('puppy_1.jpg')
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

# size_300 = (300,300)

# for img in os.listdir('.'):
#     if img.endswith('.jpg'):
#         image = Image.open(img)
#         f_name, f_ext = os.path.splitext(img)
#         image.thumbnail(size_300)
#         image.save('300/{}_300{}'.format(f_name,f_ext))

# rotate images
# image1 = Image.open('puppy_1.jpg')
# image1.rotate(90).save('puppy_1_rotate.jpg')

# make black and white images
# image2 = Image.open('puppy_2.jpg')
# image2.convert(mode='L').save('puppy_2_bw.jpg')

# make blur images using ImageFilter
image3 = Image.open('puppy_3.jpg')
image3.filter(ImageFilter.GaussianBlur(3)).save('puppy_3_blur.jpg')