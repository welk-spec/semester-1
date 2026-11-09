from image import Image, ImageError


def blur(img):
    """
    Blurs the given image by averaging each pixel with its neighbors.

    The edges of the image are not blurred, since they do not have a full
    set of neighbors.
    """
    new_img = Image.create(img.width, img.height, maximum=img.max_value)

    for row in range(5, img.height - 5):
        for col in range(5, img.width - 5):
            total = 0
            for r in range(-5, 6):
                for c in range(-5, 6):
                    total += img.get(row + r, col + c)
            average = total // 121
            new_img.set(row, col, average)

    return new_img
