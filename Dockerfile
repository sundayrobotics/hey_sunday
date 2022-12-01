FROM python:latest
RUN apt-get -y update && \
    apt-get -y full-upgrade 

COPY requirements.txt requirements.txt

RUN apt install -r requirements.txt && \
    pip3 install -y pvporcupine 

COPY sample.pnn  .
