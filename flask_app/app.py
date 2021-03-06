import os
from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from utils import slice_image
from constants import IMAGES_DIR_PATH

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

if not os.path.exists(IMAGES_DIR_PATH):
    os.makedirs(IMAGES_DIR_PATH)


@app.route('/upload', methods=['POST', ])
def upload_and_slice_image():
    image = request.files.get('image')
    grid_size = int(request.form.get('grid_size', 10))
    image.save(os.path.join(IMAGES_DIR_PATH, image.filename))

    return jsonify(slice_image(image.filename, grid_size))


@app.route('/images/<filename>')
def _static(filename):
    return send_from_directory(IMAGES_DIR_PATH, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
