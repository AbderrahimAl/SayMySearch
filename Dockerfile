FROM ubuntu
WORKDIR /home/es_app
COPY . .
RUN apt-get update -y\
    && apt-get install -y python3.9\
    && apt-get install -y python3-pip\
    && pip3 install -r requirements.txt

WORKDIR /home/es_app

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
