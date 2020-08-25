from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


class Girl:
    def __init__(self, name, addr):
        self.name = name
        self.gender = '女'
        self.addr = addr

    def __str__(self):
        return self.name


@app.route('/show')
def show():
    name = 'klvchen'
    age = 18
    friends = ['klvchen', 'lily', 'lucy', 'tom']
    dict1 = {'gift': '大手镯', 'gift1': '鲜花', 'gift2': '费列罗'}

    # 创建对象
    girlfriend = Girl('lily', '广东')

    return render_template('show.html', name=name, age=age, gender='男', friends=friends, dict1=dict1, girl=girlfriend )


if __name__ == '__main__':
    app.run(debug=True)
