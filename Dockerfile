FROM python:3.11.4-slim-buster

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

ENV PORT=8000
EXPOSE $PORT

RUN python manage.py migrate

ENV ADMIN_USERNAME=admin1
ENV ADMIN_EMAIL=admin1@gmail.com

RUN python manage.py createsuperuser \
        --noinput \
        --username $ADMIN_USERNAME \
        --email $ADMIN_EMAIL

CMD python manage.py runserver 0.0.0.0:$PORT
