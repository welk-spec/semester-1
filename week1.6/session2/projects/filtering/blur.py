import sys
from image import Image
from filters import blur

if len(sys.argv) != 3:
    print("Usage: python blur.py <input_image> <output_image>")
    sys.exit(1)

img = Image.read(sys.argv[1])
blurred = blur(img)
blurred.write_pgm(sys.argv[2])
