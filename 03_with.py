# coding:utf-8


'''
# 1.创建一个文件
f = open("./1.txt", "wb")
# 2.向文件写内容
try:
	f.write("hello flask")
except Exception:
	pass
finally:
	# 3.关闭文件
	f.close()


# with上下文管理器
with open("./1.txt", "wb") as f:
	f.write("hello flask")
'''

class Foo(object):
	def __enter__(self):
		"""进入with语句的时候被调用"""
		print("enter called")

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""离开with语句的时候with调用"""
		print("exit called")
		print("exc_type: %s" % exc_type)
		print("exc_val: %s" % exc_val)
		print("exc_tb: %s" % exc_tb)

with Foo() as foo:
	print("hello python")
	a = 1/0
	print("hello python")