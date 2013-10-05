from flask import redirect, url_for, request, render_template

from app import app
import url, excepts
from db import session
from models import Url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
       if "url" in request.form:
           try:
               # encodes and stores the url:
               encoded_url = data.store(url, encoded_url)
           except:
               return undefined_error()
    
    return render_template("index.html")

@app.route("/<encoded_url>")
def redir(encoded_url):
    try:
        url = data.retrieve(encoded_url)
    except excepts.NotFoundException:
        return notfound_error()
    except:
        return undefined_error()

# error handlers

@app.errorhandler(500)
def server_error():
    return render_template("500.html")

@app.errorhandler(404)
def notfound_error():
    return render_template("404.html")

def undefined_error():
    return render_template("undefined_error.html")
