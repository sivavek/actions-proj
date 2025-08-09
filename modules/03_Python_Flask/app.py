from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify(message='Hello, World!')


@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify(
        {
            'message': 'This is a message from the API!'
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
