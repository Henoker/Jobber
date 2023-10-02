# Pull base image
FROM python:3.10.4-slim-bullseye
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN sleep 10
RUN pip3 install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD gunicorn -b 0.0.0.0:8000 --worker-class=gevent --worker-connections=1000 --workers=5 backend.wsgi
