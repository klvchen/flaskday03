# __author__: "klvchen"
# date: 2020/8/25
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/show1')
def show1():
    girls = ['klvchen', 'lily', 'lucy', 'tom', 'james']
    return render_template('show_1.html', girls=girls)


if __name__ == '__main__':
    app.run(debug=True)
