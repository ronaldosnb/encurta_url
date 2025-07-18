from encurta_url import app, db
# from encurta_url.models import Url
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')