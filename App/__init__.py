from config import basedir
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')   # 载入配置文件
from Views import picture
from Views import qiniu




