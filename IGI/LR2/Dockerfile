FROM python:3.9-slim

LABEL maintainer="Fyodor"

WORKDIR /app

ADD main.py .

ENV RADIUS=10 SIDE=10

RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/smartiqaorg/geometric_lib.git /app/geometric_lib 

CMD ["python", "/app/main.py"]
