FROM python:3.8.2-alpine as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip && pip install flake8
COPY app .
RUN flake8 --ignore=E501,F401 .

COPY app/requirements/requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python:3.8.2-alpine

RUN mkdir -p /home/app && addgroup -S app && adduser -S app -G app

ENV HOME=/home/app
ENV APP_HOME=/home/app/project_name
WORKDIR $APP_HOME

RUN mkdir staticfiles && mkdir mediafiles && apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache /wheels/*

COPY app/entrypoints/entrypoint.prod.sh .

COPY app .

RUN chown -R app:app .

USER app
RUN ls
ENTRYPOINT ["/home/app/project_name/entrypoint.prod.sh"]