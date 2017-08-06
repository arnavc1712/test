from flask import Flask
from flask import render_template,flash, request
from flask import url_for
from flask_pymongo import PyMongo
from flask import jsonify
from flask_mail import Mail
from flask_mail import Message
import hashlib
from flask_login import login_user, logout_user, LoginManager
from flask_login import current_user


app = Flask(__name__)

app.config['MONGO_DBNAME']= 'kakushin'
app.config['MONGO_URI']= 'mongodb://127.0.0.1:27017/kakushin'
app.secret_key='some secret'
mongo=PyMongo(app)



@app.route('/',methods=['GET'])
def index():
	return render_template("upload.html")



@app.route('/something',methods=['POST'])
def upload():
	file= request.files['file']
	# file=str(file)
	print file.filename
	return "Sort"