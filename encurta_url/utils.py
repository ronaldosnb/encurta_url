import random
import string
from .models import Url

def gerar_short_url():
    letras = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(letras) for _ in range(6))
    return short_url