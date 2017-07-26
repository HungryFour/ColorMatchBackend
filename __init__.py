from macpath import join

from flask import Flask,request,jsonify
from haishoku.haishoku import Haishoku

app = Flask(__name__)

@app.route("/getcolor",methods=['post'])
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
            dic = {"percentage":p_percentage,
                   "RGB":{
                       "R":p_d[0],
                       "G":p_d[1],
                       "B":p_d[2]
                   }}
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


