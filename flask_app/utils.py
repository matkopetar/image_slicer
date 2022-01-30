import os
from PIL import Image
from constants import IMAGES_DIR_PATH, IMAGES_ENDPOINT_URL


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

    sliced_images = _create_image_response_list(grid_dimension)
    number_of_tiles = grid_dimension * grid_dimension

    for row in range(grid_dimension):
        for column in range(grid_dimension):
            image_tile_filename = f'{name}_{row}_{column}{ext}'
            destination_filename = os.path.join(IMAGES_DIR_PATH, image_tile_filename)

            box = (column * width / grid_dimension,
                   row * height / grid_dimension,
                   column * width / grid_dimension + width / grid_dimension,
                   row * height / grid_dimension + height / grid_dimension)
            image.crop(box).save(destination_filename)

            number_of_tiles = number_of_tiles - 1
            sliced_images[grid_dimension - number_of_tiles // grid_dimension - 1].\
                append(IMAGES_ENDPOINT_URL + image_tile_filename)

    os.remove(source_filename)

    return sliced_images
