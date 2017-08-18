FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update
# RUN apt-get install -y openssl libffi-dev libssl-dev libxml2-dev libxmlsec1-dev libldap2-dev
RUN apt-get install -y libpq-dev postgresql-client-9.4

WORKDIR /exchange/server

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
