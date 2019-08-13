# coding:utf-8

from flask import Flask, session


app = Flask(__name__)

# flask的session需要用到秘钥字符串
app.config["SECRET_KEY"] = "dkhekbgasdkkjdshakgbkjb"

# flask默认把session保存到cookie中

@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "python"
    session["mobile"] = "17788889999"
    return "login success"

@app.route("/index")
def index():
    # 获取sesion数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)