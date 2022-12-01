from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def housing():
    if request.method == 'POST':
        