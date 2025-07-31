import random
import string
from .models import Url

def gerar_short_url():
    """Gera um código de URL curta único com 6 caracteres."""
    letras = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(letras) for _ in range(6))
        # Verifica no banco de dados se o código já existe
        if not Url.query.filter_by(short_url=short_url).first():
            return short_url