# Base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install initial dependencies (psycopg2 and C base)
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY app/requirements/requirements.txt /requirements.txt
COPY app/requirements/dev.txt /dev.txt
RUN pip install -r /dev.txt

# Copy application
COPY app .

RUN cat /usr/src/app/entrypoints/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoints/entrypoint.sh"]