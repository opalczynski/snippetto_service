FROM python:3.7-alpine3.7 as application
ENV PYTHONUNBUFFERED 1
RUN set -e;

RUN apk update
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
    musl-dev \
    libffi-dev \
    libressl-dev \
    build-base

RUN apk add --no-cache libxml2 libxml2-dev

ADD requirements/app.txt /app/requirements/app.txt
RUN pip install -U setuptools --no-cache-dir && \
     pip install -r /app/requirements/app.txt --no-cache-dir

RUN apk del .build-deps

ADD . /app/
WORKDIR /app/

RUN python manage.py collectstatic --no-input
CMD ["sh", "-c", "uwsgi --ini uwsgi.ini:${ENVIRONMENT}"]

FROM application as ci
EXPOSE 8000
RUN pip install -r requirements/ci.txt --no-cache-dir
RUN python manage.py migrate
RUN python manage.py create_test_user
ENV ENVIRONMENT development
ENV DJANGO_SETTINGS_MODULE settings.development
