from PIL import Image

img = Image.open('im1.jpg')
imgGray = img.convert('L')
imgGray.save('im2.jpg')