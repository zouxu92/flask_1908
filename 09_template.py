# coding:utf-8

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name":"python",
        "age": 18,
        "my_dict":{"city":"sz"},
        "my_list":[1, 2, 3, 4, 5],
        "my_int":0

    }
    # 1.直接在模板后面传递参数
    # return render_template("index.html", name="python", age=20)
    return render_template("index.html", **data)

if __name__ == '__main__':
    app.run(debug=True)