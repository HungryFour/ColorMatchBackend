from flask import Flask
from flask_restful import Api

from Views.picture import RootClass, GetColorClass
from Views.qiniu import UploadTokenClass

app = Flask(__name__)
api = Api(app)

# These are the extension that we are accepting to be uploaded
api.add_resource(RootClass, "/")
api.add_resource(GetColorClass, "/color")
api.add_resource(UploadTokenClass, "/uploadtoken")