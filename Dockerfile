FROM python:3.9-slim-buster

WORKDIR /encurta-url

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txts

ENV FLASK_APP=encurta_url

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "encurta_url:app"]