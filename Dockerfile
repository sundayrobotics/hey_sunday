FROM python:latest
RUN apt-get -y update && \
    apt-get -y full-upgrade \
    && pip install --upgrade pip 

COPY requirements.txt requirements.txt

RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev -y \
        && pip3 install pyaudio     

RUN pip3 install pvporcupine

COPY sample.ppn  .
COPY main.py .

RUN ["python", "main.py"]
