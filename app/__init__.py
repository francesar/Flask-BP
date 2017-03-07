from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import requests as r
from mongoengine import connect

from models import Post
from Post import Post

app = Flask(__name__)
app.config["DEBUG"] == True

socketio = SocketIO(app)

connect(host="mongodb://cesar:cesar@ds123050.mlab.com:23050/flasktalk")

@app.route('/')
def index():
	user_posts = Post.objects
	return render_template("index.html", posts=user_posts)

@app.route("/post")
def post():
	return render_template("post.html")
