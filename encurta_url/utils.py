import random
import string
from .models import Url

def gerar_short_url():
    letras = string.ascii_letters + string.digits
    return ''.join(random.choice(letras) for _ in range(6))