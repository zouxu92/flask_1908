# coding:utf-8

from flask import Flask, request

app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
def index():
    # request中包含了前端发送过来的所有数据
    # 通过request.form可以直接提取请求中的表单个数的数据，是一个类字典的对象
    # 通过get方法只能拿到多个同名参数的第一个
    name = request.form.get('name')
    age = request.form.get('age')
    # getlist可以获取同一个参数的全部值
    name_li = request.form.getlist("name")

    # 如果是请求体的数据不是表单个数的（如json格式），可以通过request.data获取
    print(request.data)

    # 通过args获取查询字符串参数（url中的参数）
    city = request.args.get('city')
    return u"hello name=%s, age=%s， city=%s, name_li=%s" %(name, age, city, name_li)


if __name__ == '__main__':
    app.run(debug=True)