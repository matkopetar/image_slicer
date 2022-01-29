from flask import Flask

app = Flask(__name__)


@app.route('/upload', methods=['POST', ])
def upload_and_slice_image():
    return 'Image is sliced.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
