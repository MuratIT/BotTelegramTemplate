FROM python:3.8

WORKDIR /telegrambot

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . .

