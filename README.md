# Encurtador de URLs com Flask 🔗

Um encurtador de URLs simples e eficiente desenvolvido com Flask, PostgreSQL e Docker. Permite transformar URLs longas em links curtos e fáceis de compartilhar.

## ✨ Funcionalidades

- **Encurtamento de URLs**: Transforma URLs longas em códigos de 6 caracteres
- **Redirecionamento automático**: Redireciona automaticamente para a URL original
- **Verificação de duplicatas**: Retorna a mesma URL curta para URLs já encurtadas
- **Interface responsiva**: Design limpo e moderno
- **Banco de dados persistente**: Armazena URLs no PostgreSQL

## 🚀 Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrações**: Flask-Migrate
- **Containerização**: Docker & Docker Compose
- **Servidor**: Gunicorn
- **Frontend**: HTML5, CSS3

## 📋 Pré-requisitos

- Docker
- Docker Compose
- Git

## 🛠️ Instalação e Execução

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd encurta-url
```

### 2. Execute com Docker Compose
```bash
docker-compose up --build
```

### 3. Acesse a aplicação
Abra seu navegador e acesse: `http://localhost:5000`

## 📁 Estrutura do Projeto

```
encurta-url/
├── encurta_url/
│   ├── __init__.py          # Configuração da aplicação Flask
│   ├── models.py            # Modelos do banco de dados
│   ├── routes.py            # Rotas da aplicação
│   ├── utils.py             # Funções utilitárias
│   ├── static/
│   │   └── css/
│   │       └── style.css    # Estilos da aplicação
│   └── templates/
│       └── index.html       # Template principal
├── instance/
│   └── pg_data/            # Dados do PostgreSQL
├── Docker-compose.yaml     # Configuração do Docker Compose
├── Dockerfile             # Configuração do container
├── requirements.txt       # Dependências Python
└── .gitignore            # Arquivos ignorados pelo Git
```

## 🐳 Configuração do Docker

### Serviços Definidos:

#### Web (Flask App)
- **Porta**: 5000
- **Ambiente**: Desenvolvimento com debug ativo
- **Volumes**: Código fonte mapeado para desenvolvimento

#### Database (PostgreSQL)
- **Porta**: 5432
- **Usuário**: user
- **Senha**: password
- **Database**: encurta_db

## 🗄️ Banco de Dados

### Modelo `Url`
```python
class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
```

## 🔧 Configuração de Ambiente

As seguintes variáveis de ambiente são utilizadas:

```bash
DATABASE_URL=postgresql://user:password@db:5432/encurta_db
FLASK_APP=encurta_url
FLASK_DEBUG=1
SECRET_KEY=uma-chave-secreta-para-desenvolvimento
```

## 📝 Como Usar

1. **Acesse** a aplicação em `http://localhost:5000`
2. **Cole** sua URL longa no campo de texto
3. **Clique** em "Encurtar!"
4. **Copie** a URL encurtada gerada
5. **Compartilhe** a URL curta - ela redirecionará automaticamente

## 🔍 Endpoints da API

- `GET /` - Página principal com formulário
- `POST /` - Processa o encurtamento da URL
- `GET /<short_url>` - Redireciona para a URL original

## 🛡️ Características de Segurança

- Validação de URLs no frontend
- Verificação de URLs duplicadas
- Tratamento de erros para URLs não encontradas
- Geração segura de códigos aleatórios

## 🔄 Algoritmo de Geração

O sistema gera códigos de 6 caracteres usando:
- Letras maiúsculas e minúsculas (A-Z, a-z)
- Números (0-9)
- Verificação de unicidade no banco de dados

## 📊 Comandos Úteis

### Parar os containers
```bash
docker-compose down
```

### Ver logs
```bash
docker-compose logs web
docker-compose logs db
```

### Executar comandos no container
```bash
docker-compose exec web bash
```

### Backup do banco de dados
```bash
docker-compose exec db pg_dump -U user encurta_db > backup.sql
```

## 🐛 Solução de Problemas

### Container não inicia
- Verifique se as portas 5000 e 5432 estão disponíveis
- Execute `docker-compose down` e tente novamente

### Erro de conexão com banco
- Aguarde alguns segundos para o PostgreSQL inicializar completamente
- Verifique os logs: `docker-compose logs db`
