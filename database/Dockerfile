FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED True
ENV PORT 8000
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./requirements.txt ./requirements.txt
#RUN apt-get update

RUN pip3 install -r requirements.txt


COPY . .

RUN pip3 install django

RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pipenv
RUN pipenv install
#EXPOSE 8000
#CMD pipenv run gunicorn mysite.wsgi:application --bind 0.0.0.0:$PORT
CMD gunicorn mysite.wsgi:application --bind 0.0.0.0:$PORT