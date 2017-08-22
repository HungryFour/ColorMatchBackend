from flask import Flask
from flask_restful import Api
from App.Views.picture import RootClass
from App.Views.picture import GetColorClass
from App.Views.qiniu import UploadTokenClass

app = Flask(__name__)
api = Api(app)

# These are the extension that we are accepting to be uploaded
api.add_resource(RootClass, "/")
api.add_resource(GetColorClass, "/color")
api.add_resource(UploadTokenClass, "/uploadtoken")