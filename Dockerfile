FROM python:3

RUN adduser --disabled-password app-user

USER app-user

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY messages ./messages/

EXPOSE 8000

COPY entrypoint.sh .

ENTRYPOINT ["sh", "entrypoint.sh"]
