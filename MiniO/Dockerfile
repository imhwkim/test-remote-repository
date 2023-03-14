FROM python:3.9

ENV PYTHOUNBUFFERED 1

RUN apt-get update && \
	apt-get upgrade -y && \
    apt-get clean && apt-get autoremove -y

WORKDIR /app/mlflow-docker/

RUN python -m pip install --upgrade pip setuptools

ADD requirements.txt /app/mlflow-docker/

RUN pip install -r /app/mlflow-docker/requirements.txt