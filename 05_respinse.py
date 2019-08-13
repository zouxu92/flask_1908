# coding:utf-8

from flask import Flask, request, abort, Response, make_response

app = Flask(__name__)

@app.route("/index")
def index():
    # 1 使用元组，返回自定义的响应信息
    #          响应体    状态码   响应头
    # return "index page", 400, [("Itcast", "python"), ("city", "shenzhen")]
    # return "index page", 400, {"Itcast":"python", "city":"shenzhen"}

    # 2.使用make_response 来构造信息
    resp = make_response("index Page 2")
    resp.status = "999 itcast" # 设置状态码
    resp.headers['city'] = "sz" # 设置响应头
    return resp

if __name__ == '__main__':
    app.run(debug=True)