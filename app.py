from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
   app.run()