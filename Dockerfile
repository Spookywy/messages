FROM python:3-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	postgresql-dev gcc python3-dev musl-dev linux-headers

COPY requirements.txt ./
COPY ./scripts /scripts

RUN pip install -r requirements.txt

RUN apk del .tmp-build-deps

RUN adduser --disabled-password app-user

RUN mkdir -p /usr/src/vol/web/static && \
	mkdir -p /usr/src/vol/web/media && \
	chown -R app-user:app-user /usr/src/vol && \
	chmod -R 755 /usr/src/vol && \
	chmod -R +x /scripts

ENV PATH="/scripts:$PATH"

COPY messages ./messages/

WORKDIR /usr/src/app/messages/

EXPOSE 8000

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

USER app-user

CMD ["run.sh"]
