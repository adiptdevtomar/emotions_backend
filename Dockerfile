FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app