# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config(object):
    '''配置参数'''
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:root123@127.0.0.1:3306/db_python04"

    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)

class Role(db.Model):
    '''用户角色/身份表'''
    __tablename__ = 'tbl_roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship("User", backref='role')


# 表名的常见规范
# ihome --> ih_user  数据库名缩写_表名
# tbl_user  tbl_表名
# 创建数据库模型类
class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True) # 整型的主键， 会默认设置为自增主键
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(64))
    # 设置外键
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))


if __name__ == '__main__':
    # 清除数据库的所有数据
    db.drop_all()

    # 创建所有的表
    db.create_all()
