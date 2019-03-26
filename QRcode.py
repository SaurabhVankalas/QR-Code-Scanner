from flask import Flask, render_template, Response
app = Flask(__name__)
from qr import func
import os

@app.route('/',methods=['GET','POST'])
def index():
    x = func()
    return x

if  __name__ == '__main__':
	app.run(host='0.0.0.0',port=1100,debug=True)
