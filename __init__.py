from flask import Flask

app = Flask(__name__)

@app.route("/getcolor")
def get_color():
    return "Success"

if __name__ == '__main__':
    app.run()


