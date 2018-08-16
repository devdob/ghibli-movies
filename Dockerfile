FROM python:3.5

EXPOSE 8000

RUN apt update -y
RUN apt upgrade -y

WORKDIR /app
COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
