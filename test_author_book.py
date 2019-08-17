# coding:utf-8

import unittest
from author_book import Author, db, app

class DatabaseTest(unittest.TestCase):
	def setUp(self):
		app.testing = True
		app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root123@127.0.0.1:3306/flask_test"
		db.create_all()

	def test_add_author(self):
		'''测试添加作者的数据库'''
		author = Author(name="zhang", email="itcast@itcast", mobil="18612345678")
		db.session.add(author)
		db.session.commit()

		import time
		time.sleep(3)

		result_author = Author.query.filter_by(name="zhang").first()
		self.assertIsNotNone(result_author)

	def tearDown(self):
		'''在所有的测试执行后，执行，通常用来进行清理操作'''
		db.session.remove()
		db.drop_all()