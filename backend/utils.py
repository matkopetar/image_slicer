import os
from PIL import Image
from itertools import product
from constants import IMAGES_DIR_PATH


def _create_image_response_list(dimension):
    response_list = list()
    for i in range(0, dimension):
        response_list.append(list())

    return response_list


def slice_image(filename, grid_dimension):
    name, ext = os.path.splitext(filename)
    source_filename = os.path.join(IMAGES_DIR_PATH, filename)
    image = Image.open(source_filename)
    width, height = image.size
    tile_width = width // grid_dimension
    tile_height = height // grid_dimension

    sliced_images = _create_image_response_list(grid_dimension)
    number_of_tiles = grid_dimension * grid_dimension

    grid = product(range(0, height - height % tile_height, tile_height),
                   range(0, width - width % tile_width, tile_width))
    for i, j in grid:
        box = (j, i, j + tile_height, i + tile_width)
        image_tile_filename = f'{name}_{i}_{j}{ext}'
        destination_filename = os.path.join(IMAGES_DIR_PATH, image_tile_filename)
        image.crop(box).save(destination_filename)

        number_of_tiles = number_of_tiles - 1
        sliced_images[grid_dimension - number_of_tiles // grid_dimension - 1].append(image_tile_filename)

    os.remove(source_filename)

    return sliced_images
