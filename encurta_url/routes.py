from encurta_url import app, db
from .models import Url
from flask import render_template, request, redirect, url_for, flash
from .utils import gerar_short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        url_existente = Url.query.filter_by(original_url=original_url).first()
        if url_existente:
            return render_template('index.html', short_url=url_existente.short_url)
        while True:
            short_url = gerar_short_url()
            if not Url.query.filter_by(short_url=short_url).first():
                break

        nova_url = Url(original_url=original_url, short_url=short_url)
        db.session.add(nova_url)
        db.session.commit()
        
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_url>')
def redirecionar(short_url):
    url = Url.query.filter_by(short_url=short_url).first()
    if url:
        return redirect(url.original_url)
    else:
        flash('URL não encontrada', 'danger')
        return redirect(url_for('index'))
