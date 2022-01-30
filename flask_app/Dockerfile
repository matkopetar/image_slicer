FROM python:3.8.6-alpine

ADD . /app
WORKDIR /app

ENV FLASK_APP=backend/app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000


RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add jpeg-dev zlib-dev libjpeg && \
    pip3 install -r requirements.txt && \
    apk del build-deps

CMD python backend/app.py