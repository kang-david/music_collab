FROM python:3.9.7-slim-buster

RUN apt-get update && apt-get -y install git

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements /requirements/
RUN pip install -U pip -r /requirements/dev.txt
COPY . ./app
