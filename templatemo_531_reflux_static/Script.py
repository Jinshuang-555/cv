from flask import Flask, render_template
from flask.helpers import url_for
from flask import send_file
import os
STATIC_DIR = os.path.abspath('static')
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)