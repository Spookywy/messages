FROM python:3-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .tmp-build-deps

RUN adduser --disabled-password app-user

USER app-user

COPY messages ./messages/

EXPOSE 8000

COPY entrypoint.sh .

ENTRYPOINT ["sh", "entrypoint.sh"]
