FROM ubuntu:20.04

RUN /usr/bin/apt-get update -y && /usr/bin/apt-get install -y python3 && /usr/bin/apt-get install -y python3-pip

RUN mkdir -p /opt/api

COPY . /opt/api/

WORKDIR /opt/api/

RUN pip install -r requirements.txt

CMD [ "uvicorn", "app.main:app", "--reload" ]
