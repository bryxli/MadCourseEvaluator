from flask import Flask

api = Flask(__name__)

@api.route('/courselist')
def courselist():
    return [
        { "id": "CS506", "name": "Software Engineering" },
        { "id": "CS577", "name": "Introduction to Algorithms" },
    ]
