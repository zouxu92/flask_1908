# coding:utf-8

from flask import Flask,current_app

# 创建flask的应用对象
# __name__ 表示当前的模块名字
#      模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,
			static_url_path='/python', # 访问静态资源的url前缀，默认值是static
			static_folder="static",  # 静态文件的目录，默认就是static
			template_folder="templates",  # 模板文件的目录，默认是templates
			)

# 配置参数的使用方式
# 1.使用配置文件
# app.config.from_pyfile("config.cfg")

# 2.使用类对象来配置参数
class Config(object):
	DEBUG = True
	ITCAST = "PYTHON"

app.config.from_object(Config)

# 3.直接操作config的字典对象
# app.config["DEBUG"] = True

@app.route("/")
def index():
	"""定义的视图函数"""

	# 读取配置参数
	# 1.直接冲全局对象app的config字典中取值
	# value = app.config.get("ITCAST")
	# 2.通过current_app获取参数
	value = current_app.config.get("ITCAST")
	print (value)
	return  "hello Flask"

if __name__ == '__main__':
	# 启动flask程序
	app.run()