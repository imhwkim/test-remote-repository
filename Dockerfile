FROM python:3.8

WORKDIR /workspace

COPY . /workspace

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT ["jupyter"]

EXPOSE 8888

CMD ["notebook", "--ip", "0.0.0.0", "--port", "8888", "--allow-root", "--ServerApp.token=''"]
