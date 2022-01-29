import os
from flask import Flask, request
from utils import slice_image
from constants import IMAGES_DIR_PATH

app = Flask(__name__)


@app.route('/upload', methods=['POST', ])
def upload_and_slice_image():
    image = request.files.get('image')
    image.save(os.path.join(IMAGES_DIR_PATH, image.filename))
    slice_image(image.filename, 10)

    return 'Image is sliced.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
