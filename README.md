# Messages

Messages is a small messaging application.

## Installation using Docker

```docker-compose build```

```docker-compose up```

## Deployment

```docker-compose -f docker-compose-deploy.yml up -d```

The project was deployed on a t2.micro ec2 instance. (AWS)

## Installation without Docker

Create a virtual environment

```virtualenv venv -p python3```

Activate the virtual environment

```source venv/bin/activate```

Install requirements

```pip install -r requirements```

Apply migrations

```python3 manage.py migrate```

Start a Redis server (required by Django channels)

```docker run -p 6379:6379 -d redis```

PostgreSQL is needed to run the project
