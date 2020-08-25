from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/klvchen/')
def klvchen():
    return 'Hello klvchen'


if __name__ == '__main__':
    app.run()
