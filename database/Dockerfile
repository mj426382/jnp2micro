FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED True
ENV PORT 8000
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./requirements.txt ./requirements.txt
RUN apt-get update
RUN pip3 install django



COPY . .
CMD exec python3 manage.py runserver
