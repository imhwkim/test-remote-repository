FROM python:3.8

ENV PYTHOUNBUFFERED 1

RUN apt-get update && \ 
apt-get upgrade -y && \ 
apt-get clean && apt-get autoremove -y

WORKDIR ./work_compose

RUN python -m pip install --upgrade pip setuptools

ADD requirements.txt .

RUN pip install -r ./requirements.txt