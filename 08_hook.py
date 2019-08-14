# coding:utf-8

from flask import Flask, session


app = Flask(__name__)

@app.route("/index")
def index():
    print ("index 被执行")
    return "index page"


@app.before_first_request
def handle_before_first_request():
    '''在第一次请求处理之前先被执行'''
    print("handle_before_first_request 被执行")

@app.before_request
def handle_before_request():
    '''在每次请求处理之前都被执行'''
    print("handle_before_request 被执行")

@app.after_request
def handle_after_request(response):
    '''在每次请求（视图函数处理）之后都被执行， 前提是视图函数没有出现异常'''
    print("handle_after_request 被执行")
    return response

@app.teardown_request
def handle_teardown_request(response):
    '''在每次请求（视图函数处理）之后都被执行， 无视视图函数是否出现异常，都被执行'''
    print("handle_teardown_request 被执行")
    return response



if __name__ == '__main__':
    app.run(debug=True)