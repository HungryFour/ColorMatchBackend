from macpath import join

import qiniu
from flask import Flask,request,jsonify
from haishoku.haishoku import Haishoku
from qiniu import Auth
app = Flask(__name__)

@app.route("/")
def root():
    return "success"

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

@app.route("/color",methods=['post'])
def get_color():

    try:
        image_url = request.form['image_url']
        haishoku = Haishoku.loadHaishoku(image_url)
        h_dominant = haishoku.dominant
        h_palette = haishoku.palette
        dominant = {"R":h_dominant[0], "G":h_dominant[1], "B":h_dominant[2]}
        palette_array = []
        for p in h_palette:
            p_percentage = p[0]
            p_d = p[1]

            r_hex = str(hex(int(p_d[0]))).strip("0x");
            g_hex = str(hex(int(p_d[1]))).strip("0x");
            b_hex = str(hex(int(p_d[2]))).strip("0x");

            if None == r_hex or r_hex=="":
                r_hex = "00"
            if None == g_hex or r_hex=="":
                g_hex = "00"
            if None == b_hex or r_hex=="":
                b_hex = "00"
            if len(r_hex) == 1:
                if int(p_d[0]<10):
                    r_hex = "0"+r_hex
                else:
                    r_hex = r_hex+"0"
            if len(g_hex) == 1:
                if int(p_d[1]<10):
                    g_hex = "0"+g_hex
                else:
                    g_hex = g_hex+"0"
            if len(b_hex) == 1:
                if int(p_d[2]<10):
                    b_hex = "0"+b_hex
                else:
                    b_hex = b_hex+"0"
            hex_color = "#"+r_hex+g_hex+b_hex

            dic = {"percentage":p_percentage,
                   "RGB":{
                       "R":p_d[0],
                       "G":p_d[1],
                       "B":p_d[2]
                   },
                   "hex":hex_color
            }
            palette_array.append(dic)

        return jsonify({
            "code":200,
            "dominant": dominant,
            "palette": palette_array
        })
    except Exception as err:
        return jsonify(
            {
                "code":501
            }
        )

if __name__ == '__main__':
    app.run()


