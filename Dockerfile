FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

copy ..

CMD uvicorn employee:app --reload