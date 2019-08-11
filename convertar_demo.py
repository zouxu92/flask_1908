# coding:utf-8

from flask import Flask,current_app,redirect, url_for
from werkzeug.routing import BaseConverter

# 创建flask的应用对象
# __name__ 表示当前的模块名字
#      模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

# 转换器
# @app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>") # 不加转换器类型， 默认是普通字符串规则(除了斜线的字符)
def goods_detail(goods_id):
	"""定义的视图函数"""
	return  "goods detail page %s" %goods_id

# 1. 定义自己的转换器
class MobileConverter(BaseConverter):
	def __init__(self, url_map):
		super(MobileConverter, self).__init__(url_map)
		self.regex = r'1[3456789]\d{9}'

class RegexConverter(BaseConverter):
	""""""
	def __init__(self, url_map, regex):
		# 调用父类的初始化方法
		super(RegexConverter, self).__init__(url_map)
		# 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由器的正则匹配
		self.regex = regex

# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter

# 3.使用自己的转换器
# 127.0.0.1:5000/send/17712345678
@app.route("/send/<re(r'1[3456789]\d{9}'):mobile>")
def send_sms(mobile):
	return "send sms to %s" % mobile

@app.route("/call/<re(r''):tel>")
def call_tel(tel):
	return tel

if __name__ == '__main__':
	# 通过url_map 可以查看整个flask中的路由信息
	print(app.url_map)
	# 启动flask程序
	app.run(debug=True)