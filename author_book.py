# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

class Config(object):
    '''配置参数'''
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:root123@127.0.0.1:3306/author_book_py04"

    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "ldlkghkfhglkrhk7868jsfdlnlk"

app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

# 创建flask脚本管理工具对象
manager = Manager(app)


# 创建数据库迁移工具对象
Migrate(app, db)

# 向manger对象中添加数据库的操作命令
manager.add_command('db', MigrateCommand)

# 定义数据库的模型
class Author(db.Model):
    """作者"""
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")
    email = db.Column(db.String(64))

class Book(db.Model):
    """书籍"""
    __tablename__ = "tbl_books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))

# 创建表单模型类
class AuthorBookForm(FlaskForm):
    '''作者数据表单模型类'''
    author_name = StringField(label=u"作者", validators=[DataRequired(u"作者必须填写")])
    book_name = StringField(label=u"书籍", validators=[DataRequired(u"书籍名称必须填写")])
    submit = SubmitField(label=u"保存")


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        # book = Book(name=book_name, author=author) 两种方法都可以；
        db.session.add(book)
        db.session.commit()

    # 查询数据库
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)

# post /delete_book json
# {"book_id": xxx}

'''
@app.route("/delete_book", methods=["POST"])
def delete_book():
    # ##删除数据
    # 提取参数
    # 如果前端发送的请求体数据是json格式，get_json 会解析成字典
    # get_json 要求前端传送的数据的 Content-Type: application/json
    req_dict = request.get_json()
    book_id = req_dict.get("book_id")

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    # Content-Type: application/json
    return jsonify(code=0, message="ok")
'''
# delete_book?book_id=xx
@app.route("/delete_book", methods=["GET"])
def delete_book():
    '''删除数据'''
    # 提取参数
    book_id = request.args.get("book_id")

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    # Content-Type: application/json
    return redirect(url_for("index"))


if __name__ == '__main__':
    ''' 基础数据
    # 清除数据库的所有数据
    db.drop_all()
    # 创建所有的表
    db.create_all()
    au_xi = Author(name='我吃西红柿')
    au_qian = Author(name='萧潜')
    au_san = Author(name='唐家三少')
    db.session.add_all([au_qian, au_san, au_xi])
    db.session.commit()

    bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
    bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
    bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    db.session.add_all([bk_qian, bk_san, bk_xi, bk_xi2])
    db.session.commit()
    '''
    # app.run(debug=True)
    # 通过manager启动命令
    manager.run()