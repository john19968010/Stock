FROM python:3.6.8-slim-stretch
ENV PYTHONUNBUFFERED=1
WORKDIR /stock
COPY requirements.txt /stock/
RUN pip3 install -r requirements.txt
COPY . /stock/
