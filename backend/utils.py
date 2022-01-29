import os
from PIL import Image
from itertools import product
from constants import IMAGES_DIR_PATH


def slice_image(filename, grid_dimension):
    name, ext = os.path.splitext(filename)
    source_filename = os.path.join(IMAGES_DIR_PATH, filename)
    image = Image.open(source_filename)
    width, height = image.size
    tile_width = width // grid_dimension
    tile_height = height // grid_dimension

    grid = product(range(0, height - height % tile_height, tile_height),
                   range(0, width - width % tile_width, tile_width))
    for i, j in grid:
        box = (j, i, j + tile_height, i + tile_width)
        destination_filename = os.path.join(IMAGES_DIR_PATH, f'{name}_{i}_{j}{ext}')
        image.crop(box).save(destination_filename)

    os.remove(source_filename)
