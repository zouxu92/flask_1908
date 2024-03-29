# coding:utf-8

from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    """接受前端上传过来的文件"""
    file_obj = request.files.get("pic")
    if file_obj is None:
        # 表示没有上传文件成功
        return "未上传文件，请重新上传"

    # 将文件保存到本地（传统方法）
    '''
    # 1.创建一个文件
    f = open("./demo.png", "wb")
    # 2.向文件写内容
    data = file_obj.read()
    f.write(data)
    # 3.关闭文件
    f.close()
    '''

    # 直接使用上传文件的对象保存文件
    file_obj.save("./demo1.png")
    return "上传成功"


if __name__ == '__main__':
    app.run(debug=True)