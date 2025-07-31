from encurta_url import app, db
from models import Url
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        
    return render_template('index.html')

