FROM python:3.7.2
LABEL maintainer="maskeyc@gmail.com"

# create app directory
ENV DOCKERIZE_VERSION="0.1.0" \
    PYTHONUNBUFFERED="1" \
    DJANGO_DB_HOST="" \
    DJANGO_DB_PORT="5432" \
    DJNAGO_SUPERUSER_NAME="" \
    DJANGO_SUPERUSER_MAIL="maskeyc@gmail.com" \
    DJANGO_SUPERUSER_PASS=""

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /django/

WORKDIR /django/

COPY requirements.txt /django/

COPY . /django/

RUN pip install -r /django/requirements.txt

CMD ["python", "manage.py", "migrate"]

EXPOSE 80

#RUN chmod +x entrypoint.sh

#ENTRYPOINT ["/usr/src/docker/madzones_backend/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

VOLUME /django/