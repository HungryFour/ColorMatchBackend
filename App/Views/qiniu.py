
import qiniu
from qiniu import Auth
from flask import Flask, jsonify
from __init__ import app

@app.route("/uploadtoken",methods=['get'])
def get_uploadtoken():
    try:
        q = qiniu.Auth("G3meMJe5tIidwGR271mDStmwp900AFRIvQ8S6d-y", "GyPLkmlb3ORbFZjvF42s_Uo-q14FV-5hIpFoSNeH")
        token = q.upload_token("photo")
        print(token)
        return jsonify({
            "code":200,
            "token":token
        })
    except Exception as err:
        return jsonify(
            {
                "code":501
            }
        )