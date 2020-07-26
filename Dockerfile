FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
ENV SECRET_KEY = 'reddy dice hola from here xD'

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "microservice/main.py" ]
# CMD [ "flask run" ]
