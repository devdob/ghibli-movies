FROM python:3.5

EXPOSE 8000

RUN apt update -y
RUN apt upgrade -y

WORKDIR /app
COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

#RUN python3 manage.py migrate

#CMD python3 manage.py runserver 0.0.0.0:8000
