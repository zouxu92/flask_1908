# coding:utf-8

import unittest
from longin import app
import json

class LoginTest(unittest.TestCase):
	'''构造单元测试案例'''
	def setUp(self):
		'''在进行测试之前，先被执行'''
		# 设置flask工作在测试模式下
		# app.config["TESTING"] = True  # 两种方式都可以
		app.testing = True

		# 创建进行web请求的客户端，使用flask提供的
		self.client = app.test_client()

	def test_empty_user_name_password(self):
		'''测试用户名密码不完整的情况'''
		# 测试账号密码都不传递
		ret = self.client.post("/login", data={})

		# ret 是视图返回的响应对象,data属性是响应的数据
		resp = ret.data

		# 因为login视图返回的是json字符串
		resp = json.loads(resp)

		# 拿到返回值后进行断言测试
		self.assertIn("code", resp)
		self.assertEqual(resp["code"], 1)


		# 测试只传递账号
		ret = self.client.post("/login", data={"user_name": "admin"})

		# ret 是视图返回的响应对象,data属性是响应的数据
		resp = ret.data

		# 因为login视图返回的是json字符串
		resp = json.loads(resp)

		# 拿到返回值后进行断言测试
		self.assertIn("code", resp)
		self.assertEqual(resp["code"], 1)

		# 测试只传递密码
		ret = self.client.post("/login", data={"password": "admin"})

		# ret 是视图返回的响应对象,data属性是响应的数据
		resp = ret.data

		# 因为login视图返回的是json字符串
		resp = json.loads(resp)

		# 拿到返回值后进行断言测试
		self.assertIn("code", resp)
		self.assertEqual(resp["code"], 1)

	def test_wrong_user_name_password(self):
		"""测试账号或密码错误"""
		# 账号密码都错误
		ret = self.client.post("/login", data={"user_name": "itcast", "password": "123456"})
		# ret 是视图返回的响应对象,data属性是响应的数据
		resp = ret.data

		# 因为login视图返回的是json字符串
		resp = json.loads(resp)

		# 拿到返回值后进行断言测试
		self.assertIn("code", resp)
		self.assertEqual(resp["code"], 2)


		# 密码错误
		ret = self.client.post("/login", data={"user_name": "admin", "password": "123456"})
		# ret 是视图返回的响应对象,data属性是响应的数据
		resp = ret.data

		# 因为login视图返回的是json字符串
		resp = json.loads(resp)

		# 拿到返回值后进行断言测试
		self.assertIn("code", resp)
		self.assertEqual(resp["code"], 2)

	def test_success_login(self):
		"""测试账号密码正确，登录成功"""
		# 账号密码都正确
		ret = self.client.post("/login", data={"user_name": "admin", "password": "python"})
		# ret 是视图返回的响应对象,data属性是响应的数据
		resp = ret.data

		# 因为login视图返回的是json字符串
		resp = json.loads(resp)

		# 拿到返回值后进行断言测试
		self.assertIn("code", resp)
		self.assertEqual(resp["code"], 0)

if __name__ == "__main__":
	unittest.main()