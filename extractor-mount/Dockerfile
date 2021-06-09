FROM python:3.8-slim

RUN apt-get update && \
      apt-get -y install sudo
RUN apt install -y -qq python3-pip

RUN python3 -m pip install --upgrade pip

RUN pip3 install pyclowder

COPY . /home

CMD ["python3", "/home/extractor-mount.py"]