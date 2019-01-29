from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


def get_page_text_from_file():
    f = open('page.html', "r")
    return f.read()


# sanity check route
@app.route('/', methods=['GET'])
def ping_pong():
    return get_page_text_from_file()


# @app.route('/')
# def random_number():
#     response = {
#         'randomNumber': 666
#     }
#     return jsonify(response)


if __name__ == '__main__':
    app.run()
