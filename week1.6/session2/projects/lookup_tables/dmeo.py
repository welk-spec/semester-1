from image import Image, ImageError

table = [255 - x for x in range(256)]
print(table)

img = Image.read("coins.pgm")

for i in range(img.width * img.height):
    img[i] = table[img[i]]

img.write_pgm("output.pgm")
