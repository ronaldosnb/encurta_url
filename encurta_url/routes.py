from encurta_url import app, db
from .models import Url
from flask import render_template, request, redirect, url_for, flash
from .utils import gerar_short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']

        # Verifica se a URL já foi encurtada antes
        url_existente = Url.query.filter_by(original_url=original_url).first()
        if url_existente:
            flash('Essa URL já foi encurtada anteriormente!')
            return render_template('index.html', short_url=url_existente.short_url)

        # Se não existe, cria uma nova
        short_url = gerar_short_url() # A função agora garante um código único
        nova_url = Url(original_url=original_url, short_url=short_url)
        db.session.add(nova_url)
        db.session.commit()

        flash('URL encurtada com sucesso!')
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Redireciona a URL curta para a URL original."""
    # Busca a URL no banco ou retorna um erro 404 (Not Found) se não encontrar
    url_entry = Url.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url_entry.original_url)
